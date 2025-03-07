# -*- coding: utf-8 -*-

"""
视频预处理模块
负责下载YouTube视频和提取音频
"""

import os
import tempfile
import yt_dlp
from pathlib import Path
from typing import Union, Optional, Dict, Any

from src.config.config_manager import get_config
from src.utils.log import get_logger
from src.utils.file_utils import ensure_dir, safe_filename

# 获取日志器
logger = get_logger()


class VideoPreprocessor:
    """视频预处理器"""
    
    def __init__(self, output_dir: Optional[str] = None):
        """
        初始化预处理器
        
        Args:
            output_dir: 输出目录，默认使用临时目录或配置中的目录
        """
        config = get_config()
        self.config = config
        
        # 如果未指定输出目录，使用配置中的目录或临时目录
        if output_dir is None:
            output_dir = config.get('storage', {}).get('temp_dir', './temp')
        
        self.output_dir = ensure_dir(output_dir)
        self.audio_dir = ensure_dir(os.path.join(output_dir, 'audio'))
        
        # 下载配置
        self.download_config = config.get('download', {})
        self.max_resolution = self.download_config.get('max_resolution', 1080)
        self.preferred_format = self.download_config.get('format', 'mp4')
        self.timeout = self.download_config.get('timeout', 300)
        self.retry_count = self.download_config.get('retry', 3)
        
        logger.info(f"预处理器初始化，输出目录: {self.output_dir}")
    
    def _create_optimized_audio(self, audio_path, sample_rate=16000):
        """
        创建用于转写的优化音频文件 (单声道, 16kHz采样率)
        
        Args:
            audio_path: 原始音频文件路径
            sample_rate: 目标采样率，默认16kHz
            
        Returns:
            优化后的音频文件路径
        """
        import subprocess
        
        audio_filename = os.path.basename(audio_path)
        audio_basename = os.path.splitext(audio_filename)[0]
        
        # 创建存储优化音频的目录
        converted_dir = os.path.join(self.output_dir, 'converted_audio')
        os.makedirs(converted_dir, exist_ok=True)
        
        # 设置优化后的音频文件路径 (WAV格式更适合处理)
        optimized_path = os.path.join(converted_dir, f"{audio_basename}_{sample_rate//1000}k.wav")
        
        # 检查优化音频文件是否已存在
        if os.path.exists(optimized_path):
            logger.info(f"优化音频文件已存在: {optimized_path}")
            return optimized_path
        
        # 使用FFmpeg转换音频为单声道、指定采样率
        try:
            logger.info(f"优化音频文件: {audio_path} -> {optimized_path}")
            subprocess.run(
                [
                    'ffmpeg', 
                    '-i', audio_path, 
                    '-ac', '1',  # 单声道
                    '-ar', str(sample_rate),  # 采样率
                    '-c:a', 'pcm_s16le',  # 16位PCM编码
                    optimized_path
                ],
                check=True, 
                capture_output=True
            )
            logger.info(f"音频优化成功: {optimized_path}")
            return optimized_path
        except subprocess.CalledProcessError as e:
            logger.error(f"音频优化失败: {e.stderr.decode()}")
            return audio_path  # 失败时返回原始音频路径
    
    def process(self, source: Union[str, Path]) -> Union[str, tuple]:
        """
        处理视频源（可以是URL或本地文件）
        
        Args:
            source: URL或文件路径
            
        Returns:
            如果是URL：返回(音频路径, 视频信息字典)
            如果是文件：返回音频路径
        """
        logger.info(f"处理视频源: {source}")
        
        # 检查是否是URL
        if isinstance(source, str) and (source.startswith("http") or source.startswith("www")):
            return self._process_url(source)
        else:
            # 处理本地文件
            return self._process_file(source)
            
    def _process_url(self, url: str) -> tuple:
        """
        处理YouTube URL
        
        Args:
            url: YouTube视频URL
            
        Returns:
            (音频路径, 视频信息字典)
        """
        logger.info(f"处理YouTube URL: {url}")
        
        # 从URL中提取视频信息
        video_info = self._get_video_info(url)
        
        # 构建输出文件名（使用视频标题）
        if "title" in video_info:
            safe_title = safe_filename(video_info["title"])
            video_id = video_info.get("id", "unknown")
            output_filename = f"{safe_title}_{video_id}"
        else:
            # 如果无法获取标题，使用URL的最后部分
            url_parts = url.split("/")
            video_id = url_parts[-1].split("=")[-1] if "=" in url_parts[-1] else url_parts[-1]
            output_filename = f"youtube_{video_id}"
        
        # 下载视频
        video_path = self._download_video(url, output_filename)
        
        # 提取音频
        audio_path = self._extract_audio(video_path, output_filename)
        
        # 优化音频（使其适合转写）
        optimized_audio_path = self._create_optimized_audio(audio_path)
        
        # 同时返回音频路径和视频信息
        return optimized_audio_path, video_info
    
    def _process_file(self, file_path: Union[str, Path]) -> str:
        """
        处理本地视频文件
        
        Args:
            file_path: 本地视频文件路径
            
        Returns:
            提取的音频文件路径
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"找不到文件: {file_path}")
        
        # 获取文件名（不含扩展名）
        filename = file_path.stem
        safe_name = safe_filename(filename)
        
        # 提取音频
        audio_path = self._extract_audio(str(file_path), safe_name)
        
        return audio_path
    
    def _get_video_info(self, url: str) -> Dict[str, Any]:
        """
        获取视频信息
        
        Args:
            url: 视频URL
            
        Returns:
            视频信息字典
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            logger.error(f"获取视频信息失败: {e}")
            raise
    
    def _download_video(self, url: str, output_filename: str) -> str:
        """
        下载视频
        
        Args:
            url: 视频URL
            output_filename: 输出文件名（不含扩展名）
            
        Returns:
            下载的视频文件路径
        """
        # 输出文件路径
        video_path = os.path.join(self.output_dir, f"{output_filename}.{self.preferred_format}")
        
        # 如果文件已存在，直接返回
        if os.path.exists(video_path):
            logger.info(f"视频文件已存在: {video_path}")
            return video_path
        
        # 下载配置
        ydl_opts = {
            'format': f'bestvideo[height<={self.max_resolution}]+bestaudio/best[height<={self.max_resolution}]',
            'outtmpl': os.path.join(self.output_dir, f"{output_filename}.%(ext)s"),
            'merge_output_format': self.preferred_format,
            'progress_hooks': [self._download_hook],
            'retries': self.retry_count,
            'socket_timeout': self.timeout,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            if os.path.exists(video_path):
                logger.info(f"视频下载完成: {video_path}")
                return video_path
            
            # 如果指定格式的文件不存在，寻找其他格式
            for ext in ['mp4', 'mkv', 'webm']:
                alt_path = os.path.join(self.output_dir, f"{output_filename}.{ext}")
                if os.path.exists(alt_path):
                    logger.info(f"视频下载完成(替代格式): {alt_path}")
                    return alt_path
                    
            raise FileNotFoundError(f"下载完成但找不到视频文件: {output_filename}")
            
        except Exception as e:
            logger.error(f"视频下载失败: {e}")
            raise
    
    def _extract_audio(self, video_path: str, output_filename: str) -> str:
        """
        从视频中提取音频
        
        Args:
            video_path: 视频文件路径
            output_filename: 输出文件名（不含扩展名）
            
        Returns:
            提取的音频文件路径
        """
        # 输出音频路径
        audio_path = os.path.join(self.audio_dir, f"{output_filename}.mp3")
        
        # 如果文件已存在，直接返回
        if os.path.exists(audio_path):
            logger.info(f"音频文件已存在: {audio_path}")
            return audio_path
        
        try:
            import ffmpeg
            
            # 使用ffmpeg-python提取音频
            (
                ffmpeg
                .input(video_path)
                .output(audio_path, acodec='libmp3lame', ab='128k', ac=2, ar='44100')
                .global_args('-y')  # 覆盖已存在的文件
                .global_args('-loglevel', 'error')  # 只显示错误
                .run(capture_stdout=True, capture_stderr=True)
            )
            
            logger.info(f"音频提取完成: {audio_path}")
            return audio_path
            
        except ImportError:
            logger.warning("ffmpeg-python未安装，尝试使用系统ffmpeg命令")
            return self._extract_audio_command(video_path, audio_path)
        except Exception as e:
            logger.error(f"音频提取失败: {e}")
            raise
    
    def _extract_audio_command(self, video_path: str, audio_path: str) -> str:
        """
        使用系统ffmpeg命令提取音频
        
        Args:
            video_path: 视频文件路径
            audio_path: 输出音频路径
            
        Returns:
            提取的音频文件路径
        """
        import subprocess
        from pathlib import Path
        import time
        
        # 确保输出目录存在
        ensure_dir(Path(audio_path).parent)
        
        # 简化输出文件名（避免路径问题）
        audio_filename = Path(audio_path).name
        audio_dir = Path(audio_path).parent
        simplified_audio_path = str(Path(audio_dir) / audio_filename)
        
        # 重试机制
        max_retries = 3
        retry_delay = 2  # 秒
        
        for attempt in range(max_retries):
            try:
                logger.info(f"尝试提取音频 (尝试 {attempt+1}/{max_retries}): {video_path} -> {simplified_audio_path}")
                
                # 增强的FFmpeg命令，提供更多选项和更好的兼容性
                cmd = [
                    'ffmpeg', '-y',  # 覆盖输出文件
                    '-i', video_path,  # 输入文件
                    '-vn',  # 不处理视频
                    '-acodec', 'libmp3lame',  # 使用mp3编码器
                    '-ab', '128k',  # 音频比特率
                    '-ar', '44100',  # 采样率
                    '-af', 'aformat=sample_fmts=s16:sample_rates=44100',  # 音频格式化
                    '-f', 'mp3',  # 强制输出格式
                    '-threads', '0',  # 使用所有可用线程
                    '-hide_banner',  # 隐藏横幅
                    '-loglevel', 'warning',  # 只显示警告和错误
                    simplified_audio_path  # 输出文件
                ]
                
                # 执行命令
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=300  # 5分钟超时
                )
                
                # 检查命令执行结果
                if result.returncode != 0:
                    error_msg = result.stderr.strip() or "未知错误"
                    logger.error(f"音频提取失败 (退出码 {result.returncode}): {error_msg}")
                    
                    # 如果不是最后一次尝试，则重试
                    if attempt < max_retries - 1:
                        logger.info(f"将在 {retry_delay} 秒后重试...")
                        time.sleep(retry_delay)
                        retry_delay *= 2  # 指数退避
                        continue
                    else:
                        raise RuntimeError(f"FFmpeg错误: {error_msg}")
                
                # 检查文件是否存在且大小大于0
                if os.path.exists(simplified_audio_path) and os.path.getsize(simplified_audio_path) > 0:
                    logger.info(f"音频提取成功: {simplified_audio_path}")
                    return simplified_audio_path
                else:
                    raise FileNotFoundError(f"FFmpeg执行成功但未生成有效文件: {simplified_audio_path}")
                    
            except subprocess.TimeoutExpired:
                logger.error(f"音频提取超时")
                if attempt < max_retries - 1:
                    logger.info(f"将在 {retry_delay} 秒后重试...")
                    time.sleep(retry_delay)
                    retry_delay *= 2
                else:
                    raise RuntimeError("音频提取多次超时，放弃处理")
                    
            except Exception as e:
                logger.error(f"音频提取过程中出错: {str(e)}")
                if attempt < max_retries - 1:
                    logger.info(f"将在 {retry_delay} 秒后重试...")
                    time.sleep(retry_delay)
                    retry_delay *= 2
                else:
                    raise RuntimeError(f"音频提取失败，错误信息: {str(e)}")
        
        # 如果执行到这里，说明所有重试都失败了
        raise RuntimeError("所有音频提取尝试均失败")
    
    def _download_hook(self, d):
        """
        下载进度回调
        
        Args:
            d: 进度信息字典
        """
        if d['status'] == 'downloading':
            if 'total_bytes' in d and d['total_bytes'] > 0:
                percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                logger.debug(f"下载进度: {percent:.1f}%")
            elif 'downloaded_bytes' in d:
                logger.debug(f"已下载: {d['downloaded_bytes'] / 1024 / 1024:.1f} MB")
        elif d['status'] == 'finished':
            logger.debug("下载完成，开始合并文件...")
        elif d['status'] == 'error':
            logger.error(f"下载错误: {d.get('error', 'unknown error')}") 