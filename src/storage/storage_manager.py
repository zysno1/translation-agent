# -*- coding: utf-8 -*-

"""
存储管理模块
负责管理转写、翻译结果的存储和导出
"""

import os
import json
import shutil
from pathlib import Path
from typing import Union, Optional, Dict, Any, List
from datetime import datetime

from src.config.config_manager import get_config
from src.utils.log import get_logger
from src.utils.file_utils import ensure_dir, write_text_file, safe_filename

# 获取日志器
logger = get_logger()


class StorageManager:
    """存储管理器"""
    
    def __init__(self, base_dir: Optional[str] = None):
        """
        初始化存储管理器
        
        Args:
            base_dir: 基础目录，默认从配置获取
        """
        config = get_config()
        self.config = config
        
        # 获取存储配置
        storage_config = config.get('storage', {})
        
        # 临时文件目录
        self.temp_dir = ensure_dir(storage_config.get('temp_dir', './temp'))
        self.audio_dir = ensure_dir(storage_config.get('audio_dir', os.path.join(self.temp_dir, 'audio')))
        self.video_dir = ensure_dir(storage_config.get('video_dir', os.path.join(self.temp_dir, 'video')))
        self.downloads_dir = ensure_dir(storage_config.get('downloads_dir', os.path.join(self.temp_dir, 'downloads')))
        
        # 数据目录
        self.data_dir = ensure_dir(storage_config.get('data_dir', './data'))
        self.transcripts_dir = ensure_dir(storage_config.get('transcripts_dir', os.path.join(self.data_dir, 'transcripts')))
        self.translations_dir = ensure_dir(storage_config.get('translations_dir', os.path.join(self.data_dir, 'translations')))
        self.summaries_dir = ensure_dir(storage_config.get('summaries_dir', os.path.join(self.data_dir, 'summaries')))
        
        # 报告目录
        self.reports_dir = ensure_dir(storage_config.get('reports_dir', './reports'))
        
        # 日志目录
        self.logs_dir = ensure_dir(config.get('logging', {}).get('log_dir', './logs'))
        
        logger.info(f"存储管理器初始化完成，临时目录: {self.temp_dir}, 数据目录: {self.data_dir}, 报告目录: {self.reports_dir}")

    def ensure_dirs(self):
        """确保所需目录存在"""
        # 临时文件目录
        ensure_dir(self.temp_dir)
        ensure_dir(self.audio_dir)
        ensure_dir(self.video_dir)
        ensure_dir(self.downloads_dir)
        
        # 数据目录
        ensure_dir(self.data_dir)
        ensure_dir(self.transcripts_dir)
        ensure_dir(self.translations_dir)
        ensure_dir(self.summaries_dir)
        
        # 报告目录
        ensure_dir(self.reports_dir)
        
        # 日志目录
        ensure_dir(self.logs_dir)
    
    def save_transcript(self, transcript, file_name: Optional[str] = None) -> str:
        """
        保存转写结果
        
        Args:
            transcript: 转写结果对象
            file_name: 文件名，默认使用源文件名或自动生成
            
        Returns:
            保存的文件路径
        """
        if hasattr(transcript, 'to_dict'):
            data = transcript.to_dict()
        else:
            data = transcript
            
        # 如果未指定文件名，从源文件元数据生成
        if file_name is None:
            # 获取作者信息
            author = self._extract_author_info(data)
            # 生成时间戳
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # 组合文件名
            file_name = f"transcript_{author}_{timestamp}"
        
        # 确保文件名安全且唯一
        file_name = safe_filename(file_name)
        file_path = os.path.join(self.transcripts_dir, f"{file_name}.json")
        
        # 写入JSON文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"转写结果已保存: {file_path}")
        return file_path
    
    def save_translation(self, translation, file_name: Optional[str] = None) -> str:
        """
        保存翻译结果
        
        Args:
            translation: 翻译结果对象
            file_name: 文件名，默认使用源文件名或自动生成
            
        Returns:
            保存的文件路径
        """
        if hasattr(translation, 'to_dict'):
            data = translation.to_dict()
        else:
            data = translation
            
        # 如果未指定文件名，从源文件元数据生成
        if file_name is None:
            # 获取作者信息
            author = self._extract_author_info(data)
            # 生成时间戳
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # 组合文件名
            file_name = f"translation_{author}_{timestamp}"
        
        # 确保文件名安全且唯一
        file_name = safe_filename(file_name)
        file_path = os.path.join(self.translations_dir, f"{file_name}.json")
        
        # 写入JSON文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"翻译结果已保存: {file_path}")
        return file_path
    
    def save_summary(self, summary, file_name: Optional[str] = None) -> str:
        """
        保存摘要结果
        
        Args:
            summary: 摘要结果对象
            file_name: 文件名，默认使用源文件名或自动生成
            
        Returns:
            保存的文件路径
        """
        if hasattr(summary, 'to_dict'):
            data = summary.to_dict()
        else:
            data = summary
            
        # 如果未指定文件名，从源文件元数据生成
        if file_name is None:
            # 获取作者信息
            author = self._extract_author_info(data)
            # 生成时间戳
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # 组合文件名
            file_name = f"summary_{author}_{timestamp}"
        
        # 确保文件名安全且唯一
        file_name = safe_filename(file_name)
        file_path = os.path.join(self.summaries_dir, f"{file_name}.json")
        
        # 写入JSON文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"摘要结果已保存: {file_path}")
        return file_path
    
    def save_results(self, video_title: str, video_url: str, transcript, translation=None, summary=None, formats=None) -> Dict[str, str]:
        """
        保存所有处理结果并导出为多种格式
        
        Args:
            video_title: 视频标题
            video_url: 视频URL
            transcript: 转写结果
            translation: 翻译结果（可选）
            summary: 摘要结果（可选）
            formats: 导出格式列表，默认为['md', 'srt', 'txt']
            
        Returns:
            包含各种输出文件路径的字典
        """
        logger.info(f"保存处理结果: {video_title}")
        
        # 默认导出格式
        if formats is None:
            formats = ['md', 'srt', 'txt']
        
        # 验证格式
        formats = [f for f in formats if f in ['md', 'srt', 'txt']]
        if not formats:
            formats = ['md']
        
        # 确保文件名安全
        safe_title = safe_filename(video_title)
        
        # 保存原始结果
        transcript_path = self.save_transcript(transcript, safe_title)
        
        result_paths = {
            'transcript': transcript_path,
            'translation': None,
            'summary': None
        }
        
        # 保存翻译结果（如果有）
        if translation:
            translation_path = self.save_translation(translation, safe_title)
            result_paths['translation'] = translation_path
        
        # 保存摘要结果（如果有）
        if summary:
            summary_path = self.save_summary(summary, safe_title)
            result_paths['summary'] = summary_path
        
        # 导出为各种格式
        for format in formats:
            output_path = self.export_result(
                transcript=transcript,
                translation=translation,
                format=format,
                summary=summary
            )
            result_paths[f'export_{format}'] = output_path
        
        logger.info(f"处理结果已保存: {', '.join(formats)} 格式")
        return result_paths
    
    def export_result(self, transcript, translation=None, format: str = 'md', summary=None) -> str:
        """
        导出处理结果为指定格式
        
        Args:
            transcript: 转写结果
            translation: 翻译结果（可选）
            format: 输出格式 (md, srt, txt)
            summary: 摘要结果（可选）
            
        Returns:
            导出文件路径
        """
        # 默认格式
        if format not in ['md', 'srt', 'txt']:
            format = 'md'
            logger.warning(f"不支持的格式: {format}，使用默认格式: md")
        
        # 生成文件名
        file_name = self._generate_output_filename(transcript, translation)
        
        # 确定输出路径
        output_dir = os.path.join(self.data_dir, format)
        ensure_dir(output_dir)
        output_path = os.path.join(output_dir, f"{file_name}.{format}")
        
        # 根据格式导出
        if format == 'md':
            output_path = self._export_markdown(transcript, translation, output_path, summary)
        elif format == 'srt':
            output_path = self._export_srt(transcript, translation, output_path)
        elif format == 'txt':
            output_path = self._export_plaintext(transcript, translation, output_path, summary)
        
        logger.info(f"结果已导出为 {format.upper()} 格式: {output_path}")
        return output_path
    
    def _generate_output_filename(self, transcript, translation=None) -> str:
        """
        生成输出文件名
        
        Args:
            transcript: 转写结果
            translation: 翻译结果（可选）
            
        Returns:
            文件名（不含扩展名）
        """
        # 从转写或翻译结果中提取信息
        source_path = None
        text_preview = None
        
        # 处理不同类型的输入
        if hasattr(transcript, 'to_dict'):
            data = transcript.to_dict()
            source_path = data.get('source_path')
            text_preview = data.get('text', '')[:20].strip()
        elif hasattr(transcript, 'source_path'):
            source_path = transcript.source_path
            text_preview = getattr(transcript, 'text', '')[:20].strip()
        elif isinstance(transcript, dict):
            source_path = transcript.get('source_path')
            text_preview = transcript.get('text', '')[:20].strip()
        else:
            text_preview = str(transcript)[:20].strip()
        
        # 从源文件路径生成文件名
        if source_path:
            base_name = os.path.basename(source_path)
            file_name = os.path.splitext(base_name)[0]
        else:
            # 从文本内容生成文件名
            file_name = safe_filename(text_preview, prefix="output") or f"output_{os.urandom(4).hex()}"
        
        # 确保文件名安全且唯一
        file_name = safe_filename(file_name, prefix="output")
        
        return file_name
    
    def _export_markdown(self, transcript, translation=None, output_path=None, summary=None) -> str:
        """
        导出为Markdown格式
        
        Args:
            transcript: 转写结果
            translation: 翻译结果（可选）
            output_path: 输出路径
            summary: 摘要结果（可选）
            
        Returns:
            导出文件路径
        """
        # 提取文本内容
        transcript_text = self._extract_text(transcript)
        translation_text = self._extract_text(translation) if translation else None
        summary_text = self._extract_text(summary) if summary else None
        
        # 生成Markdown内容
        md_content = "# 转写与翻译结果\n\n"
        
        # 添加摘要（如果有）
        if summary_text:
            md_content += "## 内容摘要\n\n"
            md_content += f"{summary_text}\n\n"
            md_content += "---\n\n"
        
        # 添加转写文本
        md_content += "## 原文转写\n\n"
        md_content += f"{transcript_text}\n\n"
        
        # 添加翻译文本（如果有）
        if translation_text:
            md_content += "## 翻译文本\n\n"
            md_content += f"{translation_text}\n\n"
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return output_path
    
    def _export_srt(self, transcript, translation=None, output_path=None) -> str:
        """
        导出为SRT字幕格式
        
        Args:
            transcript: 转写结果
            translation: 翻译结果（可选）
            output_path: 输出路径
            
        Returns:
            导出文件路径
        """
        # 这里简单实现，仅支持带时间戳的转写结果
        segments = []
        
        # 提取字幕片段
        if hasattr(transcript, 'segments'):
            segments = transcript.segments
        elif isinstance(transcript, dict) and 'segments' in transcript:
            from src.transcription.audio_transcriber import TimeSegment
            segments = [
                TimeSegment(
                    start=segment.get('start', 0),
                    end=segment.get('end', 0),
                    text=segment.get('text', '')
                )
                for segment in transcript['segments']
            ]
        
        # 如果没有片段，则使用简化模式
        if not segments:
            # 创建一个覆盖全部的片段
            from src.transcription.audio_transcriber import TimeSegment
            text = self._extract_text(transcript)
            segments = [TimeSegment(start=0, end=0, text=text)]
        
        # 生成SRT内容
        srt_content = ""
        for i, segment in enumerate(segments):
            # 使用翻译文本（如果有）
            if translation and i < len(segments):
                text = segment.text
                if hasattr(translation, 'segments') and i < len(translation.segments):
                    text = translation.segments[i].text
                elif isinstance(translation, dict) and 'text' in translation:
                    # 简化处理：如果没有分段的翻译，使用完整翻译
                    text = translation['text']
            else:
                text = segment.text
            
            # 格式化SRT条目
            srt_content += f"{i+1}\n"
            
            # 格式化时间
            start_time = self._format_srt_time(segment.start)
            end_time = self._format_srt_time(segment.end)
            srt_content += f"{start_time} --> {end_time}\n"
            
            # 添加文本
            srt_content += f"{text}\n\n"
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        
        return output_path
    
    def _export_plaintext(self, transcript, translation=None, output_path=None, summary=None) -> str:
        """
        导出为纯文本格式
        
        Args:
            transcript: 转写结果
            translation: 翻译结果（可选）
            output_path: 输出路径
            summary: 摘要结果（可选）
            
        Returns:
            导出文件路径
        """
        # 提取文本内容
        transcript_text = self._extract_text(transcript)
        translation_text = self._extract_text(translation) if translation else None
        summary_text = self._extract_text(summary) if summary else None
        
        # 生成文本内容
        content = ""
        
        # 添加摘要（如果有）
        if summary_text:
            content += "【内容摘要】\n\n"
            content += f"{summary_text}\n\n"
            content += "----------\n\n"
        
        # 添加转写文本
        content += "【原文转写】\n\n"
        content += f"{transcript_text}\n\n"
        
        # 添加翻译文本（如果有）
        if translation_text:
            content += "【翻译文本】\n\n"
            content += f"{translation_text}\n\n"
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return output_path
    
    def _extract_text(self, data) -> str:
        """
        从各种数据结构中提取文本
        
        Args:
            data: 数据对象或字典
            
        Returns:
            提取的文本
        """
        if data is None:
            return ""
        
        if isinstance(data, str):
            return data
        
        if hasattr(data, 'text'):
            return data.text
        
        if isinstance(data, dict) and 'text' in data:
            return data['text']
        
        # 尝试将对象转为字符串
        return str(data)
    
    @staticmethod
    def _format_srt_time(seconds: float) -> str:
        """
        格式化时间为SRT格式
        
        Args:
            seconds: 秒数
            
        Returns:
            SRT格式的时间字符串
        """
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        seconds = seconds % 60
        milliseconds = int((seconds - int(seconds)) * 1000)
        
        return f"{hours:02d}:{minutes:02d}:{int(seconds):02d},{milliseconds:03d}"
    
    def cleanup(self, keep_important: bool = True) -> None:
        """
        清理临时文件
        
        Args:
            keep_important: 是否保留重要文件（如转写和翻译结果）
        """
        # 清理临时目录
        if os.path.exists(self.temp_dir):
            # 如果不保留重要文件，则清空整个目录
            if not keep_important:
                shutil.rmtree(self.temp_dir)
                ensure_dir(self.temp_dir)
                logger.info(f"已清理临时目录: {self.temp_dir}")
            else:
                # 只清理临时视频文件，保留音频
                for file in os.listdir(self.temp_dir):
                    if file.endswith(('.mp4', '.webm', '.mkv', '.avi', '.mov')):
                        file_path = os.path.join(self.temp_dir, file)
                        os.remove(file_path)
                        logger.debug(f"已删除临时文件: {file_path}")
                
                logger.info(f"已清理临时视频文件，保留音频文件")

    def _extract_author_info(self, data: Dict[str, Any]) -> str:
        """
        从数据中提取作者信息
        
        Args:
            data: 数据字典
            
        Returns:
            作者名称，如果无法提取则返回默认值
        """
        # 尝试从元数据中提取作者信息
        author = None
        
        # 从视频元数据中提取
        if isinstance(data, dict):
            metadata = data.get('metadata', {})
            # 尝试不同的可能字段名
            for field in ['author', 'creator', 'uploader', 'channel', 'speaker']:
                if field in metadata and metadata[field]:
                    author = metadata[field]
                    break
            
            # 如果元数据中没有，尝试从视频信息中获取
            if not author and 'video_info' in data:
                video_info = data.get('video_info', {})
                for field in ['author', 'creator', 'uploader', 'channel', 'speaker']:
                    if field in video_info and video_info[field]:
                        author = video_info[field]
                        break
        
        # 如果无法提取，使用默认值
        if not author:
            # 尝试使用视频标题
            if isinstance(data, dict) and data.get('title'):
                title = data.get('title', '')
                # 使用标题的前10个字符作为替代
                author = safe_filename(title[:10])
            else:
                # 最后的退路：使用unknown
                author = "unknown"
        
        # 确保作者名称安全可用
        return safe_filename(author) 