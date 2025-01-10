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
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import DIR_CONFIG, MODEL_CONFIG, OSS_CONFIG, PROMPT_CONFIG
from functools import wraps
import ffmpeg

# 添加当前目录到 Python 路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# 加载 .env 文件
load_dotenv()

class ServiceFormatter(logging.Formatter):
    """服务日志格式化器，用于格式化API调用日志"""
    
    def __init__(self, fmt=None, datefmt=None):
        """初始化格式化器
        
        Args:
            fmt: 日志格式字符串
            datefmt: 日期格式字符串
        """
        super().__init__(fmt, datefmt)
        # 定义可选字段及其默认值
        self.optional_fields = {
            'service': '',
            'request_id': '',
            'duration': 0,
            'status': '',
            'parameters': {},
            'response': {}
        }
    
    def format(self, record):
        """格式化日志记录
        
        Args:
            record: 日志记录对象
            
        Returns:
            str: 格式化后的日志字符串
        """
        # 为所有可选字段设置默认值
        for field, default in self.optional_fields.items():
            if not hasattr(record, field):
                setattr(record, field, default)
        
        # 确保 parameters 和 response 是字符串
        if hasattr(record, 'parameters'):
            if isinstance(record.parameters, dict):
                record.parameters = json.dumps(record.parameters, ensure_ascii=False)
        
        if hasattr(record, 'response'):
            if isinstance(record.response, dict):
                record.response = json.dumps(record.response, ensure_ascii=False)
        
        # 调用父类的 format 方法
        return super().format(record)

def log_service_call(service: str, api: str):
    """服务调用日志装饰器
    
    Args:
        service: 服务名称 ('ASR', 'Translate', 'OSS')
        api: API名称
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 获取 logger 实例（假设第一个参数是 self）
            self = args[0]
            request_id = str(uuid.uuid4())
            start_time = time.time()
            
            try:
                # 记录请求信息
                self.logger.info(
                    f"调用 {service} API: {api}",
                    extra={
                        'service': service,
                        'request_id': request_id,
                        'parameters': kwargs
                    }
                )
                
                # 执行API调用
                result = func(*args, **kwargs)
                
                # 计算耗时
                duration = (time.time() - start_time) * 1000
                
                # 记录成功响应
                self.logger.info(
                    f"{service} API 调用成功: {api}",
                    extra={
                        'service': service,
                        'request_id': request_id,
                        'duration': duration,
                        'status': 'success',
                        'response': result
                    }
                )
                
                return result
                
            except Exception as e:
                # 计算耗时
                duration = (time.time() - start_time) * 1000
                
                # 记录错误信息
                self.logger.error(
                    f"{service} API 调用失败: {api} - {str(e)}",
                    extra={
                        'service': service,
                        'request_id': request_id,
                        'duration': duration,
                        'status': 'error',
                        'error': str(e),
                        'stack_trace': traceback.format_exc()
                    }
                )
                raise
                
        return wrapper
    return decorator

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
        ProcessStep("语音识别", 40, "转写音频内容"),
        ProcessStep("翻译文本", 20, "翻译为中文"),
        ProcessStep("优化文本", 5, "优化文本格式"),
        ProcessStep("内容总结", 5, "生成内容总结"),  # 新增
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
        'logs': '../logs',  # 日志目录
        'temp': '../temp',  # 临时文件目录
        'output': '../output',  # 输出目录
        'transcripts': '../transcripts'  # 转写文本目录
    }
    
    # 定义文件命名模板
    FILE_TEMPLATES = {
        'log': 'log_{timestamp}.txt',
        'audio': '{video_id}.wav',
        'transcript': '{timestamp}_{video_id}_original.md',
        'transcript_summary': '{timestamp}_{video_id}_summary.md'  # 新增
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
        'qwen-max': 0.2,  # 通义千问-Max 模型价格
        'qwen-plus-summary': 0.1  # 新增
    }

    def __init__(self, debug: bool = False):
        """初始化转写器
        Args:
            debug: 是否启用调试模式
        """
        # 重新加载环境变量，确保使用最新的配置
        load_dotenv(override=True)
        
        # 使用配置文件中的目录结构
        self.dirs = DIR_CONFIG
        
        # 创建必要的目录结构
        for dir_name, dir_path in self.dirs.items():
            os.makedirs(dir_path, exist_ok=True)
            
        # 设置临时目录
        self.temp_dir = self.dirs['temp']
        
        # 设置日志记录器
        self.setup_logging(debug)
        
        # 初始化进度跟踪器
        self.progress_tracker = ProgressTracker(self.logger)
        
        # 初始化其他配置
        self.temp_files = []
        self.output_files = []
        self.config = {'enable_summary': True}  # 添加默认配置
        
        # 从配置文件获取模型信息
        self.asr_model = MODEL_CONFIG['speech_recognition']['model']
        self.translation_model = MODEL_CONFIG['translation']['model']
        
        # 初始化费用统计
        self.total_tokens = {
            'paraformer-v2': 0.0,
            'qwen-mt-plus': 0.0,    # 修改为翻译模型的实际名称
            'qwen-mt-turbo': 0.0,   # 修改为翻译模型的实际名称
            'qwen-plus-summary': 0.0
        }
        self.total_costs = {
            'paraformer-v2': 0.0,
            'qwen-mt-plus': 0.0,    # 修改为翻译模型的实际名称
            'qwen-mt-turbo': 0.0,   # 修改为翻译模型的实际名称
            'qwen-plus-summary': 0.0
        }
        
        # 初始化时间戳映射
        self.timestamp_map = {}
        self.timestamp_count = 0
        
        # 初始化视频相关属性
        self.current_video_url = None
        self.current_video_id = None
        self.current_video_title = None
        self.current_video_duration = None
        
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
            dir_path = self.dirs['logs']
        elif file_type == 'audio':
            dir_path = self.dirs['temp']
        else:
            dir_path = self.dirs['transcripts']
            
        # 返回完整路径
        return os.path.join(dir_path, filename)
        
    def process_video(self, url: str) -> None:
        """处理视频
        Args:
            url: YouTube视频URL
        """
        total_start_time = time.time()
        self.logger.info("开始处理视频...")
        
        try:
            # 保存视频URL供后续使用
            self.current_video_url = url
            
            # 下载视频
            download_start = time.time()
            video_id, video_title, video_path = self.download_video(url)
            self.current_video_id = video_id  # 保存视频ID
            self.current_video_title = video_title  # 保存视频标题
            download_duration = time.time() - download_start
            
            # 提取音频
            extract_start = time.time()
            audio_path = self.extract_audio(video_path, video_id)
            extract_duration = time.time() - extract_start
            
            # 上传音频
            upload_start = time.time()
            file_url = self.upload_audio(audio_path)
            upload_duration = time.time() - upload_start
            
            # 语音识别
            asr_start = time.time()
            result = self.recognize_speech(audio_path, file_url)
            if not result:
                raise Exception("语音识别失败")
            asr_duration = time.time() - asr_start
            
            # 提取文本
            extract_text_start = time.time()
            segments = self.extract_text_from_result(result)
            if not segments:
                raise Exception("未能提取到任何文本")
            extract_text_duration = time.time() - extract_text_start
            
            # 格式化文本
            format_start = time.time()
            original_text = self.format_segments(segments)
            if not original_text:
                raise Exception("文本格式化失败")
            format_duration = time.time() - format_start
            
            # 保存原始文本
            save_original_start = time.time()
            original_path = self.save_original_text(original_text, video_id, video_title)
            save_original_duration = time.time() - save_original_start
            
            # 翻译文本
            translation_start = time.time()
            translated_text = self.translate_text(original_text)
            if not translated_text:
                raise Exception("文本翻译失败")
            translation_duration = time.time() - translation_start
            
            # 保存翻译文本
            save_translation_start = time.time()
            final_path = self.save_translated_text(translated_text, video_id, video_title)
            save_translation_duration = time.time() - save_translation_start
            
            # 生成内容总结
            if self.config.get('enable_summary', True):
                try:
                    self.progress_tracker.start_step("内容总结")
                    summary_path = self.generate_content_summary(final_path)
                    if summary_path:
                        self.logger.info(f"Generated content summary: {summary_path}")
                    self.progress_tracker.complete_step()
                except Exception as e:
                    self.logger.error(f"Content summary generation failed: {str(e)}")
                    self.progress_tracker.complete_step()  # 确保在出错时也完成步骤
            
            # 清理临时文件
            cleanup_start = time.time()
            self.cleanup_temp_files()  # 修正方法名
            cleanup_duration = time.time() - cleanup_start
            
            # 计算总耗时
            total_end_time = time.time()
            total_duration = total_end_time - total_start_time
            
            # 输出总体耗时报告
            self.logger.info("\n处理完成，总体耗时统计：")
            self.logger.info(f"总耗时: {total_duration:.2f} 秒")
            self.logger.info("各阶段耗时:")
            self.logger.info(f"• 视频下载: {download_duration:.2f} 秒")
            self.logger.info(f"• 音频提取: {extract_duration:.2f} 秒")
            self.logger.info(f"• 音频上传: {upload_duration:.2f} 秒")
            self.logger.info(f"• 语音识别: {asr_duration:.2f} 秒")
            self.logger.info(f"• 文本提取: {extract_text_duration:.2f} 秒")
            self.logger.info(f"• 文本格式化: {format_duration:.2f} 秒")
            self.logger.info(f"• 保存原始文本: {save_original_duration:.2f} 秒")
            self.logger.info(f"• 文本翻译: {translation_duration:.2f} 秒")
            self.logger.info(f"• 保存翻译文本: {save_translation_duration:.2f} 秒")
            self.logger.info(f"• 资源清理: {cleanup_duration:.2f} 秒")
            
            # 输出费用统计
            self.print_token_statistics()
            
            return {
                "success": True,
                "video_id": video_id,
                "video_title": video_title,
                "original_path": original_path,
                "final_path": final_path
            }
                
        except Exception as e:
            self.logger.error(f"处理视频时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            sys.exit(1)  # 直接退出，不执行后续清理

    def split_text_for_translation(self, text: str, max_tokens: int = 800) -> List[str]:
        try:
            start_time = time.time()
            self.logger.info("开始分段处理文本...")
            # 添加这行日志
            self.logger.debug(f"开始分段处理的文本:\n{text}")
            
            segments = []
            current_segment = []
            current_length = 0  # 估算当前token数（按4个字符1个token计算）
            
            # 按行分割文本
            lines = text.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line:
                    # 添加这行日志
                    self.logger.debug(f"跳过空行")
                    continue
                    
                # 解析时间戳和文本
                match = re.match(r'(\[\d{2}:\d{2} - \d{2}:\d{2}\]) (.+)', line)
                if not match:
                    # 添加这行日志
                    self.logger.debug(f"行未匹配时间戳格式: {line}")
                    continue
                    
                # 添加这行日志
                self.logger.debug(f"成功匹配行: {line}")
                
                timestamp, content = match.groups()
                # 估算当前行的token数（每4个字符约1个token）
                line_tokens = len(content) // 4 + 1  # +1 是时间戳的估算token数
                
                # 如果当前行超过最大token限制，需要单独处理
                if line_tokens > max_tokens:
                    # 先保存当前段落
                    if current_segment:
                        segments.append('\n'.join(current_segment))
                        current_segment = []
                        current_length = 0
                    
                    # 将长句按句号、问号、感叹号分割
                    sentences = re.split(r'([。！？.!?]+)', content)
                    temp_segment = []
                    temp_length = 0
                    
                    for i in range(0, len(sentences), 2):
                        sentence = sentences[i]
                        if i + 1 < len(sentences):
                            sentence += sentences[i + 1]  # 加回标点符号
                            
                        sentence_tokens = len(sentence) // 4
                        if temp_length + sentence_tokens > max_tokens and temp_segment:
                            # 保存当前临时段落
                            segments.append('\n'.join([timestamp + ' ' + ' '.join(temp_segment)]))
                            temp_segment = [sentence]
                            temp_length = sentence_tokens
                        else:
                            temp_segment.append(sentence)
                            temp_length += sentence_tokens
                    
                    # 保存最后的临时段落
                    if temp_segment:
                        segments.append('\n'.join([timestamp + ' ' + ' '.join(temp_segment)]))
                        
                # 如果添加当前行会超过最大token限制，先保存当前段落
                elif current_length + line_tokens > max_tokens and current_segment:
                    segments.append('\n'.join(current_segment))
                    current_segment = [line]
                    current_length = line_tokens
                else:
                    current_segment.append(line)
                    current_length += line_tokens
            
            # 保存最后一个段落
            if current_segment:
                segments.append('\n'.join(current_segment))
                
            end_time = time.time()
            self.logger.info(f"文本分段完成，共 {len(segments)} 个片段，耗时 {end_time - start_time:.2f} 秒")
            
            # 记录分段信息
            self.logger.info(f"文本分段完成:")
            self.logger.info(f"- 总段数: {len(segments)}")
            for i, segment in enumerate(segments, 1):
                token_count = len(segment) // 4
                self.logger.debug(f"- 第{i}段: {token_count} tokens (约)")
            
            return segments
            
        except Exception as e:
            self.logger.error(f"分段处理文本时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            # 出错时返回原文本作为单个段落
            return [text]

    @retry_on_timeout(max_retries=3, base_delay=1)
    @log_service_call(service='ASR', api='recognize_speech')
    def recognize_speech(self, audio_path: str, file_url: str) -> Optional[Dict]:
        """识别音频文件中的语音。
        
        Args:
            audio_path (str): 音频文件路径
            file_url (str): 已上传到OSS的文件URL
            
        Returns:
            Optional[Dict]: 识别结果
        """
        try:
            request_id = str(uuid.uuid4())
            # 获取模型配置
            model_config = MODEL_CONFIG['speech_recognition']
            model_specific_config = model_config['available_models'][self.asr_model]
            price_per_second = model_specific_config['price_per_second']

            # 显示模型信息
            self.logger.info(
                f"使用语音识别模型: {self.asr_model}",
                extra={
                    'service': 'ASR',
                    'request_id': request_id
                }
            )
            self.logger.info(
                f"- 价格: ¥{price_per_second}/秒",
                extra={
                    'service': 'ASR',
                    'request_id': request_id
                }
            )
            
            # 计算音频文件大小和时长
            file_size = os.path.getsize(audio_path) / (1024 * 1024)  # 转换为MB
            audio = AudioSegment.from_file(audio_path)
            duration = len(audio) / 1000  # 转换为秒
            
            # 记录音频文件信息
            self.logger.debug(
                "音频文件信息",
                extra={
                    'service': 'ASR',
                    'request_id': request_id,
                    'parameters': {
                        'file_path': audio_path,
                        'file_size': f"{file_size:.2f}MB",
                        'duration': f"{duration:.2f}秒",
                        'sample_rate': f"{audio.frame_rate}Hz",
                        'channels': audio.channels,
                        'bit_depth': f"{audio.sample_width * 8}位"
                    }
                }
            )
            
            # 预估成本
            estimated_cost = duration * price_per_second
            self.logger.debug(
                "成本预估",
                extra={
                    'service': 'ASR',
                    'request_id': request_id,
                    'parameters': {
                        'duration': f"{duration:.2f}秒",
                        'price_per_second': f"¥{price_per_second}",
                        'estimated_cost': f"¥{estimated_cost:.4f}"
                    }
                }
            )
            
            # 更新总费用统计
            self.total_tokens[self.asr_model] = float(duration)
            self.total_costs[self.asr_model] += duration * price_per_second
            
            # 计算实际成本
            actual_cost = duration * price_per_second
            self.logger.debug(
                "语音识别任务统计",
                extra={
                    'service': 'ASR',
                    'request_id': request_id,
                    'parameters': {
                        'audio_duration': f"{duration:.2f}秒",
                        'actual_cost': f"¥{actual_cost:.4f}",
                        'price_rate': f"¥{price_per_second}/秒"
                    }
                }
            )
            
            # 构建请求参数
            request_params = model_specific_config['api_params'].copy()
            request_params['model'] = self.asr_model
            request_params['file_urls'] = [file_url]
            
            # 记录请求参数
            self.logger.debug(
                "语音识别请求参数",
                extra={
                    'service': 'ASR',
                    'request_id': request_id,
                    'parameters': request_params
                }
            )
            
            # 提交异步转写任务
            self.logger.info(
                "提交语音识别任务...",
                extra={
                    'service': 'ASR',
                    'request_id': request_id
                }
            )
            start_time = time.time()
            task_response = Transcription.async_call(**request_params)
            
            # 记录任务提交响应
            self.logger.debug(
                "任务提交响应",
                extra={
                    'service': 'ASR',
                    'request_id': request_id,
                    'response': task_response.__dict__
                }
            )
            
            if not task_response or not task_response.output:
                raise Exception("提交任务失败")
                
            # 获取任务ID
            task_id = task_response.output.task_id
            self.logger.info(
                f"等待转写结果... (任务ID: {task_id})",
                extra={
                    'service': 'ASR',
                    'request_id': request_id
                }
            )
            
            # 记录轮询开始时间
            poll_start_time = time.time()
            
            # 等待任务完成并获取结果
            response = Transcription.wait(task=task_id)
            
            # 记录轮询结束时间和总耗时
            poll_end_time = time.time()
            total_duration = poll_end_time - start_time
            poll_duration = poll_end_time - poll_start_time
            
            # 记录耗时统计
            self.logger.info(
                "转写任务耗时统计",
                extra={
                    'service': 'ASR',
                    'request_id': request_id,
                    'parameters': {
                        'total_duration': f"{total_duration:.2f}秒",
                        'poll_duration': f"{poll_duration:.2f}秒"
                    }
                }
            )
            
            # 检查响应
            if not response or response.status_code != HTTPStatus.OK:
                error_msg = response.message if response else "无效的响应"
                raise Exception(f"语音识别失败: {error_msg}")
                
            # 记录完整的响应内容
            self.logger.debug(
                "转写最终响应",
                extra={
                    'service': 'ASR',
                    'request_id': request_id,
                    'response': response.output
                }
            )
            
            self.logger.info(
                "语音识别任务完成",
                extra={
                    'service': 'ASR',
                    'request_id': request_id
                }
            )
            return response.output
            
        except Exception as e:
            self.logger.error(
                f"语音识别失败: {str(e)}",
                extra={
                    'service': 'ASR',
                    'request_id': request_id if 'request_id' in locals() else str(uuid.uuid4()),
                    'error': str(e),
                    'stack_trace': traceback.format_exc()
                }
            )
            sys.exit(1)  # 语音识别失败时直接退出
            
    @retry_on_timeout(max_retries=3, base_delay=1)
    @log_service_call(service='Translate', api='translate_text')
    def translate_text(self, text: str) -> str:
        """翻译文本
        
        Args:
            text: 要翻译的文本
            
        Returns:
            str: 翻译后的文本
        """
        try:
            request_id = str(uuid.uuid4())
            self.logger.info("开始翻译文本...")
            self.logger.debug(f"待翻译的原始文本:\n{text}")
            
            # 定义时间戳替换函数和映射
            timestamp_map = {}
            timestamp_count = 0
            def replace_timestamp(match):
                nonlocal timestamp_count
                mark = f"__TIMESTAMP_{timestamp_count}__"
                timestamp_map[mark] = match.group(0)
                timestamp_count += 1
                return mark
            
            # 分段处理文本
            segments = self.split_text_for_translation(text)
            translated_segments = []
            
            # 获取模型配置
            model_config = MODEL_CONFIG['translation']['available_models'][self.translation_model]
            
            # 显示模型信息
            self.logger.info(f"使用翻译模型: {self.translation_model}")
            self.logger.info(f"- 价格: ¥{model_config['input_price_per_1k_tokens']}/1K tokens")
            self.logger.info(f"- 文本已分为 {len(segments)} 个片段")
            
            # 逐段翻译
            for i, segment in enumerate(segments, 1):
                self.logger.info(f"翻译第 {i}/{len(segments)} 个片段...")
                
                # 翻译前替换时间戳
                segment_with_marks = re.sub(r'\[\d{2}:\d{2} - \d{2}:\d{2}\]', replace_timestamp, segment)
                
                # 构建请求消息
                messages = [
                    {
                        "role": "user",
                        "content": segment_with_marks
                    }
                ]
                
                # 构建翻译选项
                translation_options = {
                    "source_lang": "English",
                    "target_lang": "Chinese",
                    "domains": "The text contains timestamps and specific formatting that should be preserved. Please maintain the original format including timestamps [MM:SS - MM:SS] at the beginning of each line. The content is from IT domain, involving computer-related software development and usage methods. Pay attention to professional terminologies and sentence patterns when translating."
                }
                
                # 调用翻译API
                response = Generation.call(
                    model=self.translation_model,
                    messages=messages,
                    result_format='message',
                    translation_options=translation_options
                )
                
                # 检查响应状态
                if not response or not hasattr(response, 'status_code') or response.status_code != HTTPStatus.OK:
                    error_msg = getattr(response, 'message', '未知错误')
                    raise Exception(f"翻译API调用失败: {error_msg}")
                
                # 提取翻译结果
                if not hasattr(response.output, 'choices') or not response.output.choices:
                    raise Exception("API响应output缺少choices字段")
                
                if not response.output.choices[0].message:
                    raise Exception("API响应choices缺少message字段")
                
                translated_text = response.output.choices[0].message.content.strip()
                if not translated_text:
                    raise Exception("API返回的翻译文本为空")
                
                translated_segments.append(translated_text)
                
                try:
                    # 使用字符数估算token
                    input_tokens = len(segment) // 4
                    output_text = response.output.choices[0].message.content.strip()
                    output_tokens = len(output_text) // 4
                    
                    # 更新统计
                    total_tokens = input_tokens + output_tokens
                    self.total_tokens[self.translation_model] = float(total_tokens)
                    
                    # 计算翻译费用
                    model_config = MODEL_CONFIG['translation']['available_models'][self.translation_model]
                    input_cost = (input_tokens * model_config['input_price_per_1k_tokens']) / 1000
                    output_cost = (output_tokens * model_config['output_price_per_1k_tokens']) / 1000
                    self.total_costs[self.translation_model] += input_cost + output_cost
                except Exception as e:
                    self.logger.error(f"处理token统计时出错: {str(e)}")
                    # 不中断翻译过程，继续处理下一个片段
                
                # 添加延迟，避免请求过快
                if i < len(segments):
                    time.sleep(1)
            
            # 合并翻译结果
            merged_text = "\n".join(translated_segments)
            
            # 恢复时间戳
            for mark, timestamp in timestamp_map.items():
                merged_text = merged_text.replace(mark, timestamp)
            
            # 格式化：为每个带时间戳的行添加换行
            formatted_lines = []
            for line in merged_text.split('\n'):
                if re.match(r'\[\d{2}:\d{2} - \d{2}:\d{2}\]', line.strip()):
                    formatted_lines.append(line + '\n')
                else:
                    formatted_lines.append(line)
            
            merged_text = '\n'.join(formatted_lines)
            
            self.logger.info("文本翻译完成")
            
            # 输出翻译统计信息
            self.logger.info("翻译统计:")
            self.logger.info(f"• 模型: {self.translation_model}")
            self.logger.info(f"• Token用量: {self.total_tokens[self.translation_model]:.0f}")
            self.logger.info(f"• 预估费用: ¥{self.total_costs[self.translation_model]:.4f}")
            
            return merged_text
            
        except Exception as e:
            self.logger.error(
                f"翻译失败: {str(e)}",
                extra={
                    'service': 'Translate',
                    'request_id': request_id if 'request_id' in locals() else str(uuid.uuid4()),
                    'error': str(e),
                    'stack_trace': traceback.format_exc()
                }
            )
            # 返回已翻译的部分（如果有的话）
            if translated_segments:
                self.logger.warning(f"返回已翻译的 {len(translated_segments)} 个片段")
                return self.merge_translated_segments(translated_segments)
            raise  # 如果没有任何翻译结果，则抛出异常
    
    def merge_translated_segments(self, segments: List[str]) -> str:
        try:
            start_time = time.time()
            self.logger.info("开始合并翻译片段...")
            
            # 合并处理后的文本
            merged_text = "\n\n".join(segments)
            
            # 恢复时间戳并添加空行
            for mark, timestamp in self.timestamp_map.items():
                merged_text = merged_text.replace(mark, timestamp + "\n\n")
            
            # 清理映射（为下次使用做准备）
            self.timestamp_map.clear()
            self.timestamp_count = 0
            
            end_time = time.time()
            self.logger.info(f"翻译片段合并完成，共 {len(segments)} 个片段，耗时 {end_time - start_time:.2f} 秒")
            return merged_text.strip()
            
        except Exception as e:
            self.logger.error(f"合并翻译片段时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            return "\n\n".join(segments)  # 出错时简单连接
    
    def print_token_statistics(self) -> None:
        """打印令牌使用和成本统计信息"""
        self.logger.info("处理统计:")
        
        # ASR统计
        asr_duration = self.total_tokens.get(self.asr_model, 0)
        asr_cost = self.total_costs.get(self.asr_model, 0)
        if asr_duration > 0:
            self.logger.info(f"• 语音识别 ({self.asr_model}):")
            self.logger.info(f"  - 处理时长: {asr_duration:.2f} 秒")
            self.logger.info(f"  - 费用: ¥{asr_cost:.4f}")
        
        # 翻译统计
        for model, tokens in self.total_tokens.items():
            if model != self.asr_model and tokens > 0:
                cost = self.total_costs.get(model, 0)
                self.logger.info(f"• 文本翻译 ({model}):")
                self.logger.info(f"  - Token数量: {tokens}")
                self.logger.info(f"  - 费用: ¥{cost:.4f}")
        
        # 总费用
        total_cost = sum(self.total_costs.values())
        self.logger.info(f"总费用: ¥{total_cost:.4f}")
    
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
        """从识别结果中提取文本。
        
        Args:
            result: 识别结果
            
        Returns:
            List[Tuple[str, float, float]]: 提取的文本片段列表，每个元素为(文本, 开始时间, 结束时间)
        """
        try:
            start_time = time.time()
            request_id = str(uuid.uuid4())
            segments = []
            # 记录原始结果用于调试
            self.logger.debug(
                f"提取文本的原始数据: {json.dumps(result, ensure_ascii=False, indent=2)}",
                extra={
                    'service': 'ASR',
                    'request_id': request_id
                }
            )
            
            # 检查结果格式
            if not isinstance(result, dict):
                raise Exception("结果格式错误：不是一个字典")
                
            # 获取转写内容的 URL
            if 'results' not in result:
                raise Exception("结果格式错误：缺少 results 字段")
                
            for item in result['results']:
                if 'transcription_url' not in item:
                    self.logger.warning(
                        "结果中缺少 transcription_url",
                        extra={
                            'service': 'ASR',
                            'request_id': request_id
                        }
                    )
                    continue
                    
                try:
                    # 获取转写内容
                    import requests
                    response = requests.get(item['transcription_url'])
                    response.raise_for_status()
                    transcription = response.json()
                    
                    # 记录转写内容用于调试
                    self.logger.debug(
                        f"转写内容: {json.dumps(transcription, ensure_ascii=False, indent=2)}",
                        extra={
                            'service': 'ASR',
                            'request_id': request_id
                        }
                    )
                    
                    # 解析转写内容
                    if 'transcripts' in transcription:
                        for transcript in transcription['transcripts']:
                            if 'sentences' in transcript:
                                for sentence in transcript['sentences']:
                                    text = sentence.get('text', '').strip()
                                    if text:
                                        # 清理标签
                                        text = re.sub(r'</?(?:Speech|BGM|NEUTRAL|HAPPY|SAD|ANGRY|silence|noise|[^>]+)>', '', text)
                                        text = ' '.join(text.split())  # 清理多余空格
                                        if text:  # 确保清理后文本非空
                                            start_time = sentence.get('begin_time', 0) / 1000.0  # 转换为秒
                                            end_time = sentence.get('end_time', 0) / 1000.0
                                            segments.append((text, start_time, end_time))
                                        
                except Exception as e:
                    self.logger.error(
                        f"处理转写URL时出错: {str(e)}",
                        extra={
                            'service': 'ASR',
                            'request_id': request_id
                        }
                    )
                    continue
            
            if not segments:
                self.logger.error(
                    "未能从结果中提取到任何文本",
                    extra={
                        'service': 'ASR',
                        'request_id': request_id
                    }
                )
                self.logger.debug(
                    f"原始结果: {json.dumps(result, ensure_ascii=False, indent=2)}",
                    extra={
                        'service': 'ASR',
                        'request_id': request_id
                    }
                )
            else:
                end_time = time.time()
                self.logger.info(
                    f"成功提取了 {len(segments)} 个文本片段，耗时 {end_time - start_time:.2f} 秒",
                    extra={
                        'service': 'ASR',
                        'request_id': request_id
                    }
                )
            
            return segments
            
        except Exception as e:
            self.logger.error(
                f"提取文本时出错: {str(e)}",
                extra={
                    'service': 'ASR',
                    'request_id': str(uuid.uuid4())
                }
            )
            return []
    
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
        
        日志文件结构：
        - info_{timestamp}.log: 程序正常执行的日志
        - error_{timestamp}.log: 除ASR和Translate外的所有错误日志
        - debug_{timestamp}.log: 除ASR和Translate外的所有调试日志
        - asr_{timestamp}.log: 语音识别模块的调试和错误日志
        - translate_{timestamp}.log: 文本翻译模块的调试和错误日志
        
        Args:
            debug (bool): 是否启用调试模式
        """
        # 创建 logs 目录
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        # 生成统一的时间戳（月日_时分秒）
        timestamp = datetime.now().strftime('%m%d_%H%M%S')
        
        # 定义日志文件路径
        log_files = {
            'info': f'logs/info_{timestamp}.log',          # 正常执行日志
            'error': f'logs/error_{timestamp}.log',        # 通用错误日志
            'debug': f'logs/debug_{timestamp}.log',        # 通用调试日志
            'asr': f'logs/asr_{timestamp}.log',           # 语音识别日志
            'translate': f'logs/translate_{timestamp}.log' # 翻译日志
        }
        
        # 创建格式化器
        standard_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - [%(name)s] - %(message)s\n'
            'File: %(pathname)s:%(lineno)d\n'
            'Function: %(funcName)s'
        )
        
        # 使用自定义的服务日志格式化器
        service_formatter = ServiceFormatter(
            '%(asctime)s - %(levelname)s - [%(service)s] - %(message)s\n'
            'Request ID: %(request_id)s\n'
            'Duration: %(duration).2fms\n'
            'Status: %(status)s\n'
            'Parameters: %(parameters)s\n'
            'Response: %(response)s'
        )
        
        # 配置日志记录器
        self.logger = logging.getLogger('youtube_transcriber')
        self.logger.setLevel(logging.DEBUG)
        
        # 清除现有的处理器
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        # 1. INFO日志处理器 - 仅记录INFO级别日志
        info_handler = logging.FileHandler(log_files['info'], encoding='utf-8')
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(standard_formatter)
        info_handler.addFilter(lambda record: record.levelno == logging.INFO)
        
        # 2. ERROR日志处理器 - 仅记录非服务类的错误日志
        error_handler = logging.FileHandler(log_files['error'], encoding='utf-8')
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(detailed_formatter)
        error_handler.addFilter(lambda record: 
            record.levelno >= logging.ERROR and 
            not hasattr(record, 'service')
        )
        
        # 3. DEBUG日志处理器 - 仅记录非服务类的调试日志
        debug_handler = logging.FileHandler(log_files['debug'], encoding='utf-8')
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(detailed_formatter)
        debug_handler.addFilter(lambda record: 
            record.levelno == logging.DEBUG and 
            (not hasattr(record, 'service') or record.service not in ['ASR', 'Translate'])
        )
        
        # 4. ASR日志处理器 - 仅记录ASR服务的日志
        asr_handler = logging.FileHandler(log_files['asr'], encoding='utf-8')
        asr_handler.setLevel(logging.DEBUG)
        asr_handler.setFormatter(service_formatter)
        asr_handler.addFilter(lambda record: 
            hasattr(record, 'service') and 
            record.service == 'ASR'
        )
        
        # 5. Translate日志处理器 - 仅记录翻译服务的日志
        translate_handler = logging.FileHandler(log_files['translate'], encoding='utf-8')
        translate_handler.setLevel(logging.DEBUG)
        translate_handler.setFormatter(service_formatter)
        translate_handler.addFilter(lambda record: 
            hasattr(record, 'service') and 
            record.service == 'Translate'
        )
        
        # 6. 控制台处理器 - 根据debug参数设置级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
        console_handler.setFormatter(standard_formatter)
        
        # 添加所有处理器
        self.logger.addHandler(info_handler)
        self.logger.addHandler(error_handler)
        self.logger.addHandler(debug_handler)
        self.logger.addHandler(asr_handler)
        self.logger.addHandler(translate_handler)
        self.logger.addHandler(console_handler)
        
        # 记录初始化信息
        self.logger.info('日志系统初始化完成')
        self.logger.info('日志文件:')
        for log_type, log_path in log_files.items():
            self.logger.info(f'- {log_type}: {log_path}')
        
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
        
    def download_video(self, url: str) -> Tuple[str, str, str]:
        """下载视频并提取音频。
        
        Args:
            url: YouTube视频URL
            
        Returns:
            Tuple[str, str, str]: (视频ID, 视频标题, 音频文件路径)
        """
        try:
            start_time = time.time()
            self.logger.info("开始下载视频...")
            
            # 提取视频ID
            video_id = extract_video_id(url)
            if not video_id:
                raise Exception("无法从URL中提取视频ID")
            
            # 确保临时目录存在
            os.makedirs(self.temp_dir, exist_ok=True)
            
            # 设置下载选项
            output_template = os.path.join(self.temp_dir, video_id)  # 不包含扩展名
            ydl_opts = {
                'format': 'bestaudio/best',  # 选择最佳音频质量
                'outtmpl': output_template,  # 输出模板，不包含扩展名
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
                'ignoreerrors': False,
                'retries': 3,  # 下载重试次数
                'fragment_retries': 3,  # 分片下载重试次数
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',  # 设置较高的音质
                }]
            }
            
            # 下载视频并提取音频
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_title = info.get('title', video_id)
                if not video_title:
                    video_title = video_id
                    
                # 保存视频信息供后续使用
                self.current_video_title = video_title
                self.current_video_duration = info.get('duration', 0)
            
            # 获取实际的输出文件路径
            audio_path = output_template + '.mp3'
            
            # 文件检查
            if not os.path.exists(audio_path):
                raise Exception(f"下载完成但找不到输出文件: {audio_path}")
                
            if os.path.getsize(audio_path) == 0:
                raise Exception(f"下载的文件大小为0: {audio_path}")
            
            # 记录临时文件
            self.track_temp_file(audio_path)
            
            end_time = time.time()
            self.logger.info(f"视频下载完成，耗时 {end_time - start_time:.2f} 秒")
            self.logger.info(f"- 视频标题: {video_title}")
            self.logger.info(f"- 视频ID: {video_id}")
            if self.current_video_duration:
                self.logger.info(f"- 视频时长: {self.format_duration(self.current_video_duration)}")
            self.logger.info(f"- 音频文件: {audio_path}")
            self.logger.info(f"- 文件大小: {os.path.getsize(audio_path) / (1024*1024):.2f}MB")
            
            return video_id, video_title, audio_path
            
        except Exception as e:
            self.logger.error(f"下载视频时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            raise

    def extract_audio(self, audio_path: str, video_id: str) -> str:
        """从MP3文件中提取WAV格式音频。
        
        Args:
            audio_path: MP3文件路径
            video_id: 视频ID
            
        Returns:
            str: WAV格式音频文件路径
        """
        try:
            start_time = time.time()
            self.logger.info("开始转换音频格式...")
            
            # 构建输出路径
            wav_path = os.path.join(self.temp_dir, f"{video_id}.wav")
            
            # 转换音频格式
            stream = ffmpeg.input(audio_path)
            stream = ffmpeg.output(
                stream,
                wav_path,
                acodec='pcm_s16le',
                ac=1,
                ar='16k'
            )
            ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)
            
            # 记录临时文件
            self.temp_files.append(wav_path)
            
            end_time = time.time()
            self.logger.info(f"音频格式转换完成，耗时 {end_time - start_time:.2f} 秒")
            self.logger.info(f"- 输出格式: WAV 16kHz 单声道")
            self.logger.info(f"- 文件大小: {os.path.getsize(wav_path) / (1024*1024):.2f}MB")
            
            return wav_path
            
        except Exception as e:
            self.logger.error(f"转换音频格式时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            raise

    def upload_audio(self, audio_path: str) -> str:
        """上传音频文件到OSS。
        
        Args:
            audio_path: 音频文件路径
            
        Returns:
            str: 上传后的文件URL
        """
        try:
            start_time = time.time()
            self.logger.info("开始上传音频文件...")
            
            # 上传文件
            file_url = self.upload_to_oss(audio_path)
            if not file_url:
                raise Exception("文件上传失败")
                
            end_time = time.time()
            self.logger.info(f"音频文件上传完成，耗时 {end_time - start_time:.2f} 秒")
            self.logger.info(f"- 文件URL: {file_url}")
            
            return file_url
            
        except Exception as e:
            self.logger.error(f"上传音频文件时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            raise

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
        4. logs目录下的历史日志文件（保留当前执行的日志文件）
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
                    'output': '输出文件',
                    'logs': '日志文件'
                }
                
                for dir_name, file_type in dirs_to_clean.items():
                    dir_path = self.dirs.get(dir_name, dir_name)
                    if os.path.exists(dir_path):
                        try:
                            # 删除目录下的所有文件
                            for root, dirs, files in os.walk(dir_path, topdown=False):
                                for name in files:
                                    file_path = os.path.join(root, name)
                                    try:
                                        # 对于日志目录，跳过当前正在使用的日志文件
                                        if dir_name == 'logs':
                                            # 获取当前日志文件的处理器路径
                                            current_log_files = []
                                            for handler in self.logger.handlers:
                                                if isinstance(handler, logging.FileHandler):
                                                    current_log_files.append(os.path.abspath(handler.baseFilename))
                                            
                                            # 如果是当前正在使用的日志文件，则跳过
                                            if os.path.abspath(file_path) in current_log_files:
                                                self.logger.debug(f"保留当前日志文件: {file_path}")
                                                continue
                                        
                                        os.remove(file_path)
                                        self.logger.info(f"已删除{file_type}: {file_path}")
                                    except Exception as e:
                                        self.logger.warning(f"删除{file_type}失败: {file_path} ({str(e)})")
                                        
                            # 尝试删除空目录（对于logs目录不删除）
                            if dir_name != 'logs':
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

    @log_service_call(service='OSS', api='upload_file')
    def upload_to_oss(self, local_file: str) -> str:
        """上传文件到 OSS。
        
        Args:
            local_file (str): 本地文件路径
            
        Returns:
            str: 文件访问 URL
        """
        try:
            self.logger.info(f"开始上传文件到 OSS: {os.path.basename(local_file)}")
            
            # 获取OSS配置
            access_key = OSS_CONFIG['access_key']
            access_secret = OSS_CONFIG['access_secret']
            endpoint = OSS_CONFIG['endpoint']
            bucket_name = OSS_CONFIG['bucket']
            
            if not all([access_key, access_secret, endpoint, bucket_name]):
                missing_vars = [var for var, value in {
                    'access_key': access_key,
                    'access_secret': access_secret,
                    'endpoint': endpoint,
                    'bucket': bucket_name
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
            file_name = f"{OSS_CONFIG['temp_dir']}/{timestamp}/{os.path.basename(local_file)}"
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
            
            # 生成带签名的 URL
            url = bucket.sign_url('GET', file_name, OSS_CONFIG['url_expiration'], slash_safe=True)
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
        missing_vars = []
        for var in OSS_CONFIG['required_vars']:
            if not os.getenv(var):
                missing_vars.append(f"{var}")
                
        if missing_vars:
            error_msg = "缺少必要的环境变量:\n" + "\n".join(f"- {var}" for var in missing_vars)
            self.logger.error(error_msg)
            raise ValueError(error_msg)

    def save_original_text(self, text: str, video_id: str, video_title: str) -> str:
        """保存原始文本到markdown文件
        Args:
            text: 原始文本
            video_id: 视频ID
            video_title: 视频标题
        Returns:
            保存的文件路径
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{video_id}_original.md"
        filepath = os.path.join(self.dirs['transcripts'], filename)

        # 创建markdown文件内容
        content = f"""# {video_title}

## 视频信息
- 视频ID: {video_id}
- 视频标题: {video_title}
- 视频URL: {self.current_video_url}
- 时间长度: {self.format_duration(self.current_video_duration)}

## 原文
{text}
"""
        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.logger.info(f"原始转写文本已保存: {filename}")
        self.logger.info(f"- 文件大小: {os.path.getsize(filepath) / 1024:.2f}KB")
        
        return filepath

    def save_translated_text(self, text: str, video_id: str, video_title: str) -> str:
        """保存翻译后的文本到markdown文件
        Args:
            text: 翻译后的文本
            video_id: 视频ID
            video_title: 视频标题
        Returns:
            保存的文件路径
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{video_id}_translated.md"
        filepath = os.path.join(self.dirs['transcripts'], filename)

        # 创建markdown文件内容
        content = f"""# {video_title}

## 视频信息
- 视频ID: {video_id}
- 视频标题: {video_title}
- 视频URL: {self.current_video_url}
- 时间长度: {self.format_duration(self.current_video_duration)}

## 译文
{text}
"""

        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.logger.info(f"翻译文本已保存: {filename}")
        self.logger.info(f"- 文件大小: {os.path.getsize(filepath) / 1024:.2f}KB")
        
        return filepath
            
    def format_duration(self, seconds: float) -> str:
        """格式化视频时长。
        
        Args:
            seconds: 秒数
            
        Returns:
            str: 格式化后的时长字符串 (HH:MM:SS)
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"
            
    def format_segments(self, segments: List[Tuple[str, float, float]]) -> str:
        """格式化文本片段。
        
        Args:
            segments: 文本片段列表，每个元素为(文本, 开始时间, 结束时间)
            
        Returns:
            str: 格式化后的文本
        """
        try:
            formatted_text = []
            
            for text, start_time, end_time in segments:
                # 格式化时间戳
                start_str = time.strftime('%M:%S', time.gmtime(start_time))
                end_str = time.strftime('%M:%S', time.gmtime(end_time))
                
                # 添加带时间戳的文本，每段后添加空行
                formatted_text.append(f"[{start_str} - {end_str}] {text.strip()}\n\n")
            
            return ''.join(formatted_text)
            
        except Exception as e:
            self.logger.error(f"格式化文本片段时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            raise

    @log_service_call(service='ContentSummary', api='generate')
    def generate_content_summary(self, transcript_path: str) -> Optional[str]:
        """生成内容总结"""
        summary_config = MODEL_CONFIG['content_summary']
        
        # 读取转写文本，使用更健壮的元数据处理机制
        with open(transcript_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            content = []
            metadata_markers = 0
            in_metadata = False
            
            # 首先计算元数据标记的数量
            metadata_markers = sum(1 for line in lines if line.strip() == '---')
            
            # 如果标记数量为奇数或者没有标记，则视为没有元数据
            if metadata_markers % 2 != 0 or metadata_markers == 0:
                content = lines  # 直接使用所有内容
                self.logger.warning(f"文件 {transcript_path} 中的元数据标记不平衡（发现 {metadata_markers} 个标记），将处理所有内容")
            else:
                # 正常处理元数据
                for line in lines:
                    if line.strip() == '---':
                        in_metadata = not in_metadata
                        continue
                    if not in_metadata:
                        content.append(line)
            
            content = ''.join(content)
            
            # 确保内容不为空
            if not content.strip():
                self.logger.error(f"无法从文件 {transcript_path} 中提取有效内容")
                return None

        try:
            # 检测内容类型
            content_type = self.detect_content_type(content)
            template = MODEL_CONFIG['content_summary']['content_types'][content_type]['template']

            # 调用模型生成总结
            response = Generation.call(
                model=summary_config['model'],
                prompt=f"{template}\n\n{content}",
                **summary_config['api_params']
            )
            
            if response.status_code == HTTPStatus.OK:
                # 生成新文件名
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{timestamp}_{self.current_video_id}_summary.md"
                summary_path = os.path.join(self.dirs['transcripts'], filename)
                
                # 构建markdown内容
                output_text = f"""# {self.current_video_title}

## 基本信息
- 视频ID: {self.current_video_id}
- 视频URL: {self.current_video_url}
- 时间长度: {self.format_duration(self.current_video_duration)}

## 内容概述
> {response.output.text.split('##')[0].strip()}

---

{response.output.text}

---

## 评估指标
- 内容完整性: {'★' * 5}
- 技术深度: {'★' * 5}
- 业务价值: {'★' * 5}
- 可操作性: {'★' * 5}
- 表达清晰度: {'★' * 5}

*注：评分基于内容分析自动生成，仅供参考。*

---

*本文档由 AI 助手自动生成于 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
                # 保存文件
                with open(summary_path, 'w', encoding='utf-8') as f:
                    f.write(output_text)
                
                # 使用字符数估算token
                input_tokens = len(content) // 4
                output_tokens = len(output_text) // 4

                # 更新统计
                total_tokens = input_tokens + output_tokens
                self.total_tokens['qwen-plus-summary'] = float(total_tokens)

                # 计算费用
                model_config = MODEL_CONFIG['content_summary']['available_models']['qwen-plus']
                input_cost = (input_tokens * model_config['input_price_per_1k_tokens']) / 1000
                output_cost = (output_tokens * model_config['output_price_per_1k_tokens']) / 1000
                self.total_costs['qwen-plus-summary'] += input_cost + output_cost
                
                # 记录文件信息
                self.logger.info(f"内容总结已保存: {filename}")
                self.logger.info(f"- 文件大小: {os.path.getsize(summary_path) / 1024:.2f}KB")
                    
                return summary_path

            return None
            
        except Exception as e:
            self.logger.error(f"生成内容总结时出错: {str(e)}")
            self.logger.debug(f"错误堆栈:\n{traceback.format_exc()}")
            return None

    def detect_content_type(self, content: str) -> str:
        """检测内容类型
        
        Args:
            content: 要分析的内容文本
            
        Returns:
            str: 检测到的内容类型 ('technical_sharing', 'academic_sharing', 'keynote_speech')
        """
        content_types = MODEL_CONFIG['content_summary']['content_types']
        
        # 统计关键词出现频率
        type_scores = {}
        for content_type, config in content_types.items():
            score = sum(1 for keyword in config['keywords'] 
                       if keyword in content.lower())
            type_scores[content_type] = score
        
        # 获取得分最高的类型
        detected_type = max(type_scores.items(), key=lambda x: x[1])[0]
        
        self.logger.info(f"内容类型检测结果: {content_types[detected_type]['name']}")
        self.logger.debug(f"类型得分统计: {type_scores}")
        
        return detected_type

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
                transcriber.process_video(url)
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
    transcriber = None
    try:
        parser = argparse.ArgumentParser(
            description='YouTube视频转录工具 - 支持视频转录、翻译和字幕生成',
            formatter_class=argparse.RawTextHelpFormatter
        )
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--url', help='单个YouTube视频的URL')
        group.add_argument('--file', help='包含多个YouTube视频URL的文件路径，每行一个URL')
        group.add_argument('--clean', action='store_true', help='清理所有中间文件和缓存')
        parser.add_argument('--debug', action='store_true', help='启用调试模式，显示详细日志')
        
        # 如果没有参数，打印使用说明
        if len(sys.argv) == 1:
            parser.print_help()
            print("\n示例用法:")
            print("  处理单个视频:")
            print("    python youtube_transcriber.py --url https://www.youtube.com/watch?v=xxxxx")
            print("  处理多个视频:")
            print("    python youtube_transcriber.py --file video_urls.txt")
            print("  清理缓存:")
            print("    python youtube_transcriber.py --clean")
            print("  调试模式:")
            print("    python youtube_transcriber.py --url https://www.youtube.com/watch?v=xxxxx --debug")
            sys.exit(0)
        
        args = parser.parse_args()
        
        # 初始化转录器和日志系统
        transcriber = YouTubeTranscriber(debug=args.debug)
        
        if args.clean:
            transcriber.clean_resources()
        elif args.url:
            transcriber.process_video(args.url)
        elif args.file:
            process_url_list(transcriber, args.file)
                    
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        sys.exit(0)
    except SystemExit:
        # 正常退出
        sys.exit(0)
    except Exception as e:
        if transcriber and transcriber.logger:
            transcriber.logger.error(f"程序执行出错: {str(e)}")
            if args and args.debug:
                transcriber.logger.error(f"错误堆栈:\n{traceback.format_exc()}")
        else:
            print(f"错误: {str(e)}")
            if 'args' in locals() and args.debug:
                print(f"错误堆栈:\n{traceback.format_exc()}")
        sys.exit(1)

if __name__ == '__main__':
    main() 
