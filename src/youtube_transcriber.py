import os
import uuid
import time
import base64
import requests
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

# 加载 .env 文件
load_dotenv()

class YouTubeTranscriber:
    """YouTube视频音频提取和语音识别工具"""
    
    # 文本美化的提示词
    POLISH_SYSTEM_PROMPT = """你是一个专业的文本编辑器。你的任务是优化文本格式，使其更易阅读。
要求：
1. 去掉所有标签（如<Speech>、<BGM>、<NEUTRAL>等）
2. 保持原有的口语表达和内容不变
3. 合理划分段落，使文本结构清晰
4. 修正标点符号，使用中文标点
5. 直接输出优化后的文本，不要添加任何解释或说明"""

    POLISH_USER_PROMPT = """请优化以下文本的格式：

{text}

注意：
1. 去掉所有<Speech>、<BGM>、<NEUTRAL>等标签
2. 保持原有的口语表达和内容不变
3. 直接输出优化后的文本，不要添加任何解释"""

    # 翻译的提示词
    TRANSLATE_SYSTEM_PROMPT = """你是一个专业的翻译引擎。你的任务是将英文文本翻译成中文。
要求：
1. 保持专业、客观的翻译风格
2. 直接输出翻译结果，不要添加任何额外的说明文字
3. 准确传达原文的意思，避免添加或删减内容
4. 使用规范的中文表达
5. 保持原文的段落结构
6. 对于专业术语，保持其专业性和准确性"""

    TRANSLATE_USER_PROMPT = """请将以下文本翻译成中文：

{text}

要求：
1. 保持专业、客观的翻译风格
2. 直接输出翻译结果
3. 准确传达原文的意思
4. 使用规范的中文表达"""

    # Token 价格（元/1K tokens）
    PRICE_PER_1K_TOKENS = {
        'qwen-plus': 0.1,  # 通义千问-Plus 模型价格
        'qwen-turbo': 0.008,  # 通义千问-Turbo 模型价格
        'qwen-max': 0.2,  # 通义千问-Max 模型价格
        'sensevoice-v1': 0.0015  # 语音识别价格（元/秒）
    }

    def __init__(self):
        """初始化转录器"""
        # 从环境变量获取API密钥
        self.api_key = os.getenv('DASHSCOPE_API_KEY')
        if not self.api_key:
            raise ValueError("请设置环境变量 DASHSCOPE_API_KEY")
            
        # 从环境变量获取OSS配置
        self.oss_access_key = os.getenv('OSS_ACCESS_KEY')
        self.oss_access_secret = os.getenv('OSS_ACCESS_SECRET')
        self.oss_endpoint = os.getenv('OSS_ENDPOINT')
        self.oss_bucket = os.getenv('OSS_BUCKET')
        
        if not all([self.oss_access_key, self.oss_access_secret, self.oss_endpoint, self.oss_bucket]):
            raise ValueError("请设置OSS相关的环境变量：OSS_ACCESS_KEY, OSS_ACCESS_SECRET, OSS_ENDPOINT, OSS_BUCKET")
        
        # 设置 API Key
        dashscope.api_key = self.api_key
        
        # 初始化OSS客户端
        self.auth = oss2.Auth(self.oss_access_key, self.oss_access_secret)
        self.bucket = oss2.Bucket(self.auth, self.oss_endpoint, self.oss_bucket)
        
        # 初始化 Token 统计
        self.total_tokens = {
            'qwen-plus': 0,  # 通义千问-Plus 模型使用的 tokens
            'qwen-turbo': 0,  # 通义千问-Turbo 模型使用的 tokens
            'qwen-max': 0,  # 通义千问-Max 模型使用的 tokens
            'sensevoice-v1': 0  # 语音识别使用的时长（秒）
        }
        
        # 当前处理的音频文件路径
        self.current_audio_file = None
        
        # 创建输出目录
        self.output_dir = "outputs"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        # 生成10位时间戳 (MMDDHHMMSS)
        self.timestamp = time.strftime("%m%d%H%M%S")
        
        # 临时文件列表
        self.temp_files = []
        
        # Token 使用预警阈值（元）
        self.cost_warning_threshold = 5.0
        
        # 进度信息
        self.start_time = None
        self.progress = {
            'total_steps': 7,
            'current_step': 0,
            'step_name': '',
            'sub_progress': 0.0
        }

    def get_headers(self, request_id: str = None) -> dict:
        """生成请求头
        Args:
            request_id: 请求ID，如果为None则生成新的UUID
        Returns:
            dict: 请求头
        """
        if request_id is None:
            request_id = str(uuid.uuid4())
            
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def is_valid_audio_file(self, file_path: str) -> bool:
        """检查音频文件是否有效且完整
        Args:
            file_path: 音频文件路径
        Returns:
            bool: 文件是否有效
        """
        try:
            # 检查文件是否存在
            if not os.path.exists(file_path):
                return False
                
            # 检查文件大小是否大于0
            if os.path.getsize(file_path) == 0:
                return False
                
            # 尝试打开并读取音频文件
            audio = AudioSegment.from_wav(file_path)
            
            # 检查音频时长是否大于0
            if len(audio) == 0:
                return False
                
            return True
        except Exception:
            return False
    
    def extract_audio(self, video_url: str) -> str:
        """从YouTube视频中提取音频"""
        try:
            # 首先获取视频ID
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(video_url, download=False)
                video_id = info['id']
                video_title = info.get('title', 'unknown')
                video_duration = info.get('duration', 0)  # 视频时长（秒）
                audio_file = f"audio_{video_id}.wav"
            
            print(f"→ 视频信息:")
            print(f"  • 标题: {video_title}")
            print(f"  • 时长: {video_duration//60}分{video_duration%60}秒")
            
            # 检查本地是否已存在可用的音频文件
            if self.is_valid_audio_file(audio_file):
                audio = AudioSegment.from_wav(audio_file)
                file_size = os.path.getsize(audio_file)
                print(f"✓ 使用已有音频文件:")
                print(f"  • 文件大小: {file_size/1024/1024:.2f}MB")
                print(f"  • 音频时长: {len(audio)/1000:.2f}秒")
                print(f"  • 采样率: {audio.frame_rate}Hz")
                print(f"  • 声道数: {audio.channels}")
                return audio_file
            else:
                # 如果文件存在但无效，则删除
                if os.path.exists(audio_file):
                    print(f"→ 发现无效音频文件，将重新下载")
                    os.remove(audio_file)
            
            print("→ 开始下载并提取音频...")
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
                'outtmpl': 'audio_%(id)s.%(ext)s',
                'quiet': True
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
                
                # 下载完成后验证文件
                if not self.is_valid_audio_file(audio_file):
                    raise Exception("音频文件下载或转换失败")
                
                # 打印音频文件信息
                audio = AudioSegment.from_wav(audio_file)
                file_size = os.path.getsize(audio_file)
                print(f"✓ 音频提取完成:")
                print(f"  • 文件大小: {file_size/1024/1024:.2f}MB")
                print(f"  • 音频时长: {len(audio)/1000:.2f}秒")
                print(f"  • 采样率: {audio.frame_rate}Hz")
                print(f"  • 声道数: {audio.channels}")
                return audio_file
                
        except Exception as e:
            # 如果处理过程中出错，清理可能存在的损坏文件
            if os.path.exists(audio_file):
                os.remove(audio_file)
            raise Exception(f"音频提取失败: {str(e)}")
    
    def process_audio(self, input_file: str) -> str:
        """处理音频文件，确保符合API要求"""
        try:
            print("→ 开始处理音频...")
            # 读取原始音频信息
            audio = AudioSegment.from_wav(input_file)
            original_size = os.path.getsize(input_file)
            print(f"→ 原始音频信息:")
            print(f"  • 文件大小: {original_size/1024/1024:.2f}MB")
            print(f"  • 音频时长: {len(audio)/1000:.2f}秒")
            print(f"  • 采样率: {audio.frame_rate}Hz")
            print(f"  • 声道数: {audio.channels}")
            
            # 转换为16kHz采样率
            if audio.frame_rate != 16000:
                print(f"→ 转换采样率: {audio.frame_rate}Hz → 16000Hz")
                audio = audio.set_frame_rate(16000)
            
            # 转换为单声道
            if audio.channels > 1:
                print(f"→ 转换声道: {audio.channels}声道 → 单声道")
                audio = audio.set_channels(1)
            
            output_file = f"{input_file}_processed.wav"
            audio.export(output_file, format="wav")
            
            # 打印处理后的音频信息
            processed_size = os.path.getsize(output_file)
            print(f"✓ 音频处理完成:")
            print(f"  • 文件大小: {processed_size/1024/1024:.2f}MB")
            print(f"  • 音频时长: {len(audio)/1000:.2f}秒")
            print(f"  • 采样率: {audio.frame_rate}Hz")
            print(f"  • 声道数: {audio.channels}")
            print(f"  • 大小变化: {processed_size/original_size*100:.1f}%")
            
            return output_file
            
        except Exception as e:
            raise Exception(f"音频处理失败: {str(e)}")
    
    def split_audio(self, audio_file: str, max_size_mb: int = 400) -> list:
        """将音频文件分割成较小的片段
        Args:
            audio_file: 音频文件路径
            max_size_mb: 每个分片的最大大小（MB），通义千问单次处理限制为500MB
        Returns:
            list: 分片文件路径列表
        """
        try:
            print("正在分割音频...")
            audio = AudioSegment.from_wav(audio_file)
            
            # 获取音频总时长（毫秒）和文件大小
            total_duration = len(audio)
            file_size = os.path.getsize(audio_file)
            
            # 如果文件小于最大限制，直接返回原文件
            if file_size <= max_size_mb * 1024 * 1024:
                print(f"音频文件大小在限制范围内，无需分片")
                return [audio_file]
            
            # 计算需要的分片数量（向上取整）
            num_chunks = (file_size + (max_size_mb * 1024 * 1024) - 1) // (max_size_mb * 1024 * 1024)
            
            # 计算每个分片的时长
            chunk_duration = total_duration // num_chunks
            
            print(f"音频总时长: {total_duration/1000:.2f}秒, 文件大小: {file_size/1024/1024:.2f}MB")
            print(f"将分割成 {num_chunks} 个片段，每个片段约 {chunk_duration/1000:.2f}秒")
            
            # 分割音频
            chunks = []
            for i in range(num_chunks):
                start = i * chunk_duration
                end = total_duration if i == num_chunks - 1 else (i + 1) * chunk_duration
                
                chunk = audio[start:end]
                chunk_file = f"{audio_file}_chunk_{i}.wav"
                chunk.export(chunk_file, format="wav")
                
                # 验证分片大小
                chunk_size = os.path.getsize(chunk_file) / 1024 / 1024
                print(f"分片 {i+1} 大小: {chunk_size:.2f}MB")
                
                if chunk_size > max_size_mb:
                    raise Exception(f"分片 {i+1} 超出大小限制: {chunk_size:.2f}MB > {max_size_mb}MB")
                
                chunks.append(chunk_file)
            
            return chunks
            
        except Exception as e:
            # 清理已生成的分片
            try:
                for chunk_file in chunks:
                    if os.path.exists(chunk_file):
                        os.remove(chunk_file)
            except:
                pass
            raise Exception(f"音频分割失败: {str(e)}")
    
    def merge_texts(self, texts: list) -> str:
        """合并多个文本片段，并进行后处理
        Args:
            texts: 文本片段列表
        Returns:
            str: 合并后的文本
        """
        try:
            print("正在合并文本片段...")
            
            # 1. 基础合并
            merged_text = ""
            for i, text in enumerate(texts):
                # 去除每个片段首尾的空白字符
                text = text.strip()
                
                # 处理标点符号
                if i > 0:
                    # 检查上一个片段的结尾和当前片段的开头
                    prev_text = texts[i-1].strip()
                    if not prev_text.endswith(('。', '！', '？', '；', '.', '!', '?', ';')):
                        # 如果上一个片段没有结束标点，添加一个分隔符
                        merged_text += "，"
                
                # 添加当前文本片段
                merged_text += text
            
            # 2. 后处理
            # 移除重复的标点符号
            merged_text = merged_text.replace('。。', '。')
            merged_text = merged_text.replace('，，', '，')
            merged_text = merged_text.replace('！！', '！')
            merged_text = merged_text.replace('？？', '？')
            
            # 确保句子有合适的结束符
            if not merged_text.endswith(('。', '！', '？', '；', '.', '!', '?', ';')):
                merged_text += '。'
            
            return merged_text
            
        except Exception as e:
            raise Exception(f"文本合并失败: {str(e)}")
    
    def upload_to_oss(self, local_file: str) -> str:
        """上传文件到OSS"""
        try:
            print("→ 上传文件中...")
            file_name = f"audio/{str(uuid.uuid4())}/{os.path.basename(local_file)}"
            
            with open(local_file, 'rb') as f:
                self.bucket.put_object(file_name, f)
            
            url = self.bucket.sign_url('GET', file_name, 24 * 3600)
            
            print("✓ 上传成功:")
            print(f"  • 存储位置: {self.oss_bucket}/{file_name}")
            print(f"  • 文件大小: {os.path.getsize(local_file)/1024/1024:.2f}MB")
            print(f"  • URL有效期: 24小时")
            
            return url
            
        except Exception as e:
            raise Exception(f"上传失败: {str(e)}")
    
    def process_video(self, video_url: str, output_file: str, resume_timestamp: str = None):
        """处理完整的视频转录流程
        Args:
            video_url: YouTube视频链接
            output_file: 输出文件路径
            resume_timestamp: 恢复处理的时间戳
        """
        try:
            # 尝试恢复之前的状态
            if resume_timestamp and self.load_state(resume_timestamp):
                print(f"\n=== 恢复处理 ({resume_timestamp}) ===")
            else:
                print("\n=== 开始处理视频 ===")
                self.start_time = time.time()
            
            print(f"视频链接: {video_url}")
            
            # 创建输出目录
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
            
            # 1. 提取音频
            self.update_progress("提取音频")
            print("\n[1/7] 提取音频")
            audio_file = self.extract_audio(video_url)
            self.temp_files.append(audio_file)
            audio_output = os.path.join(self.output_dir, f"extract_{self.timestamp}.wav")
            if os.path.exists(audio_file):
                import shutil
                shutil.copy2(audio_file, audio_output)
                print(f"✓ 原始音频: {audio_output}")
            
            # 保存当前状态
            self.save_state()
            
            # 2. 处理音频
            self.update_progress("处理音频")
            print("\n[2/7] 处理音频")
            processed_file = self.process_audio(audio_file)
            self.temp_files.append(processed_file)
            processed_output = os.path.join(self.output_dir, f"process_{self.timestamp}.wav")
            if os.path.exists(processed_file):
                import shutil
                shutil.copy2(processed_file, processed_output)
                print(f"✓ 处理后音频: {processed_output}")
                self.current_audio_file = processed_file
            
            # 保存当前状态
            self.save_state()
            
            # 3. 上传到OSS
            self.update_progress("上传音频")
            print("\n[3/7] 上传音频")
            file_url = self.upload_to_oss(processed_file)
            
            # 保存当前状态
            self.save_state()
            
            # 4. 语音识别
            self.update_progress("语音识别")
            print("\n[4/7] 语音识别")
            text = self.recognize_speech(file_url)
            recognition_output = os.path.join(self.output_dir, f"recognize_{self.timestamp}.txt")
            with open(recognition_output, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"✓ 识别结果: {recognition_output}")
            
            # 保存当前状态
            self.save_state()
            
            # 5. 翻译文本
            self.update_progress("翻译文本")
            print("\n[5/7] 翻译文本")
            translated_text = self.translate_text(text)
            translation_output = os.path.join(self.output_dir, f"translate_{self.timestamp}.txt")
            with open(translation_output, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print(f"✓ 翻译结果: {translation_output}")
            
            # 保存当前状态
            self.save_state()
            
            # 6. 优化文本
            self.update_progress("优化文本")
            print("\n[6/7] 优化文本")
            polished_text = self.polish_text(translated_text)
            polished_output = os.path.join(self.output_dir, f"polish_{self.timestamp}.txt")
            with open(polished_output, 'w', encoding='utf-8') as f:
                f.write(polished_text)
            print(f"✓ 优化结果: {polished_output}")
            
            # 保存当前状态
            self.save_state()
            
            # 7. 保存最终结果
            self.update_progress("保存结果")
            print("\n[7/7] 保存结果")
            final_output = f"{os.path.splitext(output_file)[0]}_{self.timestamp}.txt"
            with open(final_output, 'w', encoding='utf-8') as f:
                f.write(polished_text)
            print(f"✓ 最终结果: {final_output}")
            
            # 完成处理
            self.update_progress("完成", 1.0)
            print("\n=== 处理完成 ===")
            
            # 打印 Token 使用统计
            print("\n=== Token 使用统计 ===")
            total_cost = 0
            
            # 统计所有使用过的模型费用
            for model, tokens in self.total_tokens.items():
                if model == 'sensevoice-v1':
                    # 语音识别费用
                    audio_cost = tokens * self.PRICE_PER_1K_TOKENS[model]
                    if audio_cost > 0:
                        print(f"语音识别:")
                        print(f"  • 使用量: {tokens:.1f} 秒")
                        print(f"  • 费用: ¥{audio_cost:.4f}")
                        total_cost += audio_cost
                else:
                    # LLM模型费用
                    model_cost = (tokens / 1000) * self.PRICE_PER_1K_TOKENS[model]
                    if tokens > 0:  # 只显示实际使用过的模型
                        print(f"{model}:")
                        print(f"  • 使用量: {tokens:,} tokens")
                        print(f"  • 费用: ¥{model_cost:.4f}")
                        total_cost += model_cost
            
            # 打印总费用和百分比
            if total_cost > 0:
                print(f"\n总费用: ¥{total_cost:.4f}")
                # 显示各项费用占比
                for model, tokens in self.total_tokens.items():
                    if model == 'sensevoice-v1':
                        cost = tokens * self.PRICE_PER_1K_TOKENS[model]
                    else:
                        cost = (tokens / 1000) * self.PRICE_PER_1K_TOKENS[model]
                    if cost > 0:  # 只显示实际产生费用的项目
                        percentage = cost / total_cost * 100
                        print(f"  • {model}: {percentage:.1f}%")
            
            # 检查费用
            self.check_cost_warning()
            
        except Exception as e:
            print(f"\n❌ 处理失败: {str(e)}")
            raise
            
        finally:
            # 清理临时文件
            print("\n→ 清理临时文件...")
            for temp_file in self.temp_files:
                try:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                        print(f"  ✓ 已删除: {temp_file}")
                except Exception as e:
                    print(f"  ⚠️ 删除失败: {temp_file} ({str(e)})")
    
    def api_call_with_retry(self, func, *args, max_retries=3, **kwargs):
        """执行API调用，失败时自动重试
        Args:
            func: 要调用的函数
            max_retries: 最大重试次数
            *args, **kwargs: 传递给函数的参数
        Returns:
            API调用结果
        Raises:
            Exception: 所有重试都失败时抛出异常
        """
        last_error = None
        
        # 如果是 requests 的调用，增加超时时间
        if func == requests.get:
            kwargs['timeout'] = 30  # 设置30秒超时
        
        # 如果是 dashscope 的调用，增加超时时间
        if 'dashscope' in str(func):
            kwargs['timeout'] = 60  # 设置60秒超时
        
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except requests.exceptions.Timeout as e:
                last_error = f"请求超时: {str(e)}"
            except requests.exceptions.ConnectionError as e:
                last_error = f"网络连接错误: {str(e)}"
            except Exception as e:
                last_error = f"API调用错误: {str(e)}"
                
            if attempt < max_retries - 1:  # 如果还有重试机会
                # 使用指数退避策略：2^attempt * 5秒（5s, 10s, 20s）
                wait_time = (2 ** attempt) * 5
                print(f"❌ 第 {attempt + 1} 次调用失败: {last_error}")
                print(f"→ {wait_time} 秒后重试...")
                # 添加随机抖动，避免多个请求同时重试
                jitter = random.uniform(0, 2)
                time.sleep(wait_time + jitter)
            else:
                print(f"❌ 最后一次调用失败: {last_error}")
                raise Exception(last_error)
    
    def check_cost_warning(self):
        """检查费用是否超过预警阈值"""
        total_cost = 0
        
        # 计算各项费用
        qwen_plus_tokens = self.total_tokens.get('qwen-plus', 0)
        qwen_plus_cost = (qwen_plus_tokens / 1000) * self.PRICE_PER_1K_TOKENS['qwen-plus']
        
        qwen_turbo_tokens = self.total_tokens.get('qwen-turbo', 0)
        qwen_turbo_cost = (qwen_turbo_tokens / 1000) * self.PRICE_PER_1K_TOKENS['qwen-turbo']
        
        audio_duration = self.total_tokens.get('sensevoice-v1', 0)
        audio_cost = audio_duration * self.PRICE_PER_1K_TOKENS['sensevoice-v1']
        
        total_cost = qwen_plus_cost + qwen_turbo_cost + audio_cost
        
        if total_cost >= self.cost_warning_threshold:
            print(f"\n⚠️ 费用预警: 当前总费用 ¥{total_cost:.2f} 已超过预警阈值 ¥{self.cost_warning_threshold:.2f}")
            print(f"  • 通义千问-Plus: ¥{qwen_plus_cost:.2f}")
            print(f"  • 通义千问-Turbo: ¥{qwen_turbo_cost:.2f}")
            print(f"  • 语音识别: ¥{audio_cost:.2f}")
            
    def recognize_speech(self, file_url: str) -> str:
        """使用通义千问 SenseVoice API 进行语音识别"""
        try:
            print("→ 提交转写任务...")
            
            # 使用重试机制提交任务
            task_response = self.api_call_with_retry(
                Transcription.async_call,
                model='sensevoice-v1',
                file_urls=[file_url],
                language_hints=['zh'],
                # 添加参数以去除标签
                config={
                    'enable_semantic_sentence_detection': True,  # 启用语义分句
                    'enable_punctuation': True,  # 启用标点
                    'enable_timestamps': False,  # 禁用时间戳
                    'enable_punc': True,  # 启用标点
                    'enable_voice_tags': False,  # 禁用语音标签
                    'enable_noise_tags': False,  # 禁用噪音标签
                    'enable_speaker_info': False  # 禁用说话人信息
                }
            )
            
            if task_response.status_code != HTTPStatus.OK:
                raise Exception(f"提交失败: {task_response.message}")
            
            task_id = task_response.output.task_id
            print(f"✓ 任务已提交 (ID: {task_id})")
            
            print("→ 等待转写结果...")
            # 使用重试机制获取结果
            transcribe_response = self.api_call_with_retry(
                Transcription.wait,
                task=task_id
            )
            
            if transcribe_response.status_code == HTTPStatus.OK:
                transcription_url = transcribe_response.output['results'][0]['transcription_url']
                print("→ 下载转写结果...")
                
                # 使用重试机制下载结果
                text_response = self.api_call_with_retry(requests.get, transcription_url)
                
                if text_response.status_code == 200:
                    text_result = text_response.json()
                    text = text_result['transcripts'][0]['text']
                    
                    # 更新语音识别使用时长（从毫秒转换为秒）
                    duration = float(text_result['duration']) / 1000.0 if 'duration' in text_result else 0
                    if duration == 0:
                        # 如果 duration 字段不存在或为0，尝试从音频文件获取时长
                        try:
                            audio = AudioSegment.from_wav(self.current_audio_file)
                            duration = len(audio) / 1000.0  # 转换为秒
                        except:
                            print("⚠️ 无法获取音频时长，将影响费用统计")
                    
                    self.total_tokens['sensevoice-v1'] = duration
                    print(f"✓ 转写完成 ({duration:.1f} 秒)")
                    
                    # 清理标签
                    text = self.clean_text(text)
                    return text
                else:
                    raise Exception(f"下载失败: {text_response.text}")
            else:
                raise Exception(f"转写失败: {transcribe_response.message}")
            
        except Exception as e:
            raise Exception(f"语音识别失败: {str(e)}")
    
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
        """清理文本中的特殊标记，但保持原有格式
        Args:
            text: 原始文本
        Returns:
            str: 清理后的文本
        """
        # 使用正则表达式清理标签
        tags_pattern = r'</?(?:speech|Speech|bgm|BGM|silence|Silence|noise|Noise|NEUTRAL|neutral|[^>]+)>'
        text = re.sub(tags_pattern, '', text)
        
        # 保持段落格式，只处理多余的空白字符
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            # 清理每行中的多余空白字符，但保持行首和行尾的换行
            cleaned_line = ' '.join(line.split())
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
        
        # 使用两个换行符连接段落，保持段落格式
        return '\n\n'.join(cleaned_lines)
    
    def merge_text_parts(self, parts: list, is_paragraphs: bool = False) -> str:
        """智能合并文本片段
        Args:
            parts: 文本片段列表
            is_paragraphs: 是否按段落格式合并
        Returns:
            str: 合并后的文本
        """
        if not parts:
            return ""
            
        if is_paragraphs:
            # 按段落合并，确保段落之间有空行
            merged = []
            for part in parts:
                # 清理每个段落的首尾空白
                cleaned_part = part.strip()
                if cleaned_part:
                    # 确保每个段落末尾有适当的标点
                    if not cleaned_part[-1] in '。！？；.!?;':
                        cleaned_part += '。'
                    merged.append(cleaned_part)
            return '\n\n'.join(merged)
        else:
            # 按句子合并，确保句子之间有适当的标点
            merged = ""
            for i, part in enumerate(parts):
                cleaned_part = part.strip()
                if not cleaned_part:
                    continue
                    
                if i > 0:
                    # 检查前一个句子的结尾和当前句子的开头
                    if not merged[-1] in '。！？；.!?;' and \
                       not cleaned_part[0] in '。！？；.!?;':
                        merged += "。"
                    elif merged[-1] in '.!?;' and cleaned_part[0] not in '。！？；.!?;':
                        # 将英文标点替换为中文标点
                        merged = merged[:-1] + '。'
                
                merged += cleaned_part
            
            # 确保最后一句有结束标点
            if merged and not merged[-1] in '。！？；.!?;':
                merged += '。'
            
            return merged
    
    def split_text(self, text: str, max_tokens: int = None) -> tuple:
        """智能分割文本
        Args:
            text: 要分割的文本
            max_tokens: 每个片段的最大token数量
        Returns:
            tuple: (segments, is_paragraphs)，分割后的片段列表和是否按段落分割的标志
        """
        # 首先尝试按段落分割
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
        
        # 如果有多个段落，按段落处理
        if len(paragraphs) > 1:
            if max_tokens:
                # 如果指定了max_tokens，需要进一步分割段落
                segments = []
                current_segment = []
                current_tokens = 0
                
                for p in paragraphs:
                    # 估算当前段落的tokens
                    p_tokens = len(p) * 2  # 粗略估计：每个字符平均2个tokens
                    
                    if current_tokens + p_tokens > max_tokens and current_segment:
                        # 当前批次达到限制，保存并开始新批次
                        segments.append('\n'.join(current_segment))
                        current_segment = [p]
                        current_tokens = p_tokens
                    else:
                        current_segment.append(p)
                        current_tokens += p_tokens
                
                # 保存最后一个批次
                if current_segment:
                    segments.append('\n'.join(current_segment))
                
                return segments, True
            else:
                return paragraphs, True
        
        # 如果没有段落分隔，按句子分割
        sentences = []
        current = []
        
        # 更智能的句子分割
        for char in text:
            current.append(char)
            if char in '.!?。！？':
                sentence = ''.join(current).strip()
                # 避免错误分割常见缩写
                if not any(sentence.endswith(abbr) for abbr in [
                    'Mr.', 'Mrs.', 'Dr.', 'Ph.D.', 'U.S.', 'U.K.',
                    'a.m.', 'p.m.', 'i.e.', 'e.g.', 'etc.'
                ]):
                    if sentence:
                        sentences.append(sentence)
                    current = []
        
        # 处理最后一个句子
        if current:
            sentence = ''.join(current).strip()
            if sentence:
                sentences.append(sentence)
        
        if max_tokens:
            # 如果指定了max_tokens，需要进一步分割句子
            segments = []
            current_segment = []
            current_tokens = 0
            
            for s in sentences:
                # 估算当前句子的tokens
                s_tokens = len(s) * 2  # 粗略估计：每个字符平均2个tokens
                
                if current_tokens + s_tokens > max_tokens and current_segment:
                    # 当前批次达到限制，保存并开始新批次
                    segments.append(' '.join(current_segment))
                    current_segment = [s]
                    current_tokens = s_tokens
                else:
                    current_segment.append(s)
                    current_tokens += s_tokens
            
            # 保存最后一个批次
            if current_segment:
                segments.append(' '.join(current_segment))
            
            return segments, False
        else:
            return sentences, False
    
    def polish_text(self, text: str) -> str:
        """使用通义千问优化文本格式
        Args:
            text: 要优化的文本
        Returns:
            str: 优化后的文本
        """
        try:
            print(f"\n[4/4] 正在优化文本格式...")
            
            # 分批处理文本
            batch_size = 4000  # turbo模型的单批次token限制
            batches, _ = self.split_text(text, batch_size)
            polished_parts = []
            
            for i, batch in enumerate(batches, 1):
                print(f"\n→ 正在处理第 {i}/{len(batches)} 批...")
                
                # 调用API优化文本
                response = self.api_call_with_retry(
                    lambda: Generation.call(
                        model='qwen-turbo',
                        prompt=self.POLISH_USER_PROMPT.format(text=batch),
                        system=self.POLISH_SYSTEM_PROMPT,
                        max_tokens=2048,
                        temperature=0.1,
                        top_p=0.1,
                        result_format='message',
                    )
                )
                
                if response.status_code != 200:
                    raise Exception(f"优化请求失败: {response.message}")
                    
                polished = response.output.choices[0]['message']['content'].strip()
                
                # 检查完整性
                if not self.check_polish_completeness(batch, polished):
                    raise Exception("文本优化结果不完整")
                    
                polished_parts.append(polished)
                
                # 更新token统计
                self.total_tokens['qwen-turbo'] = self.total_tokens.get('qwen-turbo', 0) + response.usage['total_tokens']
                
            # 合并所有批次的结果
            final_text = '\n\n'.join(polished_parts)
            
            # 保存优化后的文本
            output_file = os.path.join(self.output_dir, f'5_polished_{self.timestamp}.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_text)
                
            print(f"✓ 文本优化完成，结果已保存到: {output_file}")
            return final_text
            
        except Exception as e:
            print(f"❌ 优化失败: {str(e)}")
            return text  # 如果优化失败，返回原文本
    
    def check_translation_completeness(self, original_text: str, translated_text: str) -> bool:
        """检查翻译结果的完整性，通过比较原文和译文的最后一句话
        Args:
            original_text: 原始文本
            translated_text: 翻译后的文本
        Returns:
            bool: 翻译是否完整
        """
        def get_last_sentence(text: str) -> str:
            # 首先清理文本
            text = self.clean_text(text)
            # 按常见的句子结束符分割
            sentences = []
            current = []
            
            for char in text:
                current.append(char)
                if char in '.!?。！？':
                    sentence = ''.join(current).strip()
                    if sentence:
                        sentences.append(sentence)
                    current = []
            
            # 处理最后一个可能没有结束符的句子
            if current:
                sentence = ''.join(current).strip()
                if sentence:
                    sentences.append(sentence)
            
            # 如果没有找到任何句子，返回整个文本
            if not sentences:
                return text.strip()
            
            return sentences[-1].strip()
        
        # 获取原文和译文的最后一句
        original_last = get_last_sentence(original_text)
        translated_last = get_last_sentence(translated_text)
        
        # 检查原文最后一句是否包含英文内容
        has_english = any(ord(c) < 128 and c.isalpha() for c in original_last)
        if not has_english:
            # 如果原文最后一句没有英文内容，直接返回完整
            return True
        
        # 打印详细的检查信息
        print(f"→ 完整性检查:")
        print(f"  • 原文最后一句: {original_last}")
        print(f"  • 译文最后一句: {translated_last}")
        
        # 检查译文最后一句是否包含中文内容
        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in translated_last)
        is_complete = has_chinese
        
        if not is_complete:
            print(f"⚠️ 检测到翻译可能不完整")
        
        return is_complete

    def translate_text(self, text: str) -> str:
        """使用通义千问翻译英文文本为中文"""
        try:
            # 首先清理特殊标记
            text = self.clean_text(text)
            
            # 检查输入文本长度
            input_length = len(text)
            print(f"→ 输入文本长度: {input_length} 字符")
            
            if not any(ord(c) < 128 for c in text):
                print("✓ 无需翻译（未检测到英文内容）")
                return text
                
            print("→ 翻译中...")
            
            # 估算tokens数量（粗略估计：英文单词约1.3个tokens，中文字符约2个tokens）
            def estimate_tokens(s: str) -> int:
                chinese_chars = sum(1 for c in s if ord(c) > 127)
                english_chars = len(''.join(c for c in s if ord(c) <= 127))
                return int(chinese_chars * 2 + english_chars * 0.25)
            
            # 计算系统提示词和用户提示词模板的基础tokens
            base_tokens = estimate_tokens(self.TRANSLATE_SYSTEM_PROMPT) + \
                         estimate_tokens(self.TRANSLATE_USER_PROMPT.replace("{text}", ""))
            print(f"→ 提示词基础tokens: {base_tokens}")
            
            # 更保守的token限制，避免内容过长导致的错误
            max_text_tokens = 2000 - base_tokens
            max_chars = int(max_text_tokens / 0.25)
            
            def translate_batch(batch_text: str, max_retries: int = 3) -> str:
                """翻译单个批次的文本，带有重试机制"""
                # 首先尝试使用 qwen-plus 模型
                for attempt in range(max_retries):
                    try:
                        # 每次重试使用不同的随机种子和温度
                        temperature = 0.3 - (attempt * 0.1)  # 随着重试次数增加，降低温度
                        response = self.api_call_with_retry(
                            dashscope.Generation.call,
                            model='qwen-plus',
                            messages=[
                                {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                                {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=batch_text)}
                            ],
                            result_format='message',
                            max_tokens=2048,
                            temperature=temperature,
                            top_p=0.95,
                            enable_search=True,
                            seed=random.randint(1, 10000)
                        )
                        
                        if response.status_code == HTTPStatus.OK:
                            self.total_tokens['qwen-plus'] += response.usage.total_tokens
                            result = response.output.choices[0].message.content.strip()
                            print(f"    ✓ 本批使用 qwen-plus: {response.usage.total_tokens} tokens")
                            return result
                        elif "inappropriate content" in response.message.lower():
                            print(f"    ⚠️ qwen-plus 检测到敏感内容，尝试使用 qwen-max...")
                            # 直接跳出循环，尝试使用 qwen-max
                            break
                        else:
                            raise Exception(f"翻译请求失败: {response.message}")
                    except Exception as e:
                        if attempt < max_retries - 1:
                            print(f"    ⚠️ qwen-plus 第 {attempt + 1} 次尝试失败: {str(e)}")
                            time.sleep(2 ** attempt)  # 指数退避
                            continue
                        raise
                
                # 如果 qwen-plus 失败，尝试使用 qwen-max 模型
                print("    → 切换到 qwen-max 模型...")
                for attempt in range(max_retries):
                    try:
                        temperature = 0.3 - (attempt * 0.1)
                        response = self.api_call_with_retry(
                            dashscope.Generation.call,
                            model='qwen-max',
                            messages=[
                                {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                                {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=batch_text)}
                            ],
                            result_format='message',
                            max_tokens=2048,
                            temperature=temperature,
                            top_p=0.95,
                            enable_search=True,
                            seed=random.randint(1, 10000)
                        )
                        
                        if response.status_code == HTTPStatus.OK:
                            # 使用 qwen-max 的 token 统计
                            if 'qwen-max' not in self.total_tokens:
                                self.total_tokens['qwen-max'] = 0
                            self.total_tokens['qwen-max'] += response.usage.total_tokens
                            result = response.output.choices[0].message.content.strip()
                            print(f"    ✓ 本批使用 qwen-max: {response.usage.total_tokens} tokens")
                            return result
                        else:
                            raise Exception(f"翻译请求失败: {response.message}")
                    except Exception as e:
                        if attempt < max_retries - 1:
                            print(f"    ⚠️ qwen-max 第 {attempt + 1} 次尝试失败: {str(e)}")
                            time.sleep(2 ** attempt)
                            continue
                        raise
                
                raise Exception("所有模型和重试都失败了")
            
            # 如果文本太长，需要分段处理
            if input_length > max_chars:
                print(f"→ 文本较长，将分段处理")
                print(f"  • 单次最大处理: {max_chars} 字符（约 {max_text_tokens} tokens）")
                
                # 智能分割文本
                segments, is_paragraphs = self.split_text(text)
                
                translated_parts = []
                current_batch = []
                current_tokens = base_tokens
                
                for segment in segments:
                    segment_tokens = estimate_tokens(segment)
                    
                    # 如果当前段落加上已有内容会超过限制，先处理已有内容
                    if current_tokens + segment_tokens > max_text_tokens and current_batch:
                        # 处理当前批次
                        batch_text = self.merge_text_parts(current_batch, is_paragraphs)
                        print(f"  • 处理第 {len(translated_parts)+1} 批: {len(batch_text)} 字符")
                        
                        try:
                            translated_text = translate_batch(batch_text)
                            translated_parts.append(translated_text)
                        except Exception as e:
                            print(f"    ⚠️ 批次处理失败，尝试更小的分段...")
                            # 如果批次处理失败，尝试逐段处理
                            for small_segment in current_batch:
                                try:
                                    small_translated = translate_batch(small_segment)
                                    translated_parts.append(small_translated)
                                except Exception as sub_e:
                                    print(f"    ❌ 段落处理失败: {str(sub_e)}")
                                    # 如果翻译失败，保留原文
                                    translated_parts.append(small_segment)
                        
                        current_batch = [segment]
                        current_tokens = base_tokens + segment_tokens
                    else:
                        current_batch.append(segment)
                        current_tokens += segment_tokens
                
                # 处理最后一批
                if current_batch:
                    batch_text = self.merge_text_parts(current_batch, is_paragraphs)
                    print(f"  • 处理最后一批: {len(batch_text)} 字符")
                    
                    try:
                        translated_text = translate_batch(batch_text)
                        translated_parts.append(translated_text)
                    except Exception as e:
                        print(f"    ⚠️ 最后批次处理失败，尝试更小的分段...")
                        # 如果批次处理失败，尝试逐段处理
                        for small_segment in current_batch:
                            try:
                                small_translated = translate_batch(small_segment)
                                translated_parts.append(small_translated)
                            except Exception as sub_e:
                                print(f"    ❌ 段落处理失败: {str(sub_e)}")
                                # 如果翻译失败，保留原文
                                translated_parts.append(small_segment)
                
                # 合并所有翻译结果
                translated_text = self.merge_text_parts(translated_parts, is_paragraphs)
                
                # 在分批处理的结果合并后检查完整性
                if not self.check_translation_completeness(text, translated_text):
                    raise Exception("翻译结果不完整")
                
            else:
                print(f"→ 文本长度适中，单次处理")
                estimated_tokens = estimate_tokens(text) + base_tokens
                print(f"  • 预估tokens: {estimated_tokens}")
                
                translated_text = translate_batch(text)
                
                # 检查完整性
                if not self.check_translation_completeness(text, translated_text):
                    raise Exception("翻译结果不完整")
            
            # 检查输出文本长度
            output_length = len(translated_text)
            print(f"✓ 翻译完成:")
            print(f"  • 输入长度: {input_length} 字符")
            print(f"  • 输出长度: {output_length} 字符")
            print(f"  • 长度变化: {output_length/input_length*100:.1f}%")
            
            return translated_text
            
        except Exception as e:
            print(f"❌ 翻译失败: {str(e)}")
            raise  # 翻译失败时抛出异常，中止程序

    def check_polish_completeness(self, original_text: str, polished_text: str) -> bool:
        """检查文本美化结果的完整性
        Args:
            original_text: 原始文本
            polished_text: 美化后的文本
        Returns:
            bool: 美化是否完整
        """
        # 清理标签和空白字符后比较内容
        def clean_for_compare(text: str) -> str:
            # 去除所有标签
            text = re.sub(r'<[^>]+>', '', text)
            # 去除空白字符
            text = ''.join(c for c in text if c not in '\n\r\t ')
            return text
            
        original_clean = clean_for_compare(original_text)
        polished_clean = clean_for_compare(polished_text)
        
        # 打印详细的检查信息
        print(f"→ 完整性检查:")
        print(f"  • 原文实际内容字符数: {len(original_clean)}")
        print(f"  • 美化后内容字符数: {len(polished_clean)}")
        
        # 检查字符数量（允许5%的浮动）
        length_ratio = len(polished_clean) / len(original_clean)
        if not (0.95 <= length_ratio <= 1.05):
            print(f"⚠️ 内容长度差异过大: {length_ratio:.2%}")
            return False
            
        return True

    def update_progress(self, step_name: str, sub_progress: float = 0.0):
        """更新进度信息
        Args:
            step_name: 当前步骤名称
            sub_progress: 子进度（0-1）
        """
        self.progress['current_step'] += 1 if step_name != self.progress['step_name'] else 0
        self.progress['step_name'] = step_name
        self.progress['sub_progress'] = sub_progress
        
        # 计算总进度
        total_progress = (self.progress['current_step'] - 1 + sub_progress) / self.progress['total_steps']
        
        # 计算预估剩余时间
        if self.start_time is None:
            self.start_time = time.time()
            print(f"\r→ 总进度: {total_progress*100:.1f}% ({step_name})", end='')
        else:
            elapsed_time = time.time() - self.start_time
            # 只在进度大于1%且经过时间大于0时才计算剩余时间
            if total_progress > 0.01 and elapsed_time > 0:
                try:
                    estimated_total_time = elapsed_time / total_progress
                    remaining_time = estimated_total_time - elapsed_time
                    
                    # 格式化剩余时间
                    if remaining_time < 60:
                        time_str = f"{remaining_time:.0f}秒"
                    elif remaining_time < 3600:
                        time_str = f"{remaining_time/60:.0f}分钟"
                    else:
                        time_str = f"{remaining_time/3600:.1f}小时"
                    
                    print(f"\r→ 总进度: {total_progress*100:.1f}% ({step_name}) - 预计剩余时间: {time_str}", end='')
                except:
                    # 如果计算出现任何问题，只显示进度
                    print(f"\r→ 总进度: {total_progress*100:.1f}% ({step_name})", end='')
            else:
                # 在进度较小或刚开始时只显示进度
                print(f"\r→ 总进度: {total_progress*100:.1f}% ({step_name})", end='')
        
    def save_state(self):
        """保存当前处理状态"""
        state = {
            'timestamp': self.timestamp,
            'total_tokens': self.total_tokens,
            'progress': self.progress,
            'temp_files': self.temp_files
        }
        
        state_file = os.path.join(self.output_dir, f'state_{self.timestamp}.json')
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
            
    def load_state(self, timestamp: str):
        """加载之前的处理状态
        Args:
            timestamp: 时间戳
        Returns:
            bool: 是否成功加载
        """
        state_file = os.path.join(self.output_dir, f'state_{timestamp}.json')
        if os.path.exists(state_file):
            with open(state_file, 'r', encoding='utf-8') as f:
                state = json.load(f)
                
            self.timestamp = state['timestamp']
            self.total_tokens = state['total_tokens']
            self.progress = state['progress']
            self.temp_files = state['temp_files']
            return True
        return False

def main():
    try:
        # 创建转录器实例
        transcriber = YouTubeTranscriber()
        
        # 获取用户输入
        video_url = input("请输入 YouTube 视频链接: ")
        output_file = "transcript.txt"
        
        # 检查是否有未完成的处理
        if os.path.exists("outputs"):
            state_files = [f for f in os.listdir("outputs") if f.startswith("state_")]
            if state_files:
                print("\n发现未完成的处理:")
                for i, f in enumerate(sorted(state_files, reverse=True)):
                    timestamp = f[6:-5]  # 提取时间戳
                    print(f"{i+1}. {timestamp}")
                choice = input("\n请选择要恢复的处理编号（直接回车开始新处理）: ")
                if choice.isdigit() and 1 <= int(choice) <= len(state_files):
                    timestamp = state_files[int(choice)-1][6:-5]
                    # 处理视频（恢复模式）
                    transcriber.process_video(video_url, output_file, timestamp)
                    return
        
        # 处理视频（新处理）
        transcriber.process_video(video_url, output_file)
        
    except ValueError as e:
        print(f"配置错误: {str(e)}")
    except Exception as e:
        print(f"运行错误: {str(e)}")

if __name__ == "__main__":
    main() 