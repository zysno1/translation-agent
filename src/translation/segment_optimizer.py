#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
段落优化器模块
用于优化翻译段落，合并短段落，分割长段落
"""

import re
from typing import List, Dict, Any

from src.utils.log import get_logger

# 获取日志器
logger = get_logger()


class SegmentOptimizer:
    """段落优化器，用于优化翻译段落"""
    
    def __init__(self, max_segment_length: int = 1800, min_segment_length: int = 100):
        """
        初始化段落优化器
        
        Args:
            max_segment_length: 最大段落长度（字符数）
            min_segment_length: 最小段落长度（字符数）
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
        优化段落，合并短段落，分割长段落
        
        Args:
            segments: 原始段落列表，每个段落是一个字典，包含text, start, end等字段
            
        Returns:
            优化后的段落列表
        """
        if not segments:
            return []
        
        # 按时间顺序排序
        sorted_segments = sorted(segments, key=lambda x: x.get('start', 0))
        
        # 合并短段落
        merged_segments = self._merge_short_segments(sorted_segments)
        
        # 分割长段落
        # 注意：当前实现仅合并短段落，不分割长段落
        # optimized_segments = self._split_long_segments(merged_segments)
        
        return merged_segments
    
    def _merge_short_segments(self, segments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        合并短段落
        
        Args:
            segments: 按时间顺序排序的段落列表
            
        Returns:
            合并后的段落列表
        """
        if not segments:
            return []
        
        result = []
        current_segment = segments[0].copy()
        current_text = current_segment.get('text', '')
        
        for i in range(1, len(segments)):
            segment = segments[i]
            text = segment.get('text', '')
            
            # 如果当前段落文本长度小于最小长度，且合并后不超过最大长度，则合并
            if len(current_text) < self.min_segment_length and len(current_text + ' ' + text) <= self.max_segment_length:
                # 更新结束时间
                current_segment['end'] = segment.get('end', 0)
                # 合并文本
                current_text = current_text + ' ' + text
                current_segment['text'] = current_text
            else:
                # 添加当前段落到结果
                result.append(current_segment)
                # 开始新的段落
                current_segment = segment.copy()
                current_text = current_segment.get('text', '')
        
        # 添加最后一个段落
        result.append(current_segment)
        
        return result
    
    def _split_long_segments(self, segments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        分割长段落（当前未实现）
        
        Args:
            segments: 段落列表
            
        Returns:
            分割后的段落列表
        """
        # 当前简单实现，不分割长段落
        return segments 