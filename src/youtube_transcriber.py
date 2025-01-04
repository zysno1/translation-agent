import os
import uuid
import time
import base64
import requests
import sys
from pydub import AudioSegment
from dotenv import load_dotenv
import yt_dlp
import json
import dashscope
from dashscope.audio.asr import Transcription
from dashscope import Generation
from http import HTTPStatus
import oss2
import random
import re
import subprocess
import glob
import argparse
import logging
from datetime import datetime
import traceback
from typing import Optional, Dict, List, Tuple
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor, as_completed
import textwrap
try:
    from terms import PROFESSIONAL_TERMS
except ImportError:
    from src.terms import PROFESSIONAL_TERMS

# 加载 .env 文件
load_dotenv()

def retry_on_timeout(max_retries=3, base_delay=1):
    """处理API调用超时的重试装饰器
    
    Args:
        max_retries: 最大重试次数
        base_delay: 基础延迟时间（秒）
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    last_exception = e
                    # 只对超时和网络错误进行重试
                    if "timeout" not in str(e).lower() and "network" not in str(e).lower():
                        raise
                    
                    delay = base_delay * (2 ** attempt)  # 指数退避
                    self.logger.warning(f"第 {attempt + 1} 次调用失败: {str(e)}")
                    self.logger.info(f"等待 {delay} 秒后重试...")
                    time.sleep(delay)
            
            raise last_exception
        return wrapper
    return decorator

def setup_logger(logs_dir: str) -> tuple:
    """设置日志记录器
    Args:
        logs_dir: 日志目录
    Returns:
        tuple: (logger, log_file_path)
    """
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    # 生成日志文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(logs_dir, f"log_{timestamp}.txt")
    
    # 创建日志记录器
    logger = logging.getLogger('youtube_transcriber')
    logger.setLevel(logging.DEBUG)
    
    # 创建文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # 创建控制台处理器（只显示INFO及以上级别）
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger, log_file

class ProcessStep:
    """处理步骤的定义"""
    def __init__(self, name: str, weight: int, description: str = ""):
        self.name = name
        self.weight = weight
        self.description = description
        self.start_time = None
        self.end_time = None
        self.sub_progress = 0.0

class ProgressTracker:
    """进度跟踪器"""
    # 定义处理步骤及其权重
    STEPS = [
        ProcessStep("提取音频", 15, "下载和提取音频"),
        ProcessStep("处理音频", 5, "音频格式转换"),
        ProcessStep("上传音频", 10, "上传到OSS"),
        ProcessStep("语音识别", 40, "转写音频内容"),  # 增加语音识别的权重
        ProcessStep("翻译文本", 20, "翻译为中文"),
        ProcessStep("优化文本", 5, "优化文本格式"),
        ProcessStep("保存结果", 5, "保存最终结果")
    ]
    
    def __init__(self, logger):
        self.logger = logger
        self.current_step = None
        self.completed_steps = []
        self.start_time = None
        self.step_start_time = None
        self.step_times = {}  # 记录每个步骤的实际耗时
        self.total_weight = sum(step.weight for step in self.STEPS)
        
    def start_step(self, step_name: str) -> None:
        """开始一个新步骤"""
        step = next((s for s in self.STEPS if s.name == step_name), None)
        if not step:
            raise ValueError(f"未知的步骤: {step_name}")
        
        if self.current_step:
            self.complete_step()
        
        step.start_time = time.time()
        if not self.start_time:
            self.start_time = step.start_time
        
        self.step_start_time = step.start_time
        self.current_step = step
        self.update_progress()
    
    def complete_step(self) -> None:
        """完成当前步骤"""
        if self.current_step:
            end_time = time.time()
            step_time = end_time - self.step_start_time
            self.step_times[self.current_step.name] = step_time
            self.completed_steps.append(self.current_step)
            self.current_step.end_time = end_time
            self.current_step = None
    
    def calculate_progress(self) -> tuple:
        """计算总进度和预计剩余时间
        Returns:
            tuple: (总进度, 预计剩余时间)
        """
        if not self.start_time:
            return 0.0, None
            
        completed_weight = sum(step.weight for step in self.completed_steps)
        current_weight = 0
        
        if self.current_step:
            current_weight = self.current_step.weight * self.current_step.sub_progress
            
        total_progress = (completed_weight + current_weight) / self.total_weight
        
        # 计算预计剩余时间
        if not self.completed_steps and (not self.current_step or self.current_step.sub_progress < 0.1):
            return total_progress, None  # 刚开始时不显示预计时间
            
        elapsed_time = time.time() - self.start_time
        
        if total_progress > 0:
            # 使用已完成步骤的实际耗时来优化预估
            remaining_weight = self.total_weight - completed_weight - current_weight
            if self.step_times:
                avg_time_per_weight = sum(self.step_times.values()) / sum(step.weight for step in self.completed_steps)
                remaining_time = remaining_weight * avg_time_per_weight
                # 为语音识别步骤添加额外时间
                if self.current_step and self.current_step.name == "语音识别" and self.current_step.sub_progress < 0.5:
                    remaining_time *= 1.5  # 语音识别通常需要更长时间
                return total_progress, remaining_time
                
        return total_progress, None
    
    def update_progress(self) -> None:
        """更新并显示进度信息"""
        total_progress, remaining_time = self.calculate_progress()
        
        # 格式化进度信息
        progress_msg = f"总进度: {total_progress*100:.1f}%"
        if self.current_step:
            progress_msg += f" ({self.current_step.name}"
            if self.current_step.sub_progress > 0:
                progress_msg += f": {self.current_step.sub_progress*100:.1f}%"
            progress_msg += ")"
        
        # 添加剩余时间信息
        if remaining_time is not None:
            if remaining_time < 60:
                time_str = f"{remaining_time:.0f}秒"
            elif remaining_time < 3600:
                time_str = f"{remaining_time/60:.0f}分钟"
            else:
                time_str = f"{remaining_time/3600:.1f}小时"
            progress_msg += f" - 预计剩余: {time_str}"
        else:
            progress_msg += " - 正在计算剩余时间..."
        
        self.logger.info(progress_msg)
    
    def get_state(self) -> Dict:
        """获取当前状态"""
        return {
            'current_step': self.current_step.name if self.current_step else None,
            'sub_progress': self.current_step.sub_progress if self.current_step else 0.0,
            'completed_steps': [step.name for step in self.completed_steps],
            'start_time': self.start_time
        }
    
    def load_state(self, state: Dict) -> None:
        """加载保存的状态"""
        if not state:
            return
        
        self.start_time = state.get('start_time')
        
        # 恢复已完成的步骤
        completed_names = state.get('completed_steps', [])
        self.completed_steps = [
            step for step in self.STEPS 
            if step.name in completed_names
        ]
        for step in self.completed_steps:
            step.sub_progress = 1.0
        
        # 恢复当前步骤
        current_step_name = state.get('current_step')
        if current_step_name:
            self.current_step = next(
                (step for step in self.STEPS if step.name == current_step_name),
                None
            )
            if self.current_step:
                self.current_step.sub_progress = state.get('sub_progress', 0.0)
                self.current_step.start_time = time.time()

class YouTubeTranscriber:
    """YouTube视频音频提取和语音识别工具"""

    # 定义目录结构
    DIRS = {
        'root': '.',  # 根目录
        'logs': 'logs',  # 日志目录
        'temp': 'temp',  # 临时文件目录
        'output': 'output',  # 输出目录
        'transcripts': 'transcripts'  # 转写文本目录
    }
    
    # 定义文件命名模板
    FILE_TEMPLATES = {
        'log': '{timestamp}_transcriber.log',  # 日志文件
        'audio': '{timestamp}_{video_id}.mp3',  # 音频文件
        'original': '{timestamp}_{video_id}_original.txt',  # 原始英文转写
        'translated': '{timestamp}_{video_id}_translated.txt',  # 翻译后的中文
        'final': '{timestamp}_{video_id}_final.txt'  # 最终优化后的文本
    }
    
    # 翻译的提示词
    TRANSLATE_SYSTEM_PROMPT = """你是一位专业的英译中翻译专家，专门从事人工智能、机器学习系统(MLSys)、大语言模型(LLM)和云原生领域的技术文档翻译。你需要：

1. 保持专业性：
- 准确理解并翻译专业术语
- 保持技术文档的严谨性
- 确保翻译后的内容对目标领域的技术人员友好

2. 翻译风格：
- 采用中性、专业的语气
- 保持句式流畅自然
- 避免过度口语化
- 适当保留关键的英文术语

3. 术语处理：
- 优先使用领域内约定俗成的中文译名
- 首次出现的专业术语可采用"中文(英文)"的形式
- 对于新兴概念，可保留原有英文表述
- 参考已提供的专业术语对照表

4. 特殊要求：
- 保留代码片段、变量名和函数名中的英文
- 保持文本的格式和结构
- 确保数字、单位和标点符号的正确性
- 注意上下文的连贯性

请基于以上要求，提供准确、专业、流畅的中文翻译。"""

    TRANSLATE_USER_PROMPT = """请将以下英文文本翻译成中文：

{text}

要求：
1. 保持专业性和准确性
2. 遵循术语表中的标准翻译
3. 适当保留关键英文术语
4. 确保翻译流畅自然"""

    # Token 价格（元/1K tokens）和语音识别价格（元/秒）
    PRICE_PER_SECOND = {
        'paraformer-v2': 0.00008,  # 语音识别价格（元/秒）
    }
    
    PRICE_PER_1K_TOKENS = {
        'qwen-plus': 0.1,  # 通义千问-Plus 模型价格
        'qwen-turbo': 0.008,  # 通义千问-Turbo 模型价格
        'qwen-max': 0.2  # 通义千问-Max 模型价格
    }

    def __init__(self):
        """初始化转写器"""
        # 重新加载环境变量，确保使用最新的配置
        load_dotenv(override=True)
        
        # 创建必要的目录结构
        for dir_name, dir_path in self.DIRS.items():
            os.makedirs(dir_path, exist_ok=True)
            
        # 设置默认配置
        self.config = {
            'audio': {
                'sample_rate': 16000,  # 采样率
                'channels': 1,  # 声道数
                'bit_depth': 16,  # 位深度
                'format': 'wav'  # 音频格式
            },
            'transcription': {
                'model': 'paraformer-v2',
                'language': 'en'
            }
        }
            
        # 设置日志记录器
        self.setup_logging()
        
        # 初始化其他配置...
        self.temp_files = []
        self.output_files = []
        
        # 初始化费用统计
        self.total_tokens = {
            'qwen-plus': 0,
            'qwen-turbo': 0,
            'paraformer-v2': 0
        }
        
        # 验证环境变量
        self.verify_env_variables()

    def get_file_path(self, file_type: str, **kwargs) -> str:
        """获取文件路径
        
        Args:
            file_type: 文件类型 ('log', 'audio', 'original', 'translated', 'final')
            **kwargs: 文件名需要的参数
            
        Returns:
            str: 完整的文件路径
        """
        # 添加统一格式的时间戳（年月日_时分秒）
        if 'timestamp' not in kwargs:
            kwargs['timestamp'] = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 获取文件名模板
        template = self.FILE_TEMPLATES.get(file_type)
        if not template:
            raise ValueError(f"未知的文件类型: {file_type}")
            
        # 生成文件名
        filename = template.format(**kwargs)
        
        # 确定目录
        if file_type == 'log':
            dir_path = self.DIRS['logs']
        elif file_type == 'audio':
            dir_path = self.DIRS['temp']
        else:
            dir_path = self.DIRS['transcripts']
            
        # 返回完整路径
        return os.path.join(dir_path, filename)
        
    def process_video(self, url: str) -> Dict:
        """处理YouTube视频
        
        Args:
            url: YouTube视频URL
            
        Returns:
            Dict: 处理结果
        """
        try:
            self.logger.info("开始新的视频处理任务...")
            self.logger.info(f"工作目录: {os.getcwd()}")
            
            # 提取视频ID
            video_id = extract_video_id(url)
            if not video_id:
                raise ValueError("无效的YouTube URL")
                
            # 获取视频标题和信息
            try:
                with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_title = info.get('title', video_id)
                    duration = info.get('duration', 0)
                    
                self.logger.info(f"视频信息获取成功:")
                self.logger.info(f"- 标题: {video_title}")
                self.logger.info(f"- ID: {video_id}")
                self.logger.info(f"- URL: {url}")
                self.logger.info(f"- 时长: {duration} 秒")
                
                # 预估处理时间
                time_estimates = self.estimate_processing_time(duration)
                self.logger.info("处理时间预估:")
                self.logger.info(f"- 视频下载: {self.format_time(time_estimates['download'])}")
                self.logger.info(f"- 音频处理: {self.format_time(time_estimates['audio_process'])}")
                self.logger.info(f"- 文件上传: {self.format_time(time_estimates['upload'])}")
                self.logger.info(f"- 语音识别: {self.format_time(time_estimates['recognition'])}")
                self.logger.info(f"- 文本翻译: {self.format_time(time_estimates['translation'])}")
                self.logger.info(f"- 预计总时间: {self.format_time(time_estimates['total'])}")
                
            except Exception as e:
                self.logger.error(f"获取视频信息失败: {str(e)}")
                video_title = video_id
                
            # 下载音频
            audio_path = self.get_file_path('audio', video_id=video_id)
            self.download_audio(url, audio_path)
            
            try:
                # 提取音频并转换格式
                self.logger.info("开始音频处理...")
                processed_audio_path = self.extract_audio(audio_path, video_id)
                if not processed_audio_path:
                    raise Exception("音频处理失败")
                
                # 上传音频到OSS
                file_url = self.upload_to_oss(processed_audio_path)
                self.logger.info("音频文件上传完成")
                
                # 语音识别
                self.logger.info("开始语音识别流程...")
                results = self.recognize_speech(processed_audio_path, file_url)
                if not results:
                    self.logger.error("语音识别失败，程序退出")
                    sys.exit(1)  # 语音识别失败时直接退出
                    
                # 提取文本
                self.logger.info("开始提取识别文本...")
                text_segments = self.extract_text_from_result(results)
                if not text_segments:
                    self.logger.error("文本提取失败，程序退出")
                    sys.exit(1)  # 文本提取失败时直接退出
                    
                # 记录文本统计信息
                total_words = sum(len(text.split()) for text, _, _ in text_segments)
                total_duration = sum(end - start for _, start, end in text_segments)
                self.logger.info(f"文本提取完成:")
                self.logger.info(f"- 总字数: {total_words}")
                self.logger.info(f"- 总时长: {self.format_time(total_duration)}")
                self.logger.info(f"- 段落数: {len(text_segments)}")
                
                # 生成安全的文件名
                safe_title = re.sub(r'[<>:"/\\|?*]', '_', video_title)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                original_filename = f"{timestamp}_{safe_title}_original.md"
                final_filename = f"{timestamp}_{safe_title}_final.md"
                
                # 保存原始文本
                original_path = os.path.join(self.DIRS['transcripts'], original_filename)
                self.logger.info(f"保存原始转写文本...")
                self.save_text(text_segments, original_path, video_id=video_id, video_url=url, video_title=video_title)
                
                # 构建原始文本用于翻译
                self.logger.info("准备文本翻译...")
                original_text = self.format_text_for_translation(text_segments)
                
                # 翻译文本
                self.logger.info("开始文本翻译流程...")
                translated_text = self.translate_text(original_text)
                if not translated_text or translated_text == original_text:
                    self.logger.error("文本翻译失败，程序退出")
                    sys.exit(1)  # 翻译失败时直接退出
                
                # 保存最终文本
                final_path = os.path.join(self.DIRS['transcripts'], final_filename)
                self.logger.info("保存最终翻译文本...")
                self.save_final_text(final_path, translated_text, video_id, url, video_title)
                
                # 提交到Git仓库
                try:
                    if os.path.exists('.git'):
                        self.logger.info("提交文件到Git仓库...")
                        
                        # 检查Git状态
                        status = subprocess.run(['git', 'status', '--porcelain'], 
                            check=True, capture_output=True, text=True)
                        
                        if status.stdout.strip():
                            # 添加文件到Git
                            self.logger.info("添加文件到暂存区...")
                            subprocess.run(['git', 'add', original_path, final_path], check=True)
                            
                            # 提交更改
                            commit_message = f"添加转录文稿: {video_title}\n\n- 原始文本: {original_filename}\n- 最终文本: {final_filename}"
                            self.logger.info("提交更改...")
                            result = subprocess.run(
                                ['git', 'commit', '-m', commit_message], 
                                check=True, 
                                capture_output=True, 
                                text=True
                            )
                            commit_hash = result.stdout.split()[1] if result.stdout else "unknown"
                            
                            # 推送到远程仓库
                            self.logger.info("推送到远程仓库...")
                            push_result = subprocess.run(
                                ['git', 'push', 'origin', 'master'],  # 使用 master 分支
                                check=True,
                                capture_output=True,
                                text=True
                            )
                            
                            self.logger.info(f"Git操作完成:")
                            self.logger.info(f"- Commit Hash: {commit_hash}")
                            self.logger.info(f"- 提交消息: {commit_message}")
                            self.logger.info("- 已成功推送到远程仓库")
                        else:
                            self.logger.info("没有需要提交的更改")
                        
                except subprocess.CalledProcessError as e:
                    self.logger.error(f"Git操作失败: {str(e)}")
                    self.logger.error(f"错误输出: {e.stderr if hasattr(e, 'stderr') else '无'}")
                except Exception as e:
                    self.logger.error(f"Git操作失败: {str(e)}")
                    self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
                
                self.logger.info("视频处理任务完成")
                return {
                    "success": True,
                    "video_id": video_id,
                    "video_title": video_title,
                    "original_path": original_path,
                    "final_path": final_path
                }
                
            finally:
                # 清理临时文件
                self.clean_resources(audio_path)
                self.logger.info("临时文件清理完成")
            
        except Exception as e:
            self.logger.error(f"处理视频时出错: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }

    def split_text_for_translation(self, text: str, max_chars: int = 2000) -> List[str]:
        """将文本分段用于翻译
        
        Args:
            text: 要分段的文本
            max_chars: 每段最大字符数
            
        Returns:
            List[str]: 分段后的文本列表
        """
        segments = []
        current_segment = []
        current_length = 0
        
        lines = text.split('\n')
        for line in lines:
            # 跳过空行
            if not line.strip():
                continue
                
            # 解析时间戳和文本
            match = re.match(r'(\[\d{2}:\d{2} - \d{2}:\d{2}\]) (.+)', line)
            if not match:
                continue
                
            timestamp, content = match.groups()
            line_length = len(content)
            
            # 如果当前行超过最大长度，需要单独处理
            if line_length > max_chars:
                # 先保存当前段落
                if current_segment:
                    segments.append('\n'.join(current_segment))
                    current_segment = []
                    current_length = 0
                
                # 将长行按句子分割
                sentences = re.split(r'([。！？.!?]+)', content)
                temp_segment = []
                temp_length = 0
                
                for i in range(0, len(sentences), 2):
                    sentence = sentences[i]
                    if i + 1 < len(sentences):
                        sentence += sentences[i + 1]  # 加回标点符号
                        
                    if temp_length + len(sentence) > max_chars and temp_segment:
                        # 保存当前临时段落
                        segments.append('\n'.join([timestamp + ' ' + ' '.join(temp_segment)]))
                        temp_segment = [sentence]
                        temp_length = len(sentence)
                    else:
                        temp_segment.append(sentence)
                        temp_length += len(sentence)
                
                # 保存最后的临时段落
                if temp_segment:
                    segments.append('\n'.join([timestamp + ' ' + ' '.join(temp_segment)]))
                    
            # 如果添加当前行会超过最大长度，先保存当前段落
            elif current_length + line_length > max_chars and current_segment:
                segments.append('\n'.join(current_segment))
                current_segment = [line]
                current_length = line_length
            else:
                current_segment.append(line)
                current_length += line_length
        
        # 保存最后一个段落
        if current_segment:
            segments.append('\n'.join(current_segment))
        
        return segments

    @retry_on_timeout(max_retries=3, base_delay=1)
    def translate_text(self, text: str) -> str:
        """翻译文本
        
        Args:
            text: 要翻译的文本
            
        Returns:
            str: 翻译后的文本
        """
        try:
            self.logger.info("开始翻译文本...")
            self.logger.debug(f"原文长度: {len(text)} 字符")
            
            # 估算token数量（粗略估计：每4个字符约1个token）
            estimated_tokens = len(text) // 4
            estimated_cost = (estimated_tokens / 1000) * self.PRICE_PER_1K_TOKENS['qwen-plus']
            
            self.logger.debug(f"预估token数: {estimated_tokens}")
            self.logger.debug(f"预估成本: ¥{estimated_cost:.4f}")
            
            # 构建系统提示词
            messages = [
                {"role": "system", "content": self.TRANSLATE_SYSTEM_PROMPT},
                {"role": "user", "content": self.TRANSLATE_USER_PROMPT.format(text=text)}
            ]
            
            # 调用翻译API
            response = self.api_call_with_retry(
                Generation.call,
                model='qwen-plus',
                messages=messages
            )
            
            if not response or not response.output or not response.output.text:
                raise Exception("翻译API返回无效响应")
                
            # 更新token统计
            if response.usage:
                total_tokens = response.usage.total_tokens
                self.total_tokens['qwen-plus'] = float(total_tokens)  # 更新token统计
                actual_cost = (total_tokens / 1000) * self.PRICE_PER_1K_TOKENS['qwen-plus']
                self.logger.debug(f"实际使用token数: {total_tokens}")
                self.logger.debug(f"实际成本: ¥{actual_cost:.4f}")
            
            translated_text = response.output.text.strip()
            self.logger.info("文本翻译完成")
            return translated_text
            
        except Exception as e:
            self.logger.error(f"翻译文本时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            return text  # 出错时返回原文
    
    def print_token_statistics(self) -> None:
        """打印令牌使用统计信息。"""
        self.logger.info("音频处理统计:")
        for model, tokens in self.total_tokens.items():
            self.logger.info(f"• {model}: {tokens} 秒")
            
    def cleanup_temp_files(self, video_id: str = None) -> None:
        """清理临时文件
        Args:
            video_id: 视频ID,如果提供则只清理该视频相关的文件
        """
        try:
            files_to_clean = []
            
            # 收集需要清理的文件
            for temp_file in self.temp_files:
                if video_id:
                    if video_id in temp_file:
                        files_to_clean.append(temp_file)
                else:
                    files_to_clean.append(temp_file)
                    
            # 清理文件
            for file_path in files_to_clean:
                try:
                    if os.path.exists(file_path):
                        file_size = os.path.getsize(file_path)
                        os.remove(file_path)
                        self.logger.debug(f"删除临时文件: {file_path} (大小: {file_size} 字节)")
                        self.temp_files.remove(file_path)
                except Exception as e:
                    self.logger.warning(f"删除失败: {file_path} ({str(e)})")
                    
        except Exception as e:
            self.handle_error(e, "清理临时文件")
    
    def handle_error(self, error: Exception, step: str, fatal: bool = False) -> None:
        """集中处理错误
        Args:
            error: 异常对象
            step: 发生错误的步骤
            fatal: 是否为致命错误
        """
        error_msg = f"{step}时发生错误: {str(error)}"
        self.logger.error(error_msg)
        
        # 记录详细的错误信息
        self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
        
        if fatal:
            sys.exit(1)
        else:
            self.logger.warning("尝试继续执行后续步骤")
            
    def api_call_with_retry(self, func, *args, max_retries: int = 3, **kwargs):
        """执行API调用,失败时自动重试"""
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                self.logger.warning(f"第 {attempt + 1} 次调用失败: {str(e)}")
                time.sleep(2 ** attempt)
    
    def check_cost_warning(self):
        """检查费用是否超过预警阈值"""
        try:
            total_cost = 0
            
            # 计算各项费用
            qwen_plus_tokens = self.total_tokens.get('qwen-plus', 0)
            qwen_plus_cost = (qwen_plus_tokens / 1000) * self.PRICE_PER_1K_TOKENS['qwen-plus']
            
            qwen_turbo_tokens = self.total_tokens.get('qwen-turbo', 0)
            qwen_turbo_cost = (qwen_turbo_tokens / 1000) * self.PRICE_PER_1K_TOKENS['qwen-turbo']
            
            # 语音识别成本计算（基于时长）
            audio_duration = float(self.total_tokens.get('paraformer-v2', 0))  # 确保转换为浮点数
            audio_cost = audio_duration * self.PRICE_PER_SECOND['paraformer-v2']
            
            total_cost = qwen_plus_cost + qwen_turbo_cost + audio_cost
            
            if total_cost >= self.cost_warning_threshold:
                self.logger.warning(f"费用预警: 当前总费用 ¥{total_cost:.4f} 已超过预警阈值 ¥{self.cost_warning_threshold:.2f}")
                self.logger.warning(f"• 通义千问-Plus: ¥{qwen_plus_cost:.4f}")
                self.logger.warning(f"• 通义千问-Turbo: ¥{qwen_turbo_cost:.4f}")
                self.logger.warning(f"• 语音识别 (Paraformer-v2): ¥{audio_cost:.4f} ({audio_duration:.2f}秒)")
        except Exception as e:
            self.logger.error(f"计算成本时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
    
    def extract_text_from_result(self, result: Dict) -> List[Tuple[str, float, float]]:
        """从转写结果中提取文本和时间戳。
        
        Args:
            result (Dict): 转写结果 JSON
            
        Returns:
            List[Tuple[str, float, float]]: 包含 (text, start_time, end_time) 元组的列表
        """
        segments = []
        try:
            # 记录原始结果用于调试
            self.logger.debug(f"提取文本的原始数据: {json.dumps(result, ensure_ascii=False, indent=2)}")
            
            # 检查结果格式
            if not isinstance(result, dict):
                raise Exception("结果格式错误：不是一个字典")
                
            # 获取转写内容的 URL
            if 'results' not in result:
                raise Exception("结果格式错误：缺少 results 字段")
                
            for item in result['results']:
                if 'transcription_url' not in item:
                    self.logger.warning("结果中缺少 transcription_url")
                    continue
                    
                try:
                    # 获取转写内容
                    import requests
                    response = requests.get(item['transcription_url'])
                    response.raise_for_status()
                    transcription = response.json()
                    
                    # 记录转写内容用于调试
                    self.logger.debug(f"转写内容: {json.dumps(transcription, ensure_ascii=False, indent=2)}")
                    
                    # 解析转写内容
                    if 'transcripts' in transcription:
                        for transcript in transcription['transcripts']:
                            if 'sentences' in transcript:
                                for sentence in transcript['sentences']:
                                    text = sentence.get('text', '').strip()
                                    if text:
                                        start_time = sentence.get('begin_time', 0) / 1000.0  # 转换为秒
                                        end_time = sentence.get('end_time', 0) / 1000.0
                                        segments.append((text, start_time, end_time))
                                        
                except Exception as e:
                    self.logger.error(f"处理转写URL时出错: {str(e)}")
                    continue
            
            if not segments:
                self.logger.error("未能从结果中提取到任何文本")
                self.logger.debug(f"原始结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
            else:
                self.logger.info(f"成功提取了 {len(segments)} 个文本片段")
            
            return segments
            
        except Exception as e:
            self.logger.error(f"提取文本时出错: {str(e)}")
            return []
    
    def recognize_speech(self, audio_path: str, file_url: str) -> Optional[Dict]:
        """识别音频文件中的语音。
        
        Args:
            audio_path (str): 音频文件路径
            file_url (str): 已上传到OSS的文件URL
            
        Returns:
            Optional[Dict]: 识别结果
        """
        try:
            # 计算音频文件大小和时长
            file_size = os.path.getsize(audio_path) / (1024 * 1024)  # 转换为MB
            audio = AudioSegment.from_file(audio_path)
            duration = len(audio) / 1000  # 转换为秒
            
            self.logger.debug(f"音频文件信息:")
            self.logger.debug(f"- 路径: {audio_path}")
            self.logger.debug(f"- 大小: {file_size:.2f}MB")
            self.logger.debug(f"- 时长: {duration:.2f}秒")
            self.logger.debug(f"- 采样率: {audio.frame_rate}Hz")
            self.logger.debug(f"- 声道数: {audio.channels}")
            self.logger.debug(f"- 位深度: {audio.sample_width * 8}位")
            
            # 预估成本
            estimated_cost = duration * self.PRICE_PER_SECOND['paraformer-v2']
            self.logger.debug(f"预估成本: ¥{estimated_cost:.4f}")
            
            # 更新总费用统计
            self.total_tokens['paraformer-v2'] = float(duration)  # 更新语音识别的时长统计

            # 构建请求参数
            request_params = {
                "model": "paraformer-v2",
                "file_urls": [file_url],
                "format": "mp3",
                "sample_rate": 16000,
                "enable_timestamps": True,
                "enable_sentence_detection": True
            }
            
            # 记录请求参数
            self.logger.debug(f"语音识别请求参数:\n{json.dumps(request_params, ensure_ascii=False, indent=2)}")
            
            # 提交异步转写任务
            self.logger.info("提交语音识别任务...")
            start_time = time.time()
            task_response = Transcription.async_call(**request_params)
            
            # 记录任务提交响应
            self.logger.debug(f"任务提交响应:\n{json.dumps(task_response.__dict__, ensure_ascii=False, indent=2)}")
            
            if not task_response or not task_response.output:
                raise Exception("提交任务失败")
                
            # 获取任务ID
            task_id = task_response.output.task_id
            self.logger.info(f"等待转写结果... (任务ID: {task_id})")
            
            # 记录轮询开始时间
            poll_start_time = time.time()
            
            # 等待任务完成并获取结果
            response = Transcription.wait(task=task_id)
            
            # 记录轮询结束时间和总耗时
            poll_end_time = time.time()
            total_duration = poll_end_time - start_time
            poll_duration = poll_end_time - poll_start_time
            
            self.logger.debug(f"转写任务耗时统计:")
            self.logger.debug(f"- 总耗时: {total_duration:.2f}秒")
            self.logger.debug(f"- 轮询耗时: {poll_duration:.2f}秒")
            
            # 检查响应
            if not response or response.status_code != HTTPStatus.OK:
                error_msg = response.message if response else "无效的响应"
                raise Exception(f"语音识别失败: {error_msg}")
                
            # 记录完整的响应内容
            self.logger.debug(f"转写最终响应:\n{json.dumps(response.output, ensure_ascii=False, indent=2)}")
            
            # 计算实际成本
            actual_cost = duration * self.PRICE_PER_SECOND['paraformer-v2']
            self.logger.debug(f"语音识别任务统计:")
            self.logger.debug(f"- 音频时长: {duration:.2f}秒")
            self.logger.debug(f"- 实际成本: ¥{actual_cost:.4f} (按 ¥{self.PRICE_PER_SECOND['paraformer-v2']}/秒 计算)")
            
            self.logger.info("语音识别任务完成")
            return response.output
            
        except Exception as e:
            self.logger.error(f"语音识别失败: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            return None
    
    def get_query_headers(self, request_id: str) -> dict:
        """生成查询请求的请求头
        Args:
            request_id: 提交任务时的请求ID
        Returns:
            dict: 查询请求头
        """
        return {
            "X-Api-App-Key": self.app_id,
            "X-Api-Access-Key": self.access_token,
            "X-Api-Resource-Id": "volc.bigasr.auc",
            "X-Api-Request-Id": request_id,  # 使用提交任务时的 request_id
            "Content-Type": "application/json"  # 添加 Content-Type 头
        }
        
    def get_submit_headers(self, request_id: str = None) -> dict:
        """生成提交任务的请求头
        Args:
            request_id: 请求ID，如果为None则生成新的UUID
        Returns:
            dict: 提交任务请求头
        """
        if request_id is None:
            request_id = str(uuid.uuid4())
            
        return {
            "X-Api-App-Key": self.app_id,
            "X-Api-Access-Key": self.access_token,
            "X-Api-Resource-Id": "volc.bigasr.auc",
            "X-Api-Request-Id": request_id,
            "X-Api-Sequence": "-1",
            "Content-Type": "application/json"
        }
    
    def clean_text(self, text: str) -> str:
        """清理文本中的特殊标记，但保持时间戳
        Args:
            text: 原始文本
        Returns:
            str: 清理后的文本
        """
        if not text:
            return ""
        
        # 使用正则表达式清理标签，但保留时间戳
        lines = text.split('\n')
        cleaned_lines = []
        timestamp_pattern = r'\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]'
        
        for line in lines:
            # 如果是时间戳行，直接保留
            if re.match(timestamp_pattern, line.strip()):
                cleaned_lines.append(line)
                continue
            
            # 清理其他行的标签和多余空白
            cleaned_line = re.sub(r'</?(?:speech|Speech|bgm|BGM|silence|Silence|noise|Noise|NEUTRAL|neutral|[^>]+)>', '', line)
            cleaned_line = ' '.join(cleaned_line.split())
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
        
        return '\n'.join(cleaned_lines)
    
    def process_text(self, text: str, max_chars: int = 2000) -> list:
        """处理文本：清理、分割和合并
        Args:
            text: 要处理的文本
            max_chars: 每个片段的最大字符数
        Returns:
            list: 处理后的文本片段列表
        """
        if not text:
            return []
            
        # 清理文本
        text = self.clean_text(text)
        if not text:
            return []
            
        # 按段落分割
        paragraphs = []
        current = []
        current_length = 0
        
        for line in text.split('\n'):
            line = line.strip()
            if not line:
                if current:
                    paragraph = '\n'.join(current)
                    if len(paragraph) <= max_chars:
                        paragraphs.append(paragraph)
                    else:
                        # 如果段落太长，按句子分割
                        sentences = re.split(r'([.!?。！？]+)', line)
                        temp = []
                        temp_length = 0
                        for i in range(0, len(sentences), 2):
                            sentence = sentences[i]
                            if i + 1 < len(sentences):
                                sentence += sentences[i + 1]
                            if temp_length + len(sentence) > max_chars and temp:
                                paragraphs.append('\n'.join(temp))
                                temp = [sentence]
                                temp_length = len(sentence)
                            else:
                                temp.append(sentence)
                                temp_length += len(sentence)
                        if temp:
                            paragraphs.append('\n'.join(temp))
                    current = []
                    current_length = 0
            else:
                line_length = len(line)
                if current_length + line_length > max_chars and current:
                    paragraphs.append('\n'.join(current))
                    current = [line]
                    current_length = line_length
                else:
                    current.append(line)
                    current_length += line_length
        
        # 处理最后一个段落
        if current:
            paragraph = '\n'.join(current)
            if len(paragraph) <= max_chars:
                paragraphs.append(paragraph)
            else:
                # 如果最后的段落太长，按句子分割
                sentences = re.split(r'([.!?。！？]+)', paragraph)
                temp = []
                temp_length = 0
                for i in range(0, len(sentences), 2):
                    sentence = sentences[i]
                    if i + 1 < len(sentences):
                        sentence += sentences[i + 1]
                    if temp_length + len(sentence) > max_chars and temp:
                        paragraphs.append('\n'.join(temp))
                        temp = [sentence]
                        temp_length = len(sentence)
                    else:
                        temp.append(sentence)
                        temp_length += len(sentence)
                if temp:
                    paragraphs.append('\n'.join(temp))
        
        return paragraphs

    def save_result(self, text: str) -> None:
        """保存最终的处理结果
        Args:
            text: 要保存的文本内容
        """
        try:
            # 检查输入
            if not text or not text.strip():
                self.logger.warning("保存的文本为空")
                raise Exception("保存的文本为空")
            
            # 创建 transcripts 目录
            transcripts_dir = "transcripts"
            if not os.path.exists(transcripts_dir):
                os.makedirs(transcripts_dir)
            
            # 生成安全的文件名
            safe_title = re.sub(r'[<>:"/\\|?*]', '_', self.video_title)
            output_file = os.path.join(transcripts_dir, f"{safe_title}.md")
            
            # 保存文本
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# {self.video_title}\n\n")
                f.write(text)
            
            self.logger.info(f"结果已保存到: {output_file}")
            
            # 如果启用了Git，提交更改
            if os.path.exists('.git'):
                try:
                    # 添加文件到Git
                    subprocess.run(['git', 'add', output_file], check=True)
                    
                    # 提交更改
                    commit_message = f"添加转录文稿: {self.video_title}"
                    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
                    
                    self.logger.info("已提交到Git仓库")
                    
                except subprocess.CalledProcessError as e:
                    self.logger.warning(f"Git操作失败: {str(e)}")
                except Exception as e:
                    self.logger.warning(f"Git提交失败: {str(e)}")
            
        except Exception as e:
            self.logger.error(f"保存结果失败: {str(e)}")
            raise Exception(f"保存结果失败: {str(e)}")

    def format_time(self, seconds: float) -> str:
        """格式化时间显示。
        
        Args:
            seconds (float): 秒数
            
        Returns:
            str: 格式化后的时间字符串
        """
        if seconds < 60:
            return f"{int(seconds)}秒"
        if seconds < 3600:
            minutes = int(seconds / 60)
            return f"{minutes}分钟"
        
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        if minutes > 0:
            return f"{hours}小时{minutes}分钟"
        return f"{hours}小时"
    
    def handle_error(self, error: Exception, step: str, fatal: bool = False) -> None:
        """集中处理错误
        Args:
            error: 异常对象
            step: 发生错误的步骤
            fatal: 是否为致命错误
        """
        error_msg = f"{step}时发生错误: {str(error)}"
        self.logger.error(error_msg)
        
        # 记录详细的错误信息
        self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
        
        if fatal:
            sys.exit(1)
        else:
            self.logger.warning("尝试继续执行后续步骤")
            
    def setup_logging(self, debug: bool = False):
        """设置日志记录器。
        
        Args:
            debug (bool): 是否启用调试模式
        """
        # 创建 logs 目录（如果不存在）
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        # 生成带时间戳的日志文件名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = f'logs/transcriber_{timestamp}.log'
        
        # 设置日志格式
        file_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s\n'
            'File "%(pathname)s", line %(lineno)d'
        )
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # 配置日志记录器
        self.logger = logging.getLogger('youtube_transcriber')
        self.logger.setLevel(logging.DEBUG)  # 主记录器始终设置为 DEBUG 级别
        
        # 清除现有的处理器
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        # 设置文件处理器 - 始终记录 DEBUG 级别的日志到文件
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
        
        # 设置控制台处理器 - 根据 debug 标志设置日志级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
            
        # 记录初始化信息
        self.logger.info(f'日志文件已创建: {log_file}')
        if debug:
            self.logger.debug('调试模式已启用')
            self.logger.debug('系统信息:')
            self.logger.debug(f'- Python版本: {sys.version}')
            self.logger.debug(f'- 操作系统: {sys.platform}')
            self.logger.debug(f'- 工作目录: {os.getcwd()}')

    def log_step(self, step: str, status: str = "开始") -> None:
        """记录步骤状态"""
        self.logger.info(f"[{step}] {status}")
        
    def log_progress(self, current: int, total: int, step: str) -> None:
        """记录进度"""
        self.logger.info(f"[{step}] {current}/{total} ({current/total*100:.1f}%)")

    def init_resources(self) -> None:
        """初始化资源管理"""
        self.temp_files = []
        self.output_files = []
        
        # 创建必要的目录
        for dir_path in ['outputs', 'logs', 'temp']:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                self.logger.debug(f"创建目录: {dir_path}")
                
    def track_temp_file(self, file_path: str) -> None:
        """跟踪临时文件
        Args:
            file_path: 文件路径
        """
        if file_path and os.path.exists(file_path):
            self.temp_files.append(file_path)
            self.logger.debug(f"添加临时文件: {file_path}")
            
    def track_output_file(self, file_path: str) -> None:
        """跟踪输出文件
        Args:
            file_path: 文件路径
        """
        if file_path and os.path.exists(file_path):
            self.output_files.append(file_path)
            self.logger.debug(f"添加输出文件: {file_path}")
            
    def cleanup_temp_files(self, video_id: str = None) -> None:
        """清理临时文件
        Args:
            video_id: 视频ID,如果提供则只清理该视频相关的文件
        """
        try:
            files_to_clean = []
            
            # 收集需要清理的文件
            for temp_file in self.temp_files:
                if video_id:
                    if video_id in temp_file:
                        files_to_clean.append(temp_file)
                else:
                    files_to_clean.append(temp_file)
                    
            # 清理文件
            for file_path in files_to_clean:
                try:
                    if os.path.exists(file_path):
                        file_size = os.path.getsize(file_path)
                        os.remove(file_path)
                        self.logger.debug(f"删除临时文件: {file_path} (大小: {file_size} 字节)")
                        self.temp_files.remove(file_path)
                except Exception as e:
                    self.logger.warning(f"删除失败: {file_path} ({str(e)})")
                    
        except Exception as e:
            self.handle_error(e, "清理临时文件")
    
    def cleanup_all(self) -> None:
        """清理所有资源"""
        try:
            # 清理临时文件
            self.cleanup_temp_files()
            
            # 清理空目录
            for dir_path in ['temp']:
                if os.path.exists(dir_path) and not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    self.logger.debug(f"删除空目录: {dir_path}")
                    
        except Exception as e:
            self.handle_error(e, "清理资源")

    def get_config(self, key: str, default=None):
        """获取配置值
        Args:
            key: 配置键,支持点号分隔
            default: 默认值
        Returns:
            配置值
        """
        try:
            value = self.config
            for k in key.split('.'):
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
            
    def set_config(self, key: str, value) -> None:
        """设置配置值
        Args:
            key: 配置键,支持点号分隔
            value: 配置值
        """
        keys = key.split('.')
        config = self.config
        
        # 遍历到最后一个键
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
            
        # 设置值
        config[keys[-1]] = value
        
    def download_video(self, video_url: str) -> str:
        """下载YouTube视频
        Args:
            video_url: YouTube视频URL
        Returns:
            str: 视频ID
        """
        try:
            # 提取视频ID
            video_id = extract_video_id(video_url)
            if not video_id:
                raise ValueError("无效的YouTube URL")
                
            # 获取视频保存路径
            video_path = self.get_file_path('video', video_id=video_id)
            
            # 配置yt-dlp选项
            ydl_opts = {
                'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': video_path,
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
                'ignoreerrors': False,
                'retries': 3,
                'fragment_retries': 3,
                'concurrent_fragment_downloads': 4,
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'
                }]
            }
            
            # 下载视频
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.logger.info("开始下载视频...")
                info = ydl.extract_info(video_url, download=True)
                if not info:
                    raise Exception("无法获取视频信息")
                
            # 检查文件是否存在
            if not os.path.exists(video_path):
                # 检查是否有 .mp4 扩展名被自动添加
                video_path_with_ext = video_path + '.mp4'
                if os.path.exists(video_path_with_ext):
                    video_path = video_path_with_ext
                else:
                    raise Exception(f"视频下载失败，文件不存在: {video_path}")
                
            # 跟踪临时文件
            self.track_temp_file(video_path)
            
            # 记录视频信息
            file_size = os.path.getsize(video_path)
            self.logger.info(f"视频已下载: {video_path}")
            self.logger.info(f"文件大小: {file_size/1024/1024:.2f}MB")
            
            # 返回视频ID和路径
            return video_id, video_path
            
        except Exception as e:
            self.handle_error(e, "下载视频")
            return None, None
            
    def extract_audio(self, audio_path: str, video_id: str) -> str:
        """处理音频文件，转换为正确的格式。
        
        Args:
            audio_path: 输入音频文件路径
            video_id: 视频ID
            
        Returns:
            str: 处理后的音频文件路径
        """
        try:
            # 检查输入文件
            if not os.path.exists(audio_path):
                raise FileNotFoundError(f"音频文件不存在: {audio_path}")
                
            # 生成输出文件路径（使用wav格式）
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_path = os.path.join(self.DIRS['temp'], f"{timestamp}_{video_id}.wav")
            
            # 加载音频文件
            self.logger.info("加载音频文件...")
            audio = AudioSegment.from_file(audio_path)
            
            # 设置音频参数
            self.logger.info("转换音频格式...")
            audio = audio.set_frame_rate(16000)  # 设置采样率
            audio = audio.set_channels(1)        # 设置为单声道
            audio = audio.set_sample_width(2)    # 设置为16位
            
            # 标准化音量
            audio = audio.normalize()
            
            # 导出为WAV格式
            self.logger.info(f"保存处理后的音频到: {output_path}")
            audio.export(
                output_path,
                format='wav',
                parameters=[
                    "-ac", "1",         # 单声道
                    "-ar", "16000",     # 16kHz采样率
                    "-acodec", "pcm_s16le"  # 16位PCM编码
                ]
            )
            
            # 记录音频信息
            duration = len(audio) / 1000  # 转换为秒
            file_size = os.path.getsize(output_path)
            self.logger.info(f"音频处理完成:")
            self.logger.info(f"- 时长: {duration:.2f}秒")
            self.logger.info(f"- 大小: {file_size/1024/1024:.2f}MB")
            self.logger.info(f"- 采样率: {audio.frame_rate}Hz")
            self.logger.info(f"- 声道数: {audio.channels}")
            self.logger.info(f"- 位深度: {audio.sample_width * 8}位")
            
            # 删除原始MP3文件
            if os.path.exists(audio_path) and audio_path != output_path:
                os.remove(audio_path)
                self.logger.info(f"已删除原始MP3文件: {audio_path}")
            
            return output_path
            
        except Exception as e:
            self.logger.error(f"处理音频时出错: {str(e)}")
            if os.path.exists(audio_path):
                os.remove(audio_path)
                self.logger.info(f"清理失败的音频文件: {audio_path}")
            return None

    def save_transcript(self, text: str, video_id: str) -> None:
        """保存转写结果
        Args:
            text: 转写文本
            video_id: 视频ID
        """
        try:
            if not text:
                raise ValueError("文本为空")
                
            # 获取保存路径
            output_path = self.get_file_path('transcript', video_id=video_id)
            
            # 保存文件
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
                
            # 跟踪输出文件
            self.track_output_file(output_path)
            
            # 记录文件信息
            file_size = os.path.getsize(output_path)
            self.logger.info(f"保存文件: {output_path}")
            self.logger.info(f"文件大小: {file_size/1024:.1f}KB")
            
        except Exception as e:
            self.handle_error(e, "保存文本")

    def clean_resources(self, audio_path: str = None) -> None:
        """清理所有程序执行产生的中间文件。
        
        Args:
            audio_path (str, optional): 音频文件路径。如果不指定，则清理所有中间文件。
            
        清理内容包括：
        1. temp目录下的临时文件
        2. output目录下的输出文件
        3. OSS上的临时文件
        
        注意：logs目录下的日志文件会被保留
        """
        try:
            if audio_path:
                # 删除指定的音频文件
                if os.path.exists(audio_path):
                    os.remove(audio_path)
                    self.logger.info(f"已删除音频文件: {audio_path}")
            else:
                # 清理本地目录
                dirs_to_clean = {
                    'temp': '临时文件',
                    'output': '输出文件'  # 移除了 'logs' 目录
                }
                
                for dir_name, file_type in dirs_to_clean.items():
                    dir_path = self.DIRS.get(dir_name, dir_name)
                    if os.path.exists(dir_path):
                        try:
                            # 删除目录下的所有文件
                            for root, dirs, files in os.walk(dir_path, topdown=False):
                                for name in files:
                                    file_path = os.path.join(root, name)
                                    try:
                                        os.remove(file_path)
                                        self.logger.info(f"已删除{file_type}: {file_path}")
                                    except Exception as e:
                                        self.logger.warning(f"删除{file_type}失败: {file_path} ({str(e)})")
                                        
                            # 尝试删除空目录
                            try:
                                os.rmdir(dir_path)
                                self.logger.info(f"已删除空目录: {dir_path}")
                            except OSError:
                                pass  # 目录不为空或其他原因无法删除，忽略错误
                                    
                        except Exception as e:
                            self.logger.error(f"清理{file_type}目录失败: {dir_path} ({str(e)})")

                # 清理OSS临时文件
                try:
                    # 获取OSS配置
                    access_key = os.getenv('OSS_ACCESS_KEY')
                    access_secret = os.getenv('OSS_ACCESS_SECRET')
                    endpoint = os.getenv('OSS_ENDPOINT')
                    bucket_name = os.getenv('OSS_BUCKET')
                    
                    if all([access_key, access_secret, endpoint, bucket_name]):
                        # 初始化OSS客户端
                        auth = oss2.Auth(access_key, access_secret)
                        bucket = oss2.Bucket(auth, endpoint, bucket_name)
                        
                        # 删除audio/目录下的所有文件
                        self.logger.info("开始清理OSS临时文件...")
                        count = 0
                        for obj in oss2.ObjectIterator(bucket, prefix='audio/'):
                            try:
                                bucket.delete_object(obj.key)
                                count += 1
                                self.logger.info(f"已删除OSS文件: {obj.key}")
                            except Exception as e:
                                self.logger.warning(f"删除OSS文件失败: {obj.key} ({str(e)})")
                        
                        self.logger.info(f"OSS清理完成，共删除 {count} 个文件")
                    else:
                        self.logger.warning("未配置OSS环境变量，跳过OSS清理")
                        
                except Exception as e:
                    self.logger.error(f"清理OSS文件失败: {str(e)}")
                
                self.logger.info("所有清理任务完成")
                
        except Exception as e:
            self.logger.error(f"清理资源时发生错误: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            # 不抛出异常，因为这是清理步骤

    def save_text(self, text_segments: List[Tuple[str, float, float]], output_path: str, video_id: str = None, video_url: str = None, video_title: str = None) -> None:
        """保存文本到Markdown文件。
        
        Args:
            text_segments (List[Tuple[str, float, float]]): 包含 (text, start_time, end_time) 元组的列表
            output_path (str): 输出文件路径
            video_id (str, optional): 视频ID
            video_url (str, optional): 视频URL
            video_title (str, optional): 视频标题
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                # 写入元数据
                f.write('---\n')
                if video_id:
                    f.write(f'video_id: {video_id}\n')
                if video_url:
                    f.write(f'video_url: {video_url}\n')
                if video_title:
                    f.write(f'video_title: {video_title}\n')
                f.write(f'created_at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                f.write('---\n\n')
                
                # 写入标题
                if video_title:
                    f.write(f'# {video_title}\n\n')
                
                # 写入内容
                for text, start_time, end_time in text_segments:
                    # 将秒转换为分钟和秒
                    start_minutes = int(start_time // 60)
                    start_seconds = int(start_time % 60)
                    end_minutes = int(end_time // 60)
                    end_seconds = int(end_time % 60)
                    
                    # 格式化时间戳 [MM:SS - MM:SS]
                    timestamp = f"[{start_minutes:02d}:{start_seconds:02d} - {end_minutes:02d}:{end_seconds:02d}]"
                    
                    # 写入带时间戳的文本，使用Markdown引用格式
                    f.write(f"> {timestamp}\n")
                    f.write(f"{text.strip()}\n\n")
                    
            self.logger.info(f"Markdown文件已保存到: {output_path}")
        except Exception as e:
            self.logger.error(f"保存Markdown文件时出错: {str(e)}")
            raise

    def download_audio(self, url: str, output_path: str) -> None:
        """从YouTube视频下载音频。
        
        Args:
            url (str): YouTube视频URL
            output_path (str): 输出音频文件路径
        """
        try:
            self.logger.info(f"开始下载音频: {url}")
            
            # 设置下载选项
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }],
                'outtmpl': output_path.replace('.mp3', ''),
                'quiet': True,
                'no_warnings': True,
                'logger': self.logger
            }
            
            # 下载音频
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            self.logger.info(f"音频已下载到: {output_path}")
            
        except Exception as e:
            self.logger.error(f"下载音频失败: {str(e)}")
            raise

    def upload_to_oss(self, local_file: str) -> str:
        """上传文件到 OSS。
        
        Args:
            local_file (str): 本地文件路径
            
        Returns:
            str: 文件访问 URL
        """
        try:
            self.logger.info(f"开始上传文件到 OSS: {os.path.basename(local_file)}")
            
            # 初始化 OSS 客户端
            access_key = os.getenv('OSS_ACCESS_KEY')
            access_secret = os.getenv('OSS_ACCESS_SECRET')
            endpoint = os.getenv('OSS_ENDPOINT')
            bucket_name = os.getenv('OSS_BUCKET')
            
            if not all([access_key, access_secret, endpoint, bucket_name]):
                missing_vars = [var for var, value in {
                    'OSS_ACCESS_KEY': access_key,
                    'OSS_ACCESS_SECRET': access_secret,
                    'OSS_ENDPOINT': endpoint,
                    'OSS_BUCKET': bucket_name
                }.items() if not value]
                raise ValueError(f"缺少OSS配置: {', '.join(missing_vars)}")
            
            # 记录OSS配置信息（注意不要记录敏感信息）
            self.logger.debug("OSS配置信息:")
            self.logger.debug(f"- Endpoint: {endpoint}")
            self.logger.debug(f"- Bucket: {bucket_name}")
            
            # 创建 OSS 客户端
            auth = oss2.Auth(access_key, access_secret)
            bucket = oss2.Bucket(auth, endpoint, bucket_name)
            
            # 生成唯一的文件名
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            file_name = f"audio/{timestamp}/{os.path.basename(local_file)}"
            self.logger.debug(f"OSS目标路径: {file_name}")
            
            # 检查本地文件
            file_size = os.path.getsize(local_file)
            self.logger.debug(f"本地文件信息:")
            self.logger.debug(f"- 路径: {local_file}")
            self.logger.debug(f"- 大小: {file_size/1024/1024:.2f}MB")
            
            # 设置文件元数据
            headers = {
                'Content-Type': 'audio/wav',
                'Cache-Control': 'no-cache'
            }
            self.logger.debug(f"上传请求头: {headers}")
            
            # 上传文件
            self.logger.debug("开始上传...")
            start_time = time.time()
            
            with open(local_file, 'rb') as f:
                result = bucket.put_object(file_name, f, headers=headers)
                
            end_time = time.time()
            upload_duration = end_time - start_time
            upload_speed = file_size / (upload_duration * 1024 * 1024)  # MB/s
            
            self.logger.debug("上传结果:")
            self.logger.debug(f"- 状态码: {result.status}")
            self.logger.debug(f"- 请求ID: {result.request_id}")
            self.logger.debug(f"- ETag: {result.etag}")
            self.logger.debug(f"- 耗时: {upload_duration:.2f}秒")
            self.logger.debug(f"- 速度: {upload_speed:.2f}MB/s")
            
            # 生成带签名的 URL（1小时有效期）
            url = bucket.sign_url('GET', file_name, 3600, slash_safe=True)
            self.logger.debug(f"生成的签名URL: {url}")
            
            self.logger.info(f"文件上传成功: {file_name}")
            return url
            
        except Exception as e:
            self.logger.error(f"上传文件到 OSS 失败: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            raise

    def format_text_for_translation(self, text_segments: List[Tuple[str, float, float]]) -> str:
        """格式化文本用于翻译。
        
        Args:
            text_segments: 文本片段列表，每个元素为 (text, start_time, end_time)
            
        Returns:
            str: 格式化后的文本
        """
        formatted_text = ""
        for text, start_time, end_time in text_segments:
            start_minutes = int(start_time // 60)
            start_seconds = int(start_time % 60)
            end_minutes = int(end_time // 60)
            end_seconds = int(end_time % 60)
            timestamp = f"[{start_minutes:02d}:{start_seconds:02d} - {end_minutes:02d}:{end_seconds:02d}]"
            formatted_text += f"{timestamp} {text.strip()}\n"
        return formatted_text
        
    def save_final_text(self, file_path: str, text: str, video_id: str, video_url: str, video_title: str) -> None:
        """保存最终文本到文件。
        
        Args:
            file_path: 文件路径
            text: 文本内容
            video_id: 视频ID
            video_url: 视频URL
            video_title: 视频标题
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            # 写入元数据
            f.write('---\n')
            f.write(f'video_id: {video_id}\n')
            f.write(f'video_url: {video_url}\n')
            f.write(f'video_title: {video_title}\n')
            f.write(f'created_at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            f.write('---\n\n')
            # 写入标题
            f.write(f'# {video_title}\n\n')
            # 写入翻译后的内容
            f.write(text)
            
        file_size = os.path.getsize(file_path)
        self.logger.info(f"文件保存成功:")
        self.logger.info(f"- 路径: {file_path}")
        self.logger.info(f"- 大小: {file_size/1024:.1f}KB")

    def verify_env_variables(self):
        """验证必要的环境变量是否已设置"""
        required_vars = {
            'OSS_ACCESS_KEY': '阿里云 OSS 访问密钥',
            'OSS_ACCESS_SECRET': '阿里云 OSS 访问密钥密文',
            'OSS_ENDPOINT': '阿里云 OSS 访问端点',
            'OSS_BUCKET': '阿里云 OSS 存储桶名称'
        }
        
        missing_vars = []
        for var, description in required_vars.items():
            if not os.getenv(var):
                missing_vars.append(f"{var} ({description})")
                
        if missing_vars:
            error_msg = "缺少必要的环境变量:\n" + "\n".join(f"- {var}" for var in missing_vars)
            self.logger.error(error_msg)
            raise ValueError(error_msg)

    def estimate_processing_time(self, duration: float) -> dict:
        """预估处理时间（秒）
        
        预估公式：
        总时间 = 下载时间 + 音频处理时间 + 上传时间 + 识别时间 + 翻译时间
        
        其中：
        - 下载时间 ≈ 视频时长 * 0.3（考虑压缩比和网络速度）
        - 音频处理时间 ≈ 视频时长 * 0.2
        - 上传时间 ≈ 视频时长 * 0.1（音频文件比视频小）
        - 识别时间 ≈ 视频时长 * 1.2（语音识别通常需要1-2倍时长）
        - 翻译时间 ≈ 视频时长 * 0.4（假设每分钟音频产生约100个单词）
        
        Args:
            duration: 视频时长（秒）
        
        Returns:
            dict: 包含各阶段预估时间的字典
        """
        estimates = {
            'download': duration * 0.3,
            'audio_process': duration * 0.2,
            'upload': duration * 0.1,
            'recognition': duration * 1.2,
            'translation': duration * 0.4
        }
        
        # 计算总时间并添加10%的缓冲
        estimates['total'] = sum(estimates.values()) * 1.1
        
        return estimates

def extract_video_id(url: str) -> Optional[str]:
    """从YouTube URL中提取视频ID。
    
        Args:
        url (str): YouTube视频URL
        
    Returns:
        Optional[str]: 视频ID，如果无效则返回None
    """
    try:
        # 尝试从URL中提取视频ID
        if 'youtu.be' in url:
            return url.split('/')[-1].split('?')[0]
        elif 'youtube.com' in url:
            if 'v=' in url:
                return url.split('v=')[1].split('&')[0]
            elif 'embed/' in url:
                return url.split('embed/')[-1].split('?')[0]
        return None
    except Exception:
        return None

def process_url_list(transcriber, url_file: str):
    """处理URL列表文件
        Args:
        transcriber: YouTubeTranscriber实例
        url_file: URL列表文件路径
    """
    try:
        with open(url_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        
        if not urls:
            transcriber.logger.error(f"文件 {url_file} 中没有找到有效的URL")
            return
            
        transcriber.logger.info(f"从文件中读取到 {len(urls)} 个URL")
        for i, url in enumerate(urls, 1):
            transcriber.logger.info(f"\n处理第 {i}/{len(urls)} 个视频: {url}")
            try:
                transcriber.process_video(url, None)
            except Exception as e:
                transcriber.logger.error(f"处理视频 {url} 失败: {str(e)}")
                transcriber.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
                continue
                
    except FileNotFoundError:
        transcriber.logger.error(f"找不到文件: {url_file}")
    except Exception as e:
        transcriber.logger.error(f"读取URL列表文件失败: {str(e)}")
        transcriber.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='YouTube视频转录工具')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url', help='YouTube视频URL')
    group.add_argument('--file', help='包含YouTube视频URL列表的文件路径')
    group.add_argument('--clean', action='store_true', help='清理所有中间文件和缓存')
    parser.add_argument('--debug', action='store_true', help='显示调试日志')
    
    try:
        args = parser.parse_args()
        
        # 创建转录器实例时传入debug参数
        transcriber = YouTubeTranscriber()
        transcriber.setup_logging(debug=args.debug)
        
        if args.clean:
            transcriber.clean_resources()
            transcriber.logger.info("清理完成")
        elif args.url:
            transcriber.process_video(args.url)
        elif args.file:
            with open(args.file) as f:
                urls = [line.strip() for line in f if line.strip()]
            for url in urls:
                transcriber.process_video(url)
                
    except SystemExit:
        print("提示: 请提供必要的参数")
        parser.print_help()
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n错误: {str(e)}")
        if args.debug:
            traceback.print_exc()
        sys.exit(1)
    finally:
        # 程序结束前再次清理
        transcriber.clean_resources()

if __name__ == '__main__':
    main() 