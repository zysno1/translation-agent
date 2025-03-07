#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
音频处理工具类
提供音频分割、格式转换和信息提取功能
"""

import os
import subprocess
import json
import logging
import tempfile
from pathlib import Path
from typing import List, Union, Optional, Dict, Any

logger = logging.getLogger(__name__)

def get_audio_duration(audio_path: Union[str, Path]) -> float:
    """
    获取音频文件的时长（秒）
    
    Args:
        audio_path: 音频文件路径
        
    Returns:
        音频时长（秒）
    """
    try:
        # 确保路径为字符串
        audio_path_str = str(audio_path)
        
        # 使用ffprobe获取音频信息
        cmd = [
            'ffprobe', 
            '-v', 'quiet', 
            '-print_format', 'json', 
            '-show_format', 
            '-show_streams', 
            audio_path_str
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        info = json.loads(result.stdout)
        
        # 尝试从format中获取时长
        if 'format' in info and 'duration' in info['format']:
            return float(info['format']['duration'])
        
        # 尝试从第一个音频流中获取时长
        for stream in info.get('streams', []):
            if stream.get('codec_type') == 'audio' and 'duration' in stream:
                return float(stream['duration'])
        
        # 如果无法获取时长，记录警告并返回默认值
        logger.warning(f"无法获取音频时长: {audio_path}，使用默认值")
        return 0.0
        
    except Exception as e:
        logger.error(f"获取音频时长异常: {e}")
        # 出错时返回0
        return 0.0

def get_audio_info(audio_path: Union[str, Path]) -> Dict[str, Any]:
    """
    获取音频文件的详细信息
    
    Args:
        audio_path: 音频文件路径
        
    Returns:
        包含音频信息的字典
    """
    try:
        # 确保路径为字符串
        audio_path_str = str(audio_path)
        
        # 使用ffprobe获取音频信息
        cmd = [
            'ffprobe', 
            '-v', 'quiet', 
            '-print_format', 'json', 
            '-show_format', 
            '-show_streams', 
            audio_path_str
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        info = json.loads(result.stdout)
        
        # 提取关键信息
        audio_info = {
            'duration': 0,
            'format': '',
            'sample_rate': 0,
            'channels': 0,
            'bit_rate': 0
        }
        
        # 从format中提取信息
        if 'format' in info:
            format_info = info['format']
            audio_info['format'] = format_info.get('format_name', '')
            audio_info['duration'] = float(format_info.get('duration', 0))
            audio_info['bit_rate'] = int(format_info.get('bit_rate', 0))
        
        # 从第一个音频流中提取信息
        for stream in info.get('streams', []):
            if stream.get('codec_type') == 'audio':
                audio_info['sample_rate'] = int(stream.get('sample_rate', 0))
                audio_info['channels'] = int(stream.get('channels', 0))
                if 'duration' in stream and audio_info['duration'] == 0:
                    audio_info['duration'] = float(stream['duration'])
                break
        
        return audio_info
        
    except Exception as e:
        logger.error(f"获取音频信息异常: {e}")
        # 出错时返回空信息
        return {
            'duration': 0,
            'format': '',
            'sample_rate': 0,
            'channels': 0,
            'bit_rate': 0,
            'error': str(e)
        }

def segment_audio(audio_path: Union[str, Path], segment_length: int = 600) -> List[Path]:
    """
    将长音频文件切分为多个短片段
    
    Args:
        audio_path: 音频文件路径
        segment_length: 每个片段的长度（秒），默认10分钟
        
    Returns:
        切分后的音频文件路径列表
    """
    try:
        # 确保路径为字符串和Path对象
        audio_path_str = str(audio_path)
        audio_path_obj = Path(audio_path)
        
        # 获取音频时长
        duration = get_audio_duration(audio_path)
        if duration <= segment_length:
            logger.info(f"音频长度（{duration:.2f}秒）小于等于切片长度（{segment_length}秒），不需要切片")
            return [audio_path_obj]
        
        # 计算需要切分的片段数
        num_segments = int(duration / segment_length) + (1 if duration % segment_length > 0 else 0)
        logger.info(f"音频长度: {duration:.2f}秒，切分为{num_segments}个片段，每个{segment_length}秒")
        
        # 创建临时目录存放切分后的文件
        temp_dir = Path(tempfile.mkdtemp(prefix="audio_segments_"))
        logger.info(f"创建临时目录用于存放音频片段: {temp_dir}")
        
        # 切分音频
        segment_paths = []
        for i in range(num_segments):
            start_time = i * segment_length
            segment_file = temp_dir / f"{audio_path_obj.stem}_segment_{i+1}.wav"
            segment_file_str = str(segment_file)
            
            # 使用ffmpeg切分音频
            cmd = [
                'ffmpeg',
                '-i', audio_path_str,
                '-ss', str(start_time),
                '-t', str(segment_length),
                '-ar', '16000',  # 采样率设为16kHz
                '-ac', '1',      # 单声道
                '-vn',           # 不处理视频
                '-y',            # 覆盖已有文件
                segment_file_str
            ]
            
            logger.info(f"切分第{i+1}/{num_segments}个片段: {start_time}秒 - {start_time+segment_length}秒")
            subprocess.run(cmd, capture_output=True, check=True)
            segment_paths.append(segment_file)
        
        return segment_paths
    except Exception as e:
        logger.error(f"音频切片失败: {e}")
        raise

def convert_to_optimal_format(audio_path: Union[str, Path], 
                             sample_rate: int = 16000, 
                             channels: int = 1) -> Path:
    """
    将音频转换为最优的处理格式（16kHz单声道WAV）
    
    Args:
        audio_path: 音频文件路径
        sample_rate: 目标采样率，默认16kHz
        channels: 目标声道数，默认单声道
        
    Returns:
        转换后的音频文件路径
    """
    try:
        # 确保路径为字符串和Path对象
        audio_path_str = str(audio_path)
        audio_path_obj = Path(audio_path)
        
        # 检查是否需要转换
        audio_info = get_audio_info(audio_path)
        current_sample_rate = audio_info.get('sample_rate', 0)
        current_channels = audio_info.get('channels', 0)
        
        if current_sample_rate == sample_rate and current_channels == channels:
            logger.info(f"音频已经是最优格式 ({sample_rate}Hz, {channels}声道)，不需要转换")
            return audio_path_obj
            
        # 创建输出文件路径
        output_path = audio_path_obj.parent / f"{audio_path_obj.stem}_optimal.wav"
        output_path_str = str(output_path)
        
        # 使用ffmpeg转换音频
        cmd = [
            'ffmpeg',
            '-i', audio_path_str,
            '-ar', str(sample_rate),  # 采样率
            '-ac', str(channels),     # 声道数
            '-vn',                   # 不处理视频
            '-y',                    # 覆盖已有文件
            output_path_str
        ]
        
        logger.info(f"转换音频格式: {audio_path} -> {output_path} ({sample_rate}Hz, {channels}声道)")
        subprocess.run(cmd, capture_output=True, check=True)
        
        return output_path
    except Exception as e:
        logger.error(f"音频格式转换失败: {e}")
        raise

def extract_audio_from_video(video_path: Union[str, Path], 
                            output_format: str = 'wav',
                            sample_rate: int = 16000,
                            channels: int = 1) -> Path:
    """
    从视频文件中提取音频
    
    Args:
        video_path: 视频文件路径
        output_format: 输出音频格式，默认wav
        sample_rate: 采样率，默认16kHz
        channels: 声道数，默认单声道
        
    Returns:
        提取的音频文件路径
    """
    try:
        # 确保路径为字符串和Path对象
        video_path_str = str(video_path)
        video_path_obj = Path(video_path)
        
        # 创建输出文件路径
        output_dir = video_path_obj.parent / "extracted_audio"
        os.makedirs(output_dir, exist_ok=True)
        
        output_path = output_dir / f"{video_path_obj.stem}_audio.{output_format}"
        output_path_str = str(output_path)
        
        # 使用ffmpeg提取音频
        cmd = [
            'ffmpeg',
            '-i', video_path_str,
            '-ar', str(sample_rate),  # 采样率
            '-ac', str(channels),     # 声道数
            '-vn',                   # 不处理视频
            '-y',                    # 覆盖已有文件
            output_path_str
        ]
        
        logger.info(f"从视频提取音频: {video_path} -> {output_path}")
        subprocess.run(cmd, capture_output=True, check=True)
        
        return output_path
    except Exception as e:
        logger.error(f"从视频提取音频失败: {e}")
        raise 