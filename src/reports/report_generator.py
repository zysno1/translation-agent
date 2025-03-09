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
        
        # 获取导出文件信息（虽然不在报告中显示，但保留此调用以便其他地方使用）
        _ = self._format_export_files(processing_stats.get('exported_files', {}))
        
        # 获取摘要数据（如果存在）
        summary = processing_stats.get('summary_data', {})
        
        # 生成内容概览部分 - 但不包含快速导航、关键词、内容结构和专业术语解释
        overview_section = self._format_content_overview_simplified(transcript, translation, summary)
        
        # 生成关键观点部分
        key_points = self._format_key_points(translation, summary)
        
        # 生成完整对照翻译部分 - 不包含按句分段对照翻译和内容时长分布图
        translation_section = self._format_translation_content_simplified(transcript, translation)
        
        # 生成相关资源部分
        related_resources = self._format_related_resources(video_info)
        
        # 组合报告 - 不包含导出文件、处理日志和建议操作部分
        report = f"""# 视频翻译处理报告

{video_info_section}

{stats_section}

{overview_section}

{key_points}

{translation_section}

{related_resources}
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
        
        # 从上传者字段或频道信息中提取频道/发布者信息
        uploader = video_info.get('uploader', '')
        channel = video_info.get('channel', '')
        creator = uploader or channel or '未知发布者'
        
        # 获取发布日期并格式化
        upload_date = video_info.get('upload_date', '')
        if upload_date and len(upload_date) == 8:  # 通常格式为YYYYMMDD
            try:
                year = upload_date[:4]
                month = upload_date[4:6]
                day = upload_date[6:8]
                upload_date = f"{year}-{month}-{day}"
            except:
                pass  # 如果格式解析失败，保持原样
        
        # 构建视频缩略图URL
        video_id = video_info.get('id', '')
        thumbnail_url = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg" if video_id else ''
        thumbnail_html = f"![视频缩略图]({thumbnail_url})" if thumbnail_url else ''
        
        # 构建视频分类信息
        categories = video_info.get('categories', [])
        category_str = '、'.join(categories) if categories else '未分类'
        
        # 构建视频链接
        video_url = f"https://www.youtube.com/watch?v={video_id}" if video_id else video_info.get('url', '')
        
        return f"""## 视频信息
- 视频标题：{video_info.get('title', '未知标题')}
- 频道/发布者：{creator}
- 发布日期：{upload_date or '未知'}
- 视频长度：{video_length}
- 视频分类：{category_str}
- 视频ID：{video_id}
- 观看链接：[点击观看原视频]({video_url})
- 原始语言：{video_info.get('language', 'en')}
- 目标语言：{video_info.get('target_language', '中文')}

{thumbnail_html}
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
    
    def _format_content_overview_simplified(self, transcript: Dict[str, Any], translation: Dict[str, Any], summary: Dict[str, Any]) -> str:
        """
        格式化内容概览部分 - 简化版本，不包含快速导航、关键词、内容结构和专业术语解释
        
        Args:
            transcript: 转录结果
            translation: 翻译结果
            summary: 摘要数据
            
        Returns:
            内容概览部分的格式化文本
        """
        # 获取摘要文本
        summary_text = summary.get('summary', '')
        if not summary_text and translation.get('text'):
            # 如果没有摘要但有翻译文本，尝试提取开头部分作为简单摘要
            text = translation.get('text', '')
            # 提取前200个字符作为简要摘要
            summary_text = text[:200] + ('...' if len(text) > 200 else '')
        
        # 使用div和样式增强摘要显示
        enhanced_summary = f"""<div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9; margin: 10px 0;">
{summary_text}
</div>"""
        
        # 组合概览部分 - 仅包含视频主题摘要
        return f"""## 内容概览

### 视频主题摘要
{enhanced_summary}
"""
    
    def _format_translation_content_simplified(self, transcript: Dict[str, Any], translation: Dict[str, Any]) -> str:
        """
        格式化完整对照翻译部分 - 按时间轴分段显示原文和译文
        
        Args:
            transcript: 转录结果
            translation: 翻译结果
            
        Returns:
            完整对照翻译部分的格式化文本
        """
        # 初始化翻译内容区域
        translation_section = "## 完整对照翻译\n\n"
        
        # 获取分段数据
        segments = transcript.get('segments', [])
        translated_segments = translation.get('segments', [])
        
        # 如果有分段数据，则按时间轴展示
        if segments and translated_segments:
            # 将文本分成多个小块，每个块不超过200个字符
            # 取较短的分段数量
            min_length = min(len(segments), len(translated_segments))
            
            # 创建一个函数来分割长文本
            def split_text(text, max_length=200):
                """将长文本分割成较短的片段"""
                # 如果文本足够短，直接返回
                if len(text) <= max_length:
                    return [text]
                
                # 尝试在空格、标点符号处分割
                parts = []
                current_part = ""
                words = text.split(" ")
                
                for word in words:
                    if len(current_part + " " + word) <= max_length:
                        current_part += " " + word if current_part else word
                    else:
                        parts.append(current_part)
                        current_part = word
                
                if current_part:
                    parts.append(current_part)
                
                return parts
            
            # 长文本分割后的分段数
            text_parts = []
            text_parts_translation = []
            time_ranges = []
            
            # 以几乎相等的时间间隔创建大约10-15个分段
            target_segment_count = 10
            segment_size = max(1, min_length // target_segment_count)
            
            for i in range(0, min_length, segment_size):
                end_idx = min(i + segment_size, min_length)
                
                # 获取时间戳
                start_time = segments[i].get('start', 0)
                end_time = segments[end_idx-1].get('end', 0) if end_idx > i else segments[i].get('end', start_time + 60)
                
                # 收集这个分段内的所有文本
                original_text = " ".join(seg.get('text', '').strip() for seg in segments[i:end_idx] if seg.get('text', '').strip())
                translated_text = " ".join(seg.get('text', '').strip() for seg in translated_segments[i:end_idx] if seg.get('text', '').strip())
                
                # 分割长文本
                if len(original_text) > 200:
                    orig_parts = split_text(original_text)
                    # 如果原文被分割，也相应地分割译文
                    if len(orig_parts) > 1:
                        # 简单按照相同比例分割译文
                        trans_parts = []
                        avg_part_size = len(translated_text) / len(orig_parts)
                        for j in range(len(orig_parts)):
                            start_pos = int(j * avg_part_size)
                            end_pos = int((j + 1) * avg_part_size) if j < len(orig_parts) - 1 else len(translated_text)
                            trans_parts.append(translated_text[start_pos:end_pos])
                        
                        # 为每个分割部分创建对应的时间范围
                        part_duration = (end_time - start_time) / len(orig_parts)
                        for j in range(len(orig_parts)):
                            part_start = start_time + j * part_duration
                            part_end = start_time + (j + 1) * part_duration if j < len(orig_parts) - 1 else end_time
                            text_parts.append(orig_parts[j])
                            text_parts_translation.append(trans_parts[j])
                            time_ranges.append((part_start, part_end))
                    else:
                        text_parts.append(original_text)
                        text_parts_translation.append(translated_text)
                        time_ranges.append((start_time, end_time))
                else:
                    text_parts.append(original_text)
                    text_parts_translation.append(translated_text)
                    time_ranges.append((start_time, end_time))
            
            # 创建最终的翻译内容
            for i in range(len(text_parts)):
                if text_parts[i] and text_parts_translation[i]:
                    start_time, end_time = time_ranges[i]
                    time_str = f"时间戳 {self._format_timestamp(start_time)} - {self._format_timestamp(end_time)}"
                    
                    translation_section += f"{time_str}\n\n"
                    translation_section += f"原文: {text_parts[i]}\n\n"
                    translation_section += f"译文: {text_parts_translation[i]}\n\n"
                    translation_section += "---\n\n"  # 分隔线
        else:
            # 如果没有分段数据，尝试从完整文本创建一些简单分段
            original_text = transcript.get('text', '')
            translated_text = translation.get('text', '')
            
            if original_text and translated_text:
                # 简单按句子或段落分割
                import re
                
                # 按句号、问号、感叹号等分割
                pattern = r'(?<=[.!?。！？])\s+'
                original_sentences = re.split(pattern, original_text)
                translated_sentences = re.split(pattern, translated_text)
                
                # 如果分割后长度不一致，简单按段落分割
                if len(original_sentences) != len(translated_sentences):
                    original_sentences = original_text.split('\n\n')
                    translated_sentences = translated_text.split('\n\n')
                
                # 取较短的列表长度
                min_len = min(len(original_sentences), len(translated_sentences))
                
                # 估算每个段落的时间（假设整个文本均匀分布在视频时长上）
                total_duration = transcript.get('duration', 600)  # 默认10分钟
                
                # 每个块的大小（句子数量），确保有大约10-15个分段
                chunk_size = max(1, min_len // 10)
                
                for i in range(0, min_len, chunk_size):
                    # 确定当前块的结束索引
                    end_idx = min(i + chunk_size, min_len)
                    
                    # 计算估计的时间戳
                    segment_duration = total_duration / min_len if min_len > 0 else 60
                    start_time = i * segment_duration
                    end_time = end_idx * segment_duration
                    time_str = f"时间戳 {self._format_timestamp(start_time)} - {self._format_timestamp(end_time)}"
                    
                    # 合并这个块中的句子
                    original_block = " ".join(original_sentences[i:end_idx])
                    translated_block = " ".join(translated_sentences[i:end_idx])
                    
                    # 分割太长的块
                    if len(original_block) > 200:
                        orig_parts = []
                        for j in range(i, end_idx):
                            if j < len(original_sentences):
                                orig_parts.append(original_sentences[j])
                        
                        trans_parts = []
                        for j in range(i, end_idx):
                            if j < len(translated_sentences):
                                trans_parts.append(translated_sentences[j])
                        
                        # 为每个句子创建一个条目
                        for j in range(len(orig_parts)):
                            part_start = start_time + j * (segment_duration / len(orig_parts))
                            part_end = start_time + (j + 1) * (segment_duration / len(orig_parts)) if j < len(orig_parts) - 1 else end_time
                            part_time_str = f"时间戳 {self._format_timestamp(part_start)} - {self._format_timestamp(part_end)}"
                            
                            if j < len(trans_parts) and orig_parts[j] and trans_parts[j]:
                                translation_section += f"{part_time_str}\n\n"
                                translation_section += f"原文: {orig_parts[j]}\n\n"
                                translation_section += f"译文: {trans_parts[j]}\n\n"
                                translation_section += "---\n\n"  # 分隔线
                    else:
                        if original_block and translated_block:
                            translation_section += f"{time_str}\n\n"
                            translation_section += f"原文: {original_block}\n\n"
                            translation_section += f"译文: {translated_block}\n\n"
                            translation_section += "---\n\n"  # 分隔线
            else:
                # 如果没有有效的文本，显示一个提示信息
                translation_section += "无法获取完整的翻译分段对照。\n\n"
        
        return translation_section
    
    def _format_processing_logs(self, logs: List[str]) -> str:
        """格式化处理日志部分"""
        if not logs:
            return "处理过程中未记录特殊情况。"
        
        return "\n".join([f"- {log}" for log in logs])
    
    def _identify_chapters(self, transcript: Dict[str, Any], translation: Dict[str, Any]) -> List[Dict[str, Any]]:
        """识别内容中的章节结构"""
        # 实现简单的章节识别逻辑
        segments = transcript.get('segments', [])
        if not segments:
            return []
        
        # 计算视频总时长
        total_duration = transcript.get('duration', 0)
        if not total_duration and segments:
            try:
                total_duration = segments[-1].get('end', 0)
            except:
                total_duration = 0
        
        # 如果不能识别出明确的章节，则按时间均匀划分
        if total_duration > 0:
            # 将视频分为几个时间段
            chapter_count = min(7, max(3, len(segments) // 8))  # 根据段落数量确定章节数，至少3个，最多7个
            chapter_duration = total_duration / chapter_count
        
        chapters = []
        for i in range(chapter_count):
            start_time = i * chapter_duration
            end_time = (i + 1) * chapter_duration if i < chapter_count - 1 else total_duration
            
            # 查找该时间段内的文本
            chapter_segments = [s for s in segments if s.get('start', 0) >= start_time and s.get('start', 0) < end_time]
            
            # 生成章节标题（简单取该时间段内第一个段落的前20个字符）
            title = "内容片段"
            if chapter_segments:
                text = chapter_segments[0].get('text', '')
                title = text[:20] + "..." if len(text) > 20 else text
            
            # 格式化时间戳
            start_time_str = self._format_timestamp(start_time)
            end_time_str = self._format_timestamp(end_time)
            
            chapters.append({
                'title': title,
                'start': start_time,
                'end': end_time,
                'start_str': start_time_str,
                'end_str': end_time_str,
            })
        
        return chapters
    
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
    
    def _extract_terminology(self, source_text: str, target_text: str) -> Dict[str, str]:
        """从文本中提取可能的专业术语及解释"""
        # 这是一个基本实现，实际应用中可以替换为更复杂的逻辑
        # 比如使用NLP工具识别专有名词，或者查询预定义的术语库
        
        # 示例：从文本中查找大写词汇作为术语
        terms = {}
        
        # 尝试查找可能的技术词汇
        if source_text:
            # 简单示例：查找大写单词或特定模式的文本
            import re
            
            # 查找可能的技术术语（简化逻辑，仅作演示）
            # 查找全大写词汇（可能是缩写）
            uppercase_pattern = r'\b[A-Z]{2,}\b'
            uppercase_matches = re.findall(uppercase_pattern, source_text)
            
            # 查找首字母大写的词组（可能是专有名词）
            camelcase_pattern = r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b'
            camelcase_matches = re.findall(camelcase_pattern, source_text)
            
            # 合并并去重
            all_terms = set(uppercase_matches + camelcase_matches)
            
            # 为找到的术语提供简单解释（示例）
            for term in all_terms:
                # 过滤一些常见的非术语大写词
                if term in ['I', 'A', 'THE', 'AND', 'OR', 'BUT', 'SO']:
                    continue
                    
                # 生成一个简单解释（实际应用中应该使用术语库或AI生成）
                explanation = f"视频中提及的术语，可能与主题相关。"
                terms[term] = explanation
                
                # 限制术语表大小，避免过多
                if len(terms) >= 5:
                    break
        
        return terms
    
    def _format_related_resources(self, video_info: Dict[str, Any]) -> str:
        """格式化相关资源部分"""
        # 提取频道/上传者信息
        uploader = video_info.get('uploader', '')
        channel = video_info.get('channel', '')
        creator = uploader or channel or '未知发布者'
        
        # 提取视频ID和标题
        video_id = video_info.get('id', '')
        title = video_info.get('title', '')
        
        # 构建YouTube频道链接
        channel_id = video_info.get('channel_id', '')
        channel_url = f"https://www.youtube.com/channel/{channel_id}" if channel_id else ''
        
        # 提取视频描述中可能包含的链接
        description = video_info.get('description', '')
        import re
        url_pattern = r'https?://[^\s]+'
        urls = re.findall(url_pattern, description)
        
        # 构建相关资源部分
        resources = "## 相关资源\n\n"
        
        # 添加官方链接
        resources += "### 官方链接\n"
        if channel_url:
            resources += f"- [创作者频道: {creator}]({channel_url})\n"
        if video_id:
            resources += f"- [原始视频: {title}](https://www.youtube.com/watch?v={video_id})\n"
        
        # 添加相关资源链接
        if urls:
            resources += "\n### 视频描述中提及的链接\n"
            for i, url in enumerate(urls[:5]):  # 限制最多显示5个链接
                resources += f"- [链接 {i+1}]({url})\n"
        
        # 添加主题相关资源（可以针对视频主题进行定制）
        # 通过视频标题或内容关键词确定主题
        if title:
            resources += "\n### 可能的相关主题\n"
            keywords = title.lower().split()
            
            # 根据关键词推荐相关资源
            if any(kw in keywords for kw in ['ray', 'python', 'coding', 'programming']):
                resources += "- [Ray 官方文档](https://docs.ray.io)\n"
                resources += "- [Ray GitHub 仓库](https://github.com/ray-project/ray)\n"
                resources += "- [Python 官方网站](https://www.python.org)\n"
            elif any(kw in keywords for kw in ['ai', 'ml', 'machine', 'learning']):
                resources += "- [Machine Learning Research Papers](https://paperswithcode.com)\n"
                resources += "- [AI & ML Courses on Coursera](https://www.coursera.org/browse/data-science/machine-learning)\n"
            else:
                resources += "> 根据视频内容搜索更多相关资源\n"
        
        return resources
    
    def _format_key_points(self, translation: Dict[str, Any], summary: Dict[str, Any]) -> str:
        """格式化关键观点部分"""
        # 初始化关键观点部分
        key_points = "## 关键观点\n\n"
        
        # 尝试从summary中提取关键点
        if summary and summary.get('key_points'):
            points = summary.get('key_points', [])
            for i, point in enumerate(points):
                key_points += f"{i+1}. {point}\n"
        else:
            # 如果没有预定义的关键点，从翻译文本中提取
            text = translation.get('text', '')
            if text:
                # 简单实现：按句子分割，选择一些看起来像关键点的句子
                import re
                sentences = re.split(r'(?<=[.!?。！？])\s+', text)
                
                # 选择一些关键句子（简化实现）
                key_sentences = []
                
                # 选择策略：1.句子长度适中 2.包含关键词 3.位置（通常开头和结尾的句子很重要）
                keywords = ['重要', '关键', '核心', '主要', '总结', '结论', '最后']
                
                # 添加开头的句子
                if sentences and len(sentences) > 0:
                    first_sentence = sentences[0].strip()
                    if len(first_sentence) > 10:
                        key_sentences.append(first_sentence)
                
                # 添加包含关键词的句子
                for sentence in sentences:
                    sentence = sentence.strip()
                    if len(sentence) > 15 and len(sentence) < 100:
                        if any(kw in sentence for kw in keywords) and sentence not in key_sentences:
                            key_sentences.append(sentence)
                            if len(key_sentences) >= 3:  # 限制数量
                                break
                
                # 添加结尾的句子
                if sentences and len(sentences) > 2 and len(key_sentences) < 4:
                    last_sentence = sentences[-1].strip()
                    if len(last_sentence) > 10 and last_sentence not in key_sentences:
                        key_sentences.append(last_sentence)
                
                # 如果找到了关键句子，添加到关键观点
                if key_sentences:
                    for i, sentence in enumerate(key_sentences):
                        key_points += f"{i+1}. {sentence}\n"
                else:
                    key_points += "> 未能自动提取关键观点，建议根据内容手动添加\n"
            else:
                key_points += "> 未能提取关键观点，因为译文内容为空\n"
        
        return key_points 