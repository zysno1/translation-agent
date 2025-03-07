#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
段落优化器
将时间戳分段的转写结果优化为更适合翻译的语义段落
"""

import re
from typing import List, Dict, Any

from src.utils.log import get_logger

# 获取日志器
logger = get_logger()


class SegmentOptimizer:
    def __init__(self, max_segment_length: int = 1800, min_segment_length: int = 100):
        """
        初始化段落优化器
        
        Args:
            max_segment_length: 段落最大长度（字符数）
            min_segment_length: 段落最小长度（字符数）
        """
        self.max_segment_length = max_segment_length
        self.min_segment_length = min_segment_length
        # 句子结束标志
        self.sentence_end_markers = ['.', '?', '!', '。', '？', '！', '；', ';']
        # 强制段落结束标志（如章节标题等）
        self.paragraph_markers = re.compile(r'^(chapter|\d+\.|section|part|\[music\]|【|\[|\()', re.IGNORECASE)
    
    def is_sentence_end(self, text: str) -> bool:
        """判断文本是否以句子结束标志结尾"""
        if not text:
            return False
        return text.rstrip()[-1] in self.sentence_end_markers
    
    def is_paragraph_break(self, text: str) -> bool:
        """判断文本是否为段落分隔标志（如章节标题）"""
        return bool(self.paragraph_markers.search(text.strip()))
    
    def optimize_segments(self, segments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        优化时间戳分段的转写结果，合并为语义段落
        
        Args:
            segments: 时间戳分段的转写结果，每个元素应包含text、start和end字段
            
        Returns:
            优化后的段落列表，每个元素包含text、start和end字段
        """
        logger.info(f"优化前段落数: {len(segments)}")
        
        # 步骤1: 基于句子完整性进行初步分段
        sentences = []
        current_sentence = []
        
        for segment in segments:
            text = segment.get('text', '')
            start_time = segment.get('start', 0.0)
            end_time = segment.get('end', start_time)
            
            # 添加当前文本片段到句子
            current_sentence.append({
                'text': text,
                'start': start_time,
                'end': end_time
            })
            
            # 如果是句子结束或段落分隔符，则结束当前句子
            if self.is_sentence_end(text) or self.is_paragraph_break(text):
                if current_sentence:
                    sentences.append(current_sentence)
                    current_sentence = []
        
        # 处理最后一个未完成的句子
        if current_sentence:
            sentences.append(current_sentence)
        
        logger.info(f"分句后数量: {len(sentences)}")
        
        # 步骤2: 合并短句组成语义段落
        merged_segments = []
        current_merge = []
        current_length = 0
        
        for sentence in sentences:
            sentence_text = ' '.join([s['text'] for s in sentence])
            sentence_length = len(sentence_text)
            
            # 如果当前合并段落为空，直接添加
            if not current_merge:
                current_merge.extend(sentence)
                current_length = sentence_length
                continue
            
            # 判断是否可以继续合并
            if (current_length + sentence_length <= self.max_segment_length) and \
               not self.is_paragraph_break(sentence[0]['text']):
                current_merge.extend(sentence)
                current_length += sentence_length
            else:
                # 保存当前段落并开始新段落
                if current_merge:
                    merged_segments.append({
                        'text': ' '.join([s['text'] for s in current_merge]),
                        'start': current_merge[0]['start'],
                        'end': current_merge[-1]['end']
                    })
                current_merge = sentence
                current_length = sentence_length
        
        # 处理最后一个段落
        if current_merge:
            merged_segments.append({
                'text': ' '.join([s['text'] for s in current_merge]),
                'start': current_merge[0]['start'],
                'end': current_merge[-1]['end']
            })
        
        logger.info(f"合并短句后段落数: {len(merged_segments)}")
        
        # 步骤3: 处理过短的段落
        final_segments = []
        to_merge = None
        
        for segment in merged_segments:
            if len(segment['text']) < self.min_segment_length and not self.is_paragraph_break(segment['text']):
                # 过短的段落，尝试与下一个合并
                if to_merge is None:
                    to_merge = segment
                else:
                    # 合并两个短段落
                    to_merge = {
                        'text': to_merge['text'] + ' ' + segment['text'],
                        'start': to_merge['start'],
                        'end': segment['end']
                    }
            else:
                # 正常长度的段落
                if to_merge is not None:
                    # 先处理之前累积的短段落
                    combined_text = to_merge['text'] + ' ' + segment['text']
                    if len(combined_text) <= self.max_segment_length:
                        # 可以合并
                        final_segments.append({
                            'text': combined_text,
                            'start': to_merge['start'],
                            'end': segment['end']
                        })
                        to_merge = None
                    else:
                        # 不能合并，单独保存
                        final_segments.append(to_merge)
                        final_segments.append(segment)
                        to_merge = None
                else:
                    final_segments.append(segment)
        
        # 处理最后可能剩余的短段落
        if to_merge is not None:
            final_segments.append(to_merge)
        
        logger.info(f"优化后段落数: {len(final_segments)}")
        
        return final_segments 