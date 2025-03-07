#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
报告生成模块 - 负责创建基于内容的视频翻译处理报告
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
import re
import logging
from typing import Dict, List, Tuple, Any, Optional

from src.utils.log import get_logger
from src.config.config_manager import get_config

logger = logging.getLogger(__name__)

class ReportGenerator:
    """视频翻译处理报告生成器"""
    
    def __init__(self, output_dir: Optional[str] = None):
        """
        初始化报告生成器
        
        Args:
            output_dir: 报告输出目录，默认从配置获取
        """
        config = get_config()
        storage_config = config.get('storage', {})
        
        # 如果未指定，从配置获取，默认为"./reports"
        if output_dir is None:
            output_dir = storage_config.get('reports_dir', './reports')
        
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"报告生成器初始化完成，输出目录: {self.output_dir}")
    
    def generate_report(self, 
                        transcript: Dict[str, Any], 
                        translation: Dict[str, Any], 
                        video_info: Dict[str, Any],
                        processing_stats: Dict[str, Any]) -> str:
        """
        生成完整的视频翻译处理报告
        
        Args:
            transcript: 转录结果
            translation: 翻译结果
            video_info: 视频信息
            processing_stats: 处理统计信息
            
        Returns:
            报告文件保存路径
        """
        # 生成报告文件名
        
        # 提取作者信息
        author = self._extract_author_info(video_info, transcript)
        
        # 生成时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 组合文件名
        report_filename = f"report_{author}_{timestamp}.md"
        report_path = os.path.join(self.output_dir, report_filename)
        
        # 更新processing_stats中的导出文件信息
        if 'exported_files' in processing_stats:
            processing_stats['exported_files']['报告文件 (Markdown)'] = report_path
        
        # 获取摘要数据（如果存在）
        summary = processing_stats.get('summary_data', {})
        
        # 准备报告内容
        report_content = self._format_report(transcript, translation, video_info, processing_stats)
        
        # 保存报告文件
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            logger.info(f"报告已生成并保存: {report_path}")
        except Exception as e:
            logger.error(f"保存报告失败: {e}")
            raise
        
        return report_path
    
    def _format_report(self, 
                      transcript: Dict[str, Any], 
                      translation: Dict[str, Any], 
                      video_info: Dict[str, Any],
                      processing_stats: Dict[str, Any]) -> str:
        """
        格式化整个报告内容
        
        Args:
            transcript: 转录结果
            translation: 翻译结果
            video_info: 视频信息
            processing_stats: 处理统计信息
            
        Returns:
            完整报告内容
        """
        # 生成视频信息部分
        video_info_section = self._format_video_info(video_info)
        
        # 生成处理统计部分
        stats_section = self._format_processing_stats(processing_stats)
        
        # 生成导出文件部分
        export_files_section = self._format_export_files(processing_stats.get('exported_files', {}))
        
        # 获取摘要数据（如果存在）
        summary = processing_stats.get('summary_data', {})
        
        # 生成内容概览部分
        overview_section = self._format_content_overview(transcript, translation, summary)
        
        # 生成完整对照翻译部分
        translation_section = self._format_translation_content(transcript, translation)
        
        # 组合报告
        report = f"""# 视频翻译处理报告

{video_info_section}

{stats_section}

{export_files_section}

{overview_section}

{translation_section}

## 处理日志
{self._format_processing_logs(processing_stats.get('logs', []))}

## 建议操作
- 检查翻译质量，特别是专业术语和复杂表达
- 校对时间戳是否与视频内容同步
- 确认章节划分是否准确反映内容结构
- 考虑为重要概念添加注释或解释
"""
        return report
    
    def _format_video_info(self, video_info: Dict[str, Any]) -> str:
        """格式化视频信息部分"""
        video_length = video_info.get('duration_str', 'unknown')
        if not video_length or video_length == 'unknown':
            seconds = video_info.get('duration', 0)
            if seconds:
                hours, remainder = divmod(seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                video_length = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        return f"""## 视频信息
- 视频标题：{video_info.get('title', '未知标题')}
- 视频来源：{video_info.get('source', 'YouTube')}
- 视频长度：{video_length}
- 视频ID/链接：{video_info.get('id', video_info.get('url', '未知'))}
- 原始语言：{video_info.get('language', '未知')}
- 目标语言：{video_info.get('target_language', '中文')}
"""
    
    def _format_processing_stats(self, stats: Dict[str, Any]) -> str:
        """格式化处理统计部分"""
        start_time = stats.get('start_time', 'unknown')
        end_time = stats.get('end_time', 'unknown')
        
        # 如果时间是时间戳，转换为可读格式
        if isinstance(start_time, (int, float)):
            start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, (int, float)):
            end_time = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
            
        return f"""## 处理统计
- 处理时间：{start_time} 至 {end_time}
- 音频提取耗时：{self._format_duration(stats.get('audio_extraction_time', 0))}
- 转录耗时：{self._format_duration(stats.get('transcription_time', 0))}
- 翻译耗时：{self._format_duration(stats.get('translation_time', 0))}
- 内容章节数：{stats.get('num_chapters', '未计算')}
- 总字数（原文）：{stats.get('source_word_count', '未计算')}
- 总字数（译文）：{stats.get('target_word_count', '未计算')}
"""
    
    def _format_export_files(self, files: Dict[str, str]) -> str:
        """格式化导出文件部分"""
        files_section = "## 导出文件\n\n"
        
        if not files:
            files_section += "*没有导出文件记录*\n\n"
            return files_section
        
        # 添加表格头
        files_section += "| 文件类型 | 文件路径 |\n"
        files_section += "| ------- | ------- |\n"
        
        # 添加文件记录
        for format_name, file_path in files.items():
            if file_path:  # 只显示有路径的文件
                files_section += f"| {format_name} | `{file_path}` |\n"
        
        files_section += "\n"
        return files_section
    
    def _format_content_overview(self, transcript: Dict[str, Any], translation: Dict[str, Any], summary: Dict[str, Any] = None) -> str:
        """
        格式化内容概览部分，包括主题摘要、关键词和内容结构
        
        Args:
            transcript: 转录结果
            translation: 翻译结果
            summary: 摘要结果（如果有）
            
        Returns:
            格式化的内容概览文本
        """
        # 获取文本内容
        original_text = transcript.get('text', '')
        translated_text = translation.get('text', '')
        
        # 主题摘要
        summary_text = ""
        if summary and 'text' in summary:
            # 如果有预先生成的摘要，使用它
            summary_text = summary.get('text', '')
            
            # 将Markdown格式改为plaintext以便在代码块中显示
            if summary_text.startswith('```'):
                summary_text = summary_text.strip('`')
            
        elif translated_text:
            # 如果没有摘要但有翻译文本，使用翻译文本的前200个字符
            summary_text = f"{translated_text[:200]}..."
        elif original_text:
            # 如果没有翻译文本，使用原文的前200个字符
            summary_text = f"{original_text[:200]}..."
        
        # 提取关键词
        keywords = []
        if translated_text:
            keywords = self._extract_keywords(translated_text)
        elif original_text:
            keywords = self._extract_keywords(original_text)
        
        keywords_str = ", ".join(keywords) if keywords else "没有足够的文本提取关键词"
        
        # 生成章节结构
        chapters = self._identify_chapters(transcript, translation)
        chapter_list = ""
        if chapters:
            for i, chapter in enumerate(chapters):
                chapter_list += f"{i+1}. {chapter['title']}\n"
        else:
            chapter_list = "未能识别出明确的章节结构"
        
        # 组合概览部分
        return f"""## 内容概览
### 视频主题摘要
```plaintext
{summary_text}
```

### 关键词
{keywords_str}

### 内容结构
{chapter_list}
"""
    
    def _format_translation_content(self, transcript: Dict[str, Any], translation: Dict[str, Any]) -> str:
        """格式化完整对照翻译部分，确保原文和译文一一对照"""
        # 初始化翻译内容区域
        translation_section = "## 完整对照翻译\n\n"
        
        # 获取分段数据
        segments = transcript.get('segments', [])
        translated_segments = translation.get('segments', [])
        
        # 如果没有分段数据但有原文和译文文本，则尝试根据句号、问号、感叹号等标点符号分段
        if (not segments or not translated_segments) and transcript.get('text') and translation.get('text'):
            original_text = transcript.get('text', '')
            translated_text = translation.get('text', '')
            
            # 创建简单的分段
            import re
            
            # 尝试按句子拆分原文
            sentence_pattern = r'(?<=[.!?。！？])\s+'
            original_sentences = re.split(sentence_pattern, original_text)
            
            # 如果原文能够被分割成句子，并且译文也有文本，则创建人工分段
            if original_sentences and translated_text:
                translation_section += "### 按句分段对照翻译\n\n"
                translation_section += "| 时间 | 原文 | 译文 |\n"
                translation_section += "|------|------|------|\n"
                
                # 尝试按相同模式拆分译文
                translated_sentences = re.split(sentence_pattern, translated_text)
                
                # 如果译文句子数量与原文不匹配，可能需要重新拆分
                if len(original_sentences) != len(translated_sentences):
                    # 简单处理：尝试按段落拆分
                    original_sentences = original_text.split('\n\n')
                    translated_sentences = translated_text.split('\n\n')
                
                # 取较短的列表长度，避免索引越界
                min_length = min(len(original_sentences), len(translated_sentences))
                
                # 创建对照表格
                for i in range(min_length):
                    # 创建假时间戳 - 因为没有精确时间信息，按比例估计
                    estimated_time = self._format_timestamp(i * (transcript.get('duration', 0) / min_length))
                    
                    # 格式化原文和译文，确保不会太长
                    orig = original_sentences[i].strip()
                    trans = translated_sentences[i].strip()
                    
                    # 如果文本过长，截断显示
                    if len(orig) > 100:
                        orig = orig[:97] + "..."
                    if len(trans) > 100:
                        trans = trans[:97] + "..."
                    
                    # 添加到表格
                    translation_section += f"| {estimated_time} | {orig} | {trans} |\n"
                
                # 添加完整文本部分
                translation_section += "\n### 完整文本\n\n"
                translation_section += "#### 原文\n\n```\n"
                translation_section += original_text
                translation_section += "\n```\n\n"
                translation_section += "#### 译文\n\n```\n"
                translation_section += translated_text
                translation_section += "\n```\n\n"
                
                return translation_section
            else:
                # 回退到显示完整文本
                translation_section += "### 完整文本\n\n"
                translation_section += "#### 原文\n\n```\n"
                translation_section += original_text
                translation_section += "\n```\n\n"
                translation_section += "#### 译文\n\n```\n"
                translation_section += translated_text
                translation_section += "\n```\n\n"
                
                return translation_section
        
        # 如果有segment数据，使用时间戳创建对照表格
        elif segments and len(segments) > 0:
            # 创建对照表格
            translation_section += "### 分段对照翻译\n\n"
            translation_section += "| 时间范围 | 原文 | 译文 |\n"
            translation_section += "|---------|------|------|\n"
            
            # 如果译文段落与原文不匹配，尝试创建合理的映射
            if len(segments) != len(translated_segments):
                logger.warning(f"转录段落数({len(segments)})与翻译段落数({len(translated_segments)})不一致")
                
                # 如果有译文但没有译文segments，尝试分配译文
                if len(translated_segments) == 0 and translation.get('text'):
                    full_translation = translation.get('text', '')
                    
                    # 按段落比例分配译文
                    total_length = len(full_translation)
                    segment_positions = []
                    
                    # 计算原文段落的相对位置
                    full_original = transcript.get('text', '')
                    total_original_length = len(full_original) if full_original else 1
                    
                    # 为每个原文段落计算在完整文本中的相对位置
                    for segment in segments:
                        segment_text = segment.get('text', '')
                        rel_pos = full_original.find(segment_text) / total_original_length if segment_text in full_original else -1
                        segment_positions.append((segment, rel_pos))
                    
                    # 按相对位置排序
                    segment_positions.sort(key=lambda x: x[1] if x[1] >= 0 else float('inf'))
                    
                    # 为每个段落分配一部分译文
                    for i, (segment, _) in enumerate(segment_positions):
                        start_ratio = i / len(segments)
                        end_ratio = (i + 1) / len(segments)
                        
                        start_pos = int(start_ratio * total_length)
                        end_pos = int(end_ratio * total_length)
                        
                        # 确保不会超出译文长度
                        end_pos = min(end_pos, total_length)
                        
                        # 提取这一部分译文
                        segment_translation = full_translation[start_pos:end_pos]
                        
                        # 获取时间戳
                        start_time = self._format_timestamp(segment.get('start', 0))
                        end_time = self._format_timestamp(segment.get('end', 0))
                        time_range = f"{start_time} - {end_time}"
                        
                        # 格式化原文和译文，确保不会太长
                        orig = segment.get('text', '').strip()
                        trans = segment_translation.strip()
                        
                        # 如果文本过长，截断显示
                        if len(orig) > 100:
                            orig = orig[:97] + "..."
                        if len(trans) > 100:
                            trans = trans[:97] + "..."
                        
                        # 添加到表格
                        translation_section += f"| {time_range} | {orig} | {trans} |\n"
                else:
                    # 使用比较短的分段列表
                    min_length = min(len(segments), len(translated_segments))
                    
                    for i in range(min_length):
                        original_segment = segments[i]
                        translated_segment = translated_segments[i]
                        
                        # 获取时间戳
                        start_time = self._format_timestamp(original_segment.get('start', 0))
                        end_time = self._format_timestamp(original_segment.get('end', 0))
                        time_range = f"{start_time} - {end_time}"
                        
                        # 格式化原文和译文，确保不会太长
                        orig = original_segment.get('text', '').strip()
                        trans = translated_segment.get('text', '').strip()
                        
                        # 如果文本过长，截断显示
                        if len(orig) > 100:
                            orig = orig[:97] + "..."
                        if len(trans) > 100:
                            trans = trans[:97] + "..."
                        
                        # 添加到表格
                        translation_section += f"| {time_range} | {orig} | {trans} |\n"
            else:
                # 如果段落数量匹配，直接创建对照表格
                for i in range(len(segments)):
                    original_segment = segments[i]
                    translated_segment = translated_segments[i]
                    
                    # 获取时间戳
                    start_time = self._format_timestamp(original_segment.get('start', 0))
                    end_time = self._format_timestamp(original_segment.get('end', 0))
                    time_range = f"{start_time} - {end_time}"
                    
                    # 格式化原文和译文
                    orig = original_segment.get('text', '').strip()
                    trans = translated_segment.get('text', '').strip()
                    
                    # 如果文本过长，截断显示
                    if len(orig) > 100:
                        orig = orig[:97] + "..."
                    if len(trans) > 100:
                        trans = trans[:97] + "..."
                    
                    # 添加到表格
                    translation_section += f"| {time_range} | {orig} | {trans} |\n"
            
            # 添加完整文本部分
            translation_section += "\n### 完整文本\n\n"
            translation_section += "#### 原文\n\n```\n"
            translation_section += transcript.get('text', '')
            translation_section += "\n```\n\n"
            translation_section += "#### 译文\n\n```\n"
            translation_section += translation.get('text', '')
            translation_section += "\n```\n\n"
        else:
            # 如果没有足够的分段数据，只显示完整文本
            translation_section += "### 完整文本\n\n"
            translation_section += "#### 原文\n\n```\n"
            translation_section += transcript.get('text', '')
            translation_section += "\n```\n\n"
            translation_section += "#### 译文\n\n```\n"
            translation_section += translation.get('text', '')
            translation_section += "\n```\n\n"
        
        return translation_section
    
    def _format_processing_logs(self, logs: List[str]) -> str:
        """格式化处理日志部分"""
        if not logs:
            return "处理过程中未记录特殊情况。"
        
        return "\n".join([f"- {log}" for log in logs])
    
    def _identify_chapters(self, transcript: Dict[str, Any], translation: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        识别内容中的章节和段落
        
        这是一个复杂的NLP任务，简单实现：
        1. 基于时间间隔识别可能的章节边界
        2. 查找有明显标题特征的文本（如"第一部分"，"Introduction"等）
        3. 结合两者确定章节划分
        
        Args:
            transcript: 转录结果
            translation: 翻译结果
            
        Returns:
            章节列表，每个章节包含标题和段落
        """
        # 获取所有段落
        segments = transcript.get('segments', [])
        translated_segments = translation.get('segments', [])
        
        # 确保两个列表长度一致
        if len(segments) != len(translated_segments):
            logger.warning(f"转录段落数({len(segments)})与翻译段落数({len(translated_segments)})不一致，使用较短的列表")
            min_length = min(len(segments), len(translated_segments))
            segments = segments[:min_length]
            translated_segments = translated_segments[:min_length]
        
        # 简单实现：按照固定数量的段落划分章节
        chapter_size = max(5, len(segments) // 8)  # 每章至少5个段落，最多8章
        
        chapters = []
        current_paragraphs = []
        current_start_idx = 0
        
        for i, (seg, trans_seg) in enumerate(zip(segments, translated_segments)):
            # 将相邻的段落组合成一个逻辑段落
            if i > 0 and i % chapter_size == 0:
                # 创建一个新章节
                chapter_title = self._extract_chapter_title(segments[current_start_idx:i], translated_segments[current_start_idx:i])
                
                chapters.append({
                    'title': chapter_title,
                    'paragraphs': current_paragraphs,
                    'start_index': current_start_idx,
                    'end_index': i - 1
                })
                
                # 重置当前段落和起始索引
                current_paragraphs = []
                current_start_idx = i
            
            # 添加当前段落
            current_paragraphs.append({
                'original_text': seg.get('text', ''),
                'translated_text': trans_seg.get('text', ''),
                'start_time': seg.get('start', 0),
                'end_time': seg.get('end', 0)
            })
        
        # 添加最后一个章节
        if current_paragraphs:
            chapter_title = self._extract_chapter_title(
                segments[current_start_idx:], 
                translated_segments[current_start_idx:]
            )
            
            chapters.append({
                'title': chapter_title,
                'paragraphs': current_paragraphs,
                'start_index': current_start_idx,
                'end_index': len(segments) - 1
            })
        
        return chapters
    
    def _extract_chapter_title(self, segments: List[Dict[str, Any]], translated_segments: List[Dict[str, Any]]) -> str:
        """
        从段落中提取章节标题
        
        简单实现：
        1. 查找包含标题特征的文本
        2. 如果没有找到，使用第一个段落的前几个词
        
        Args:
            segments: 原文段落列表
            translated_segments: 翻译段落列表
            
        Returns:
            提取的章节标题
        """
        # 标题关键词模式
        title_patterns = [
            r'chapter\s+\d+', r'section\s+\d+', r'part\s+\d+',
            r'introduction', r'conclusion', r'summary',
            r'第.+章', r'第.+节', r'第.+部分',
            r'简介', r'结论', r'总结'
        ]
        
        # 遍历前几个段落，查找标题
        for i, (seg, trans_seg) in enumerate(zip(segments[:3], translated_segments[:3])):
            text = seg.get('text', '').lower()
            trans_text = trans_seg.get('text', '')
            
            # 查找标题模式
            for pattern in title_patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    return text[:50] + '...' if len(text) > 50 else text
                
                match = re.search(pattern, trans_text, re.IGNORECASE)
                if match:
                    return trans_text[:50] + '...' if len(trans_text) > 50 else trans_text
        
        # 如果没有找到标题，使用第一个段落的前几个词
        first_text = segments[0].get('text', '')
        first_trans = translated_segments[0].get('text', '')
        
        # 使用翻译文本作为标题（如果有）
        if first_trans:
            words = first_trans.split()
            title = ' '.join(words[:5]) + '...' if len(words) > 5 else first_trans
            return title[:50] + '...' if len(title) > 50 else title
        
        # 否则使用原文
        words = first_text.split()
        title = ' '.join(words[:5]) + '...' if len(words) > 5 else first_text
        return title[:50] + '...' if len(title) > 50 else title
    
    def _extract_keywords(self, text: str, count: int = 8) -> List[str]:
        """
        提取文本中的关键词
        使用词频统计和停用词过滤来提取关键词
        
        Args:
            text: 要分析的文本
            count: 要返回的关键词数量
            
        Returns:
            关键词列表
        """
        import re
        
        try:
            # 如果文本为空或过短，返回空列表
            if not text or len(text) < 50:
                return []
            
            # 中英文停用词列表
            stop_words = set([
                '的', '了', '和', '是', '就', '都', '而', '及', '与', '着', '或', '一个', '没有',
                'the', 'and', 'to', 'of', 'a', 'in', 'that', 'is', 'for', 'on', 'with', 'as', 'this', 'by', 'are',
                'at', 'be', 'it', 'we', 'you', 'will', 'can', 'from', 'have', 'has', 'had', 'was', 'were', 'they',
                'their', 'an', 'or', 'if', 'but', 'which', 'what', 'when', 'who', 'how', 'where', 'there'
            ])
            
            # 清理文本
            clean_text = re.sub(r'[^\w\s\u4e00-\u9fff]', ' ', text)
            
            try:
                # 尝试使用jieba分词（如果已安装）
                import jieba
                # 中文分词
                if re.search(r'[\u4e00-\u9fff]', clean_text):
                    words = list(jieba.cut(clean_text))
                    # 过滤停用词和单字词
                    words = [word for word in words if word not in stop_words and len(word) > 1]
            except ImportError:
                # 如果没有安装jieba，使用简单的空格分词
                words = clean_text.split()
            
            # 计算词频
            word_counts = {}
            for word in words:
                if word.lower() not in stop_words and len(word) > 1:
                    word_counts[word] = word_counts.get(word, 0) + 1
            
            # 按频率排序
            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            
            # 提取关键词（避免重复）
            keywords = []
            for word, _ in sorted_words:
                # 跳过空词和单个字符
                if not word.strip() or len(word) <= 1:
                    continue
                
                # 检查关键词是否已包含或是子字符串
                is_duplicate = False
                for existing_kw in keywords:
                    if word in existing_kw or existing_kw in word:
                        is_duplicate = True
                        break
                    
                if not is_duplicate:
                    keywords.append(word)
                
                # 达到所需数量后停止
                if len(keywords) >= count:
                    break
                
            return keywords
                
        except Exception as e:
            logger.error(f"提取关键词时出错: {str(e)}")
            # 回退到非常简单的词频统计
            words = text.lower().split()
            word_counts = {}
            
            for word in words:
                # 跳过短词
                if len(word) <= 2:
                    continue
                word = re.sub(r'[^\w\s\u4e00-\u9fff]', '', word)
                if word:
                    word_counts[word] = word_counts.get(word, 0) + 1
                
            # 按频率排序
            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            
            # 返回top N的单词
            return [word for word, _ in sorted_words[:count]]
    
    def _format_timestamp(self, seconds: float) -> str:
        """将秒数格式化为时间戳字符串 (HH:MM:SS)"""
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def _format_duration(self, seconds: float) -> str:
        """将秒数格式化为持续时间字符串"""
        if seconds < 60:
            return f"{seconds:.2f}秒"
        elif seconds < 3600:
            minutes, seconds = divmod(seconds, 60)
            return f"{int(minutes)}分{int(seconds)}秒"
        else:
            hours, remainder = divmod(seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)}小时{int(minutes)}分{int(seconds)}秒"
    
    def _sanitize_filename(self, filename: str) -> str:
        """净化文件名，移除不合法字符"""
        # 替换不合法字符
        sanitized = re.sub(r'[\\/*?:"<>|]', "_", filename)
        # 限制长度
        if len(sanitized) > 100:
            sanitized = sanitized[:97] + "..."
        return sanitized
    
    def _extract_author_info(self, video_info: Dict[str, Any], transcript: Dict[str, Any] = None) -> str:
        """
        从视频信息或转写结果中提取作者信息
        
        Args:
            video_info: 视频信息字典
            transcript: 转写结果字典（可选）
            
        Returns:
            处理后的作者名称
        """
        author = None
        
        # 首先尝试从视频信息中获取
        if video_info:
            # 按优先级尝试不同的字段
            for field in ['author', 'creator', 'uploader', 'channel', 'speaker']:
                if field in video_info and video_info[field]:
                    author = video_info[field]
                    break
                    
            # 如果没有找到，尝试从其他字段提取
            if not author and 'title' in video_info:
                # 使用视频标题
                title = video_info.get('title', '')
                if title:
                    # 使用标题前10个字符
                    author = self._sanitize_filename(title[:10])
        
        # 如果从视频信息中无法获取，尝试从转写结果中获取
        if not author and transcript:
            metadata = transcript.get('metadata', {})
            # 尝试不同的可能字段
            for field in ['author', 'creator', 'uploader', 'channel', 'speaker']:
                if field in metadata and metadata[field]:
                    author = metadata[field]
                    break
        
        # 如果仍然无法获取，使用默认值
        if not author:
            author = "unknown"
            
        # 处理作者名称
        return self._sanitize_filename(author) 