# -*- coding: utf-8 -*-

"""
音频转写模块
负责将音频文件转写为文本
"""

import os
import json
import tempfile
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Union, Optional, List, Dict, Any
from datetime import datetime

from src.config.config_manager import get_config
from src.utils.log import get_logger
from src.utils.file_utils import ensure_dir, write_json_file
from src.models.models import Models
from src.utils.audio_utils import get_audio_duration

# 获取日志器
logger = get_logger()


@dataclass
class TimeSegment:
    """时间片段"""
    start: float  # 开始时间（秒）
    end: float    # 结束时间（秒）
    text: str     # 文本内容
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'start': self.start,
            'end': self.end,
            'text': self.text
        }


@dataclass
class TranscriptionResult:
    """转写结果"""
    text: str                 # 完整文本
    segments: List[TimeSegment]  # 时间片段列表
    language: Optional[str] = None  # 识别的语言
    source_path: Optional[str] = None  # 源文件路径
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'text': self.text,
            'segments': [
                {
                    'start': segment.start,
                    'end': segment.end,
                    'text': segment.text
                }
                for segment in self.segments
            ],
            'language': self.language,
            'source_path': self.source_path
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TranscriptionResult':
        """从字典创建对象"""
        segments = [
            TimeSegment(
                start=segment['start'],
                end=segment['end'],
                text=segment['text']
            )
            for segment in data.get('segments', [])
        ]
        
        return cls(
            text=data.get('text', ''),
            segments=segments,
            language=data.get('language'),
            source_path=data.get('source_path')
        )


class AudioTranscriber:
    """音频转写器"""
    
    def __init__(self, model_name: Optional[str] = None, output_dir: Optional[str] = None):
        """
        初始化转写器
        
        Args:
            model_name: 转写模型名称，默认从配置获取
            output_dir: 输出目录，默认从配置获取
        """
        config = get_config()
        self.config = config
        
        # 转写模型
        self.model_name = model_name or config.get('defaults', {}).get('transcription')
        
        # 输出目录
        if output_dir is None:
            output_dir = config.get('storage', {}).get('transcripts_dir', './transcripts')
        
        self.output_dir = ensure_dir(output_dir)
        
        logger.info(f"转写器初始化，使用模型: {self.model_name}, 输出目录: {self.output_dir}")
    
    def transcribe(self, audio_path, save_result=True):
        """
        转录音频文件
        
        参数:
            audio_path: 音频文件路径
            save_result: 是否保存结果到文件
            
        返回:
            TranscriptionResult对象
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"音频文件不存在: {audio_path}")
        
        # 检查音频时长（仅用于日志记录）
        audio_duration = get_audio_duration(audio_path)
        logger.info(f"音频时长: {audio_duration} 秒")
        
        # 无论音频长短，都使用文件转录API
        logger.info(f"使用文件转录API，模型：{self.model_name}")
        
        # 准备音频格式
        audio_path_str = str(Path(audio_path).resolve())
        logger.info(f"准备转录音频文件: {audio_path_str}")
        
        # 调用Models.transcribe_file方法
        try:
            result_dict = Models.transcribe_file(audio_path_str, model_name=self.model_name)
            
            # 解析结果
            result = self._parse_transcription_result(result_dict)
            
            # 保存结果到文件
            if save_result:
                self._save_transcription_result(audio_path, result)
            
            return result
            
        except Exception as e:
            logger.error(f"转录失败: {e}")
            raise
    
    def _prepare_audio_for_paraformer(self, audio_path: str) -> str:
        """
        准备适合Paraformer-v2的音频（转换为16kHz单声道WAV）
        
        Args:
            audio_path: 原始音频路径
            
        Returns:
            处理后的音频路径（如果无需转换则返回原路径）
        """
        # 检查文件格式和采样率
        if self._is_optimal_audio_format(audio_path):
            logger.info(f"音频已是最佳格式，无需转换: {audio_path}")
            return audio_path
            
        # 需要转换，创建临时目录
        temp_dir = ensure_dir(os.path.join(self.config.get('storage', {}).get('temp_dir', './temp'), 'converted_audio'))
        output_filename = f"{os.path.splitext(os.path.basename(audio_path))[0]}_16k.wav"
        output_path = os.path.join(temp_dir, output_filename)
        
        # 如果转换后的文件已存在，直接返回
        if os.path.exists(output_path):
            logger.info(f"已转换的音频文件已存在: {output_path}")
            return output_path
        
        try:
            logger.info(f"转换音频为16kHz单声道WAV: {audio_path} -> {output_path}")
            
            # 使用FFmpeg转换音频
            cmd = [
                'ffmpeg', '-y', '-i', audio_path,
                '-ar', '16000',  # 采样率16kHz
                '-ac', '1',      # 单声道
                '-c:a', 'pcm_s16le',  # 16位PCM
                output_path
            ]
            
            process = subprocess.run(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            
            if process.returncode != 0:
                logger.error(f"音频转换失败: {process.stderr}")
                return audio_path  # 转换失败，返回原始路径
                
            logger.info(f"音频已成功转换: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"音频转换异常: {e}")
            return audio_path  # 发生异常，返回原始路径
    
    def _is_optimal_audio_format(self, audio_path: str) -> bool:
        """
        检查音频是否已经是最佳格式（16kHz单声道WAV）
        
        Args:
            audio_path: 音频路径
            
        Returns:
            是否为最佳格式
        """
        try:
            # 使用ffprobe检查音频格式
            cmd = [
                'ffprobe', '-v', 'quiet', '-print_format', 'json',
                '-show_format', '-show_streams', audio_path
            ]
            
            process = subprocess.run(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            
            if process.returncode != 0:
                logger.error(f"检查音频格式失败: {process.stderr}")
                return False
                
            # 解析输出
            info = json.loads(process.stdout)
            streams = info.get('streams', [])
            
            for stream in streams:
                if stream.get('codec_type') == 'audio':
                    # 检查采样率和声道数
                    sample_rate = stream.get('sample_rate')
                    channels = stream.get('channels')
                    codec_name = stream.get('codec_name')
                    
                    logger.info(f"检测到音频格式: {codec_name}, 采样率: {sample_rate}Hz, 声道数: {channels}")
                    
                    # 判断是否为最佳格式: 16kHz单声道PCM
                    if sample_rate == '16000' and channels == 1 and codec_name in ['pcm_s16le', 'pcm_s24le', 'pcm_f32le']:
                        return True
                        
            return False
            
        except Exception as e:
            logger.error(f"检查音频格式异常: {e}")
            return False
    
    def _save_transcription_result(self, audio_path, result):
        """
        保存转录结果到文件
        
        参数:
            audio_path: 音频文件路径
            result: 转录结果
        """
        # 计算输出文件路径
        audio_filename = os.path.basename(str(audio_path))
        base_name = os.path.splitext(audio_filename)[0]
        transcript_path = os.path.join(self.output_dir, f"{base_name}.json")
        
        # 保存为JSON格式
        try:
            # 确保输出目录存在
            os.makedirs(os.path.dirname(transcript_path), exist_ok=True)
            
            # 将结果保存为JSON
            with open(transcript_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'text': result.text,
                    'segments': [s.to_dict() for s in result.segments],
                    'source_path': str(audio_path),  # 确保Path转换为字符串
                    'created_at': datetime.now().isoformat()
                }, f, ensure_ascii=False, indent=2)
                
            logger.info(f"转录结果已保存至: {transcript_path}")
        except Exception as e:
            logger.error(f"保存转录结果失败: {e}")
            raise
    
    def _load_transcript(self, path: str) -> TranscriptionResult:
        """
        从文件加载转写结果
        
        Args:
            path: 文件路径
            
        Returns:
            转写结果
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return TranscriptionResult.from_dict(data)
        except Exception as e:
            logger.error(f"加载转写结果失败 {path}: {e}")
            raise
    
    def to_srt(self, result: TranscriptionResult, output_path: Optional[str] = None) -> str:
        """
        将转写结果转换为SRT字幕格式
        
        Args:
            result: 转写结果
            output_path: 输出文件路径，如果为None则使用默认路径
            
        Returns:
            SRT文件路径
        """
        if not output_path:
            if result.source_path:
                base_name = os.path.splitext(os.path.basename(result.source_path))[0]
            else:
                base_name = "transcript"
            output_path = os.path.join(self.output_dir, f"{base_name}.srt")
        
        logger.info(f"生成SRT字幕: {output_path}")
        
        # 确保输出目录存在
        ensure_dir(os.path.dirname(output_path))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(result.segments, 1):
                # 转换时间格式 (秒 -> HH:MM:SS,mmm)
                start_time = self._format_time(segment.start)
                end_time = self._format_time(segment.end)
                
                f.write(f"{i}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"{segment.text}\n\n")
        
        logger.info(f"SRT字幕已生成: {output_path}")
        return output_path
    
    def _format_time(self, seconds: float) -> str:
        """
        将秒数格式化为SRT时间格式 (HH:MM:SS,mmm)
        
        Args:
            seconds: 秒数
            
        Returns:
            格式化的时间字符串
        """
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        seconds = seconds % 60
        milliseconds = int((seconds - int(seconds)) * 1000)
        return f"{hours:02d}:{minutes:02d}:{int(seconds):02d},{milliseconds:03d}"

    def _parse_transcription_result(self, result_dict):
        """
        解析转录结果
        
        参数:
            result_dict: 转录结果字典或TranscriptionResult对象
            
        返回:
            TranscriptionResult对象
        """
        # 如果已经是TranscriptionResult对象，直接返回
        if isinstance(result_dict, TranscriptionResult):
            return result_dict
        
        # 否则解析字典
        text = result_dict.get('text', '')
        segments = []
        
        # 解析片段
        for seg in result_dict.get('segments', []):
            segment = TimeSegment(
                start=seg.get('start', 0),
                end=seg.get('end', 0),
                text=seg.get('text', '')
            )
            segments.append(segment)
        
        # 创建结果对象
        return TranscriptionResult(
            text=text,
            segments=segments
        ) 