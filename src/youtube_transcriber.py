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
from http import HTTPStatus
import oss2
import random

# 加载 .env 文件
load_dotenv()

class YouTubeTranscriber:
    """YouTube视频音频提取和语音识别工具"""
    
    # 文本优化的提示词
    POLISH_SYSTEM_PROMPT = """你是一个专业的文本编辑助手。你的任务是优化文本的格式和可读性，但要保持原有的口语表达和内容完全不变。
具体要求：
1. 保持原有的口语表达方式，不要改写为书面语
2. 保持原有的内容和意思完全不变
3. 仅优化格式，添加适当的段落划分
4. 修正明显的标点符号错误
5. 确保文本结构清晰，便于阅读"""

    POLISH_USER_PROMPT = """请帮我优化以下文本的格式，使其更容易阅读，但保持原有的口语表达和内容完全不变：

{text}

注意：
1. 不要改变任何词语和表达方式
2. 不要将口语改写为书面语
3. 只需优化格式，如段落划分和标点符号
4. 保持原有的语气和风格"""

    # 翻译的提示词
    TRANSLATE_SYSTEM_PROMPT = """你是一个专业的翻译助手。你的任务是将英文文本翻译成中文，要求：
1. 保持原文的意思和语气
2. 翻译要准确、自然
3. 保留原文的专业术语
4. 确保翻译后的文本通顺易读"""

    TRANSLATE_USER_PROMPT = """请将以下文本翻译成中文：

{text}

要求：
1. 保持原文的意思和语气
2. 翻译要准确、自然
3. 保留原文的专业术语
4. 确保翻译后的文本通顺易读"""

    # Token 价格（元/1K tokens）
    PRICE_PER_1K_TOKENS = {
        'qwen-plus': 0.1,  # 通义千问-Plus 模型价格
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
            'sensevoice-v1': 0  # 语音识别使用的时长（秒）
        }
        
        # 当前处理的音频文件路径
        self.current_audio_file = None

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
    
    def process_video(self, video_url: str, output_file: str):
        """处理完整的视频转录流程"""
        try:
            print("\n=== 开始处理视频 ===")
            print(f"视频链接: {video_url}")
            
            # 创建输出目录
            output_dir = "outputs"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # 生成时间戳
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            
            # 1. 提取音频
            print("\n[1/7] 提取音频")
            audio_file = self.extract_audio(video_url)
            audio_output = os.path.join(output_dir, f"1_original_{timestamp}_{os.path.basename(audio_file)}")
            if os.path.exists(audio_file):
                import shutil
                shutil.copy2(audio_file, audio_output)
                print(f"✓ 原始音频: {audio_output}")
            
            # 2. 处理音频
            print("\n[2/7] 处理音频")
            processed_file = self.process_audio(audio_file)
            processed_output = os.path.join(output_dir, f"2_processed_{timestamp}_{os.path.basename(processed_file)}")
            if os.path.exists(processed_file):
                import shutil
                shutil.copy2(processed_file, processed_output)
                print(f"✓ 处理后音频: {processed_output}")
                self.current_audio_file = processed_file  # 更新当前处理的音频文件路径
            
            # 3. 上传到OSS
            print("\n[3/7] 上传音频")
            file_url = self.upload_to_oss(processed_file)
            
            # 4. 语音识别
            print("\n[4/7] 语音识别")
            text = self.recognize_speech(file_url)
            recognition_output = os.path.join(output_dir, f"3_recognition_{timestamp}.txt")
            with open(recognition_output, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"✓ 识别结果: {recognition_output}")
            
            # 5. 翻译文本
            print("\n[5/7] 翻译文本")
            translated_text = self.translate_text(text)
            translation_output = os.path.join(output_dir, f"4_translation_{timestamp}.txt")
            with open(translation_output, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print(f"✓ 翻译结果: {translation_output}")
            
            # 6. 优化文本
            print("\n[6/7] 优化文本")
            polished_text = self.polish_text(translated_text)
            polished_output = os.path.join(output_dir, f"5_polished_{timestamp}.txt")
            with open(polished_output, 'w', encoding='utf-8') as f:
                f.write(polished_text)
            print(f"✓ 优化结果: {polished_output}")
            
            # 7. 保存最终结果
            print("\n[7/7] 保存结果")
            final_output = f"{os.path.splitext(output_file)[0]}_{timestamp}.txt"
            with open(final_output, 'w', encoding='utf-8') as f:
                f.write(polished_text)
            print(f"✓ 最终结果: {final_output}")
            
            print("\n=== 处理完成 ===")
            print("所有文件已保存在 outputs 目录：")
            print(f"1. 原始音频: {audio_output}")
            print(f"2. 处理后音频: {processed_output}")
            print(f"3. 识别结果: {recognition_output}")
            print(f"4. 翻译结果: {translation_output}")
            print(f"5. 优化结果: {polished_output}")
            print(f"6. 最终结果: {final_output}")
            
            # 打印 Token 使用统计
            print("\n=== Token 使用统计 ===")
            total_cost = 0
            
            # 通义千问-Plus 模型费用
            qwen_tokens = self.total_tokens['qwen-plus']
            qwen_cost = (qwen_tokens / 1000) * self.PRICE_PER_1K_TOKENS['qwen-plus']
            print(f"通义千问-Plus:")
            print(f"  • 使用量: {qwen_tokens:,} tokens")
            print(f"  • 费用: ¥{qwen_cost:.4f}")
            total_cost += qwen_cost
            
            # 语音识别费用
            audio_duration = self.total_tokens['sensevoice-v1']
            audio_cost = audio_duration * self.PRICE_PER_1K_TOKENS['sensevoice-v1']
            print(f"语音识别:")
            print(f"  • 使用量: {audio_duration:.1f} 秒")
            print(f"  • 费用: ¥{audio_cost:.4f}")
            total_cost += audio_cost
            
            print(f"\n总费用: ¥{total_cost:.4f}")
            
        except Exception as e:
            print(f"\n❌ 处理失败: {str(e)}")
            raise
            
        finally:
            pass
    
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
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:  # 如果还有重试机会
                    # 使用指数退避策略：2^attempt * 5秒（5s, 10s, 20s）
                    wait_time = (2 ** attempt) * 5
                    print(f"❌ 第 {attempt + 1} 次调用失败: {str(e)}")
                    print(f"→ {wait_time} 秒后重试...")
                    # 添加随机抖动，避免多个请求同时重试
                    jitter = random.uniform(0, 2)
                    time.sleep(wait_time + jitter)
                else:
                    print(f"❌ 最后一次调用失败: {str(e)}")
                    raise last_error

    def recognize_speech(self, file_url: str) -> str:
        """使用通义千问 SenseVoice API 进行语音识别"""
        try:
            print("→ 提交转写任务...")
            
            # 使用重试机制提交任务
            task_response = self.api_call_with_retry(
                Transcription.async_call,
                model='sensevoice-v1',
                file_urls=[file_url],
                language_hints=['zh']
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
        """清理文本中的特殊标记
        Args:
            text: 原始文本
        Returns:
            str: 清理后的文本
        """
        # 去除语音识别产生的特殊标记
        text = text.replace('<speech>', '')
        text = text.replace('</speech>', '')
        text = text.replace('<noise>', '')
        text = text.replace('</noise>', '')
        text = text.replace('<silence>', '')
        text = text.replace('</silence>', '')
        
        # 去除多余的空白字符
        text = ' '.join(text.split())
        
        return text
    
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
    
    def split_text(self, text: str) -> tuple:
        """智能分割文本
        Args:
            text: 要分割的文本
        Returns:
            tuple: (segments, is_paragraphs)，分割后的片段列表和是否按段落分割的标志
        """
        # 首先尝试按段落分割
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
        
        # 如果有多个段落，按段落处理
        if len(paragraphs) > 1:
            return paragraphs, True
        
        # 否则按句子分割
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
        
        return sentences, False
    
    def polish_text(self, text: str) -> str:
        """使用通义千问语言模型优化文本格式"""
        try:
            print("→ 优化文本中...")
            
            # 首先清理特殊标记
            text = self.clean_text(text)
            
            # 估算tokens数量
            def estimate_tokens(s: str) -> int:
                chinese_chars = sum(1 for c in s if ord(c) > 127)
                english_chars = len(''.join(c for c in s if ord(c) <= 127))
                return int(chinese_chars * 2 + english_chars * 0.25)
            
            # 计算系统提示词和用户提示词模板的基础tokens
            base_tokens = estimate_tokens(self.POLISH_SYSTEM_PROMPT) + \
                         estimate_tokens(self.POLISH_USER_PROMPT.replace("{text}", ""))
            
            # 计算输入文本的预估tokens
            input_tokens = estimate_tokens(text)
            total_tokens = base_tokens + input_tokens
            
            # 如果总tokens超过限制，需要分段处理
            if total_tokens > 6000:  # 更保守的限制
                print(f"→ 文本较长，将分段处理")
                print(f"  • 预估tokens: {total_tokens}")
                
                # 智能分割文本
                segments, is_paragraphs = self.split_text(text)
                
                # 分批处理
                current_batch = []
                current_tokens = base_tokens
                polished_parts = []
                
                for segment in segments:
                    segment_tokens = estimate_tokens(segment)
                    
                    # 如果当前段落加上已有内容会超过限制，先处理已有内容
                    if current_tokens + segment_tokens > 6000 and current_batch:
                        # 处理当前批次
                        batch_text = self.merge_text_parts(current_batch, is_paragraphs)
                        print(f"  • 处理批次: {len(batch_text)} 字符 ({current_tokens} tokens)")
                        
                        response = self.api_call_with_retry(
                            dashscope.Generation.call,
                            model='qwen-plus',
                            messages=[
                                {'role': 'system', 'content': self.POLISH_SYSTEM_PROMPT},
                                {'role': 'user', 'content': self.POLISH_USER_PROMPT.format(text=batch_text)}
                            ],
                            result_format='message',
                            max_tokens=4096,
                            temperature=0.2,
                            top_p=0.9,
                            enable_search=True,
                            seed=random.randint(1, 10000)
                        )
                        
                        if response.status_code == HTTPStatus.OK:
                            self.total_tokens['qwen-plus'] += response.usage.total_tokens
                            polished_parts.append(response.output.choices[0].message.content.strip())
                            print(f"    ✓ 本批使用 {response.usage.total_tokens} tokens")
                        else:
                            print(f"    ❌ 批次处理失败: {response.message}")
                            polished_parts.append(batch_text)
                        
                        current_batch = [segment]
                        current_tokens = base_tokens + segment_tokens
                    else:
                        current_batch.append(segment)
                        current_tokens += segment_tokens
                
                # 处理最后一批
                if current_batch:
                    batch_text = self.merge_text_parts(current_batch, is_paragraphs)
                    print(f"  • 处理最后批次: {len(batch_text)} 字符 ({current_tokens} tokens)")
                    
                    response = self.api_call_with_retry(
                        dashscope.Generation.call,
                        model='qwen-plus',
                        messages=[
                            {'role': 'system', 'content': self.POLISH_SYSTEM_PROMPT},
                            {'role': 'user', 'content': self.POLISH_USER_PROMPT.format(text=batch_text)}
                        ],
                        result_format='message',
                        max_tokens=4096,
                        temperature=0.2,
                        top_p=0.9,
                        enable_search=True,
                        seed=random.randint(1, 10000)
                    )
                    
                    if response.status_code == HTTPStatus.OK:
                        self.total_tokens['qwen-plus'] += response.usage.total_tokens
                        polished_parts.append(response.output.choices[0].message.content.strip())
                        print(f"    ✓ 本批使用 {response.usage.total_tokens} tokens")
                    else:
                        print(f"    ❌ 最后批次处理失败: {response.message}")
                        polished_parts.append(batch_text)
                
                # 合并所有处理结果
                polished_text = self.merge_text_parts(polished_parts, is_paragraphs)
                print("✓ 分段处理完成")
                
                # 验证内容完整性
                original_chars = sum(len(s.strip()) for s in segments)
                polished_chars = len(''.join(c for c in polished_text if c not in '\n\r\t '))
                if polished_chars < original_chars * 0.9:  # 如果优化后的内容少于原内容的90%
                    print("⚠️ 检测到内容可能有丢失，使用原文")
                    return text
                
                return polished_text
            else:
                print(f"→ 文本长度适中，单次处理")
                print(f"  • 预估tokens: {total_tokens}")
                
                response = self.api_call_with_retry(
                    dashscope.Generation.call,
                    model='qwen-plus',
                    messages=[
                        {'role': 'system', 'content': self.POLISH_SYSTEM_PROMPT},
                        {'role': 'user', 'content': self.POLISH_USER_PROMPT.format(text=text)}
                    ],
                    result_format='message',
                    max_tokens=4096,
                    temperature=0.2,
                    top_p=0.9,
                    enable_search=True,
                    seed=random.randint(1, 10000)
                )
                
                if response.status_code == HTTPStatus.OK:
                    self.total_tokens['qwen-plus'] += response.usage.total_tokens
                    polished_text = response.output.choices[0].message.content
                    print(f"  ✓ 使用 {response.usage.total_tokens} tokens")
                    
                    # 验证内容完整性
                    original_chars = len(''.join(c for c in text if c not in '\n\r\t '))
                    polished_chars = len(''.join(c for c in polished_text if c not in '\n\r\t '))
                    if polished_chars < original_chars * 0.9:  # 如果优化后的内容少于原内容的90%
                        print("⚠️ 检测到内容可能有丢失，使用原文")
                        return text
                    
                    return polished_text
                else:
                    raise Exception(f"优化请求失败: {response.message}")
            
        except Exception as e:
            print(f"❌ 优化失败: {str(e)}")
            return text  # 优化失败时返回原文本，不中止程序
    
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
            
            # qwen-plus的30K tokens限制，预留4K给输出（减少单批次负载）
            # 减去基础提示词tokens后，计算单次能处理的最大文本长度
            max_text_tokens = 6000 - base_tokens  # 更保守的限制，约 6K tokens
            max_chars = int(max_text_tokens / 0.25)  # 对于英文文本，平均每个字符0.25个token
            
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
                        print(f"  • 处理第 {len(translated_parts)+1} 批: {len(batch_text)} 字符 ({current_tokens} tokens)")
                        
                        response = self.api_call_with_retry(
                            dashscope.Generation.call,
                            model='qwen-plus',
                            messages=[
                                {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                                {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=batch_text)}
                            ],
                            result_format='message',
                            max_tokens=4096,
                            temperature=0.3,
                            top_p=0.95,
                            enable_search=True,
                            seed=random.randint(1, 10000)
                        )
                        
                        if response.status_code == HTTPStatus.OK:
                            self.total_tokens['qwen-plus'] += response.usage.total_tokens
                            translated_parts.append(response.output.choices[0].message.content.strip())
                            print(f"    ✓ 本批使用 {response.usage.total_tokens} tokens")
                        else:
                            print(f"    ❌ 第 {len(translated_parts)+1} 批翻译失败: {response.message}")
                            raise Exception(f"翻译请求失败: {response.message}")
                        
                        current_batch = [segment]
                        current_tokens = base_tokens + segment_tokens
                    else:
                        current_batch.append(segment)
                        current_tokens += segment_tokens
                
                # 处理最后一批
                if current_batch:
                    batch_text = self.merge_text_parts(current_batch, is_paragraphs)
                    print(f"  • 处理最后一批: {len(batch_text)} 字符 ({current_tokens} tokens)")
                    
                    response = self.api_call_with_retry(
                        dashscope.Generation.call,
                        model='qwen-plus',
                        messages=[
                            {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                            {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=batch_text)}
                        ],
                        result_format='message',
                        max_tokens=4096,
                        temperature=0.3,
                        top_p=0.95,
                        enable_search=True,
                        seed=random.randint(1, 10000)
                    )
                    
                    if response.status_code == HTTPStatus.OK:
                        self.total_tokens['qwen-plus'] += response.usage.total_tokens
                        translated_parts.append(response.output.choices[0].message.content.strip())
                        print(f"    ✓ 本批使用 {response.usage.total_tokens} tokens")
                    else:
                        print(f"    ❌ 最后一批翻译失败: {response.message}")
                        raise Exception(f"翻译请求失败: {response.message}")
                
                # 合并所有翻译结果
                translated_text = self.merge_text_parts(translated_parts, is_paragraphs)
                
                # 验证内容完整性
                original_words = len([w for w in text.split() if any(ord(c) < 128 for c in w)])  # 统计英文单词数
                translated_chars = len(''.join(c for c in translated_text if ord(c) > 127))  # 统计中文字符数
                
                # 英文单词和中文字符的比例通常在 1:1.5 到 1:2.5 之间
                # 如果比例过低，可能表示翻译不完整
                ratio = translated_chars / original_words if original_words > 0 else float('inf')
                if ratio < 1.0:  # 如果平均每个英文单词对应的中文字符数小于1，可能有问题
                    print(f"⚠️ 检测到内容可能有丢失 (英文单词数: {original_words}, 中文字符数: {translated_chars}, 比例: {ratio:.2f})")
                    raise Exception("翻译结果不完整")
                
            else:
                print(f"→ 文本长度适中，单次处理")
                estimated_tokens = estimate_tokens(text) + base_tokens
                print(f"  • 预估tokens: {estimated_tokens}")
                
                response = self.api_call_with_retry(
                    dashscope.Generation.call,
                    model='qwen-plus',
                    messages=[
                        {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                        {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=text)}
                    ],
                    result_format='message',
                    max_tokens=8192,
                    temperature=0.3,
                    top_p=0.95,
                    enable_search=True,
                    seed=random.randint(1, 10000)
                )
                
                if response.status_code == HTTPStatus.OK:
                    self.total_tokens['qwen-plus'] += response.usage.total_tokens
                    translated_text = response.output.choices[0].message.content
                    print(f"  ✓ 使用 {response.usage.total_tokens} tokens")
                    
                    # 验证内容完整性
                    original_words = len([w for w in text.split() if any(ord(c) < 128 for c in w)])  # 统计英文单词数
                    translated_chars = len(''.join(c for c in translated_text if ord(c) > 127))  # 统计中文字符数
                    
                    # 英文单词和中文字符的比例通常在 1:1.5 到 1:2.5 之间
                    # 如果比例过低，可能表示翻译不完整
                    ratio = translated_chars / original_words if original_words > 0 else float('inf')
                    if ratio < 1.0:  # 如果平均每个英文单词对应的中文字符数小于1，可能有问题
                        print(f"⚠️ 检测到内容可能有丢失 (英文单词数: {original_words}, 中文字符数: {translated_chars}, 比例: {ratio:.2f})")
                        raise Exception("翻译结果不完整")
                else:
                    raise Exception(f"翻译请求失败: {response.message}")
            
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

def main():
    try:
        # 创建转录器实例
        transcriber = YouTubeTranscriber()
        
        # 获取用户输入
        video_url = input("请输入 YouTube 视频链接: ")
        output_file = "transcript.txt"
        
        # 处理视频
        transcriber.process_video(video_url, output_file)
        
    except ValueError as e:
        print(f"配置错误: {str(e)}")
    except Exception as e:
        print(f"运行错误: {str(e)}")

if __name__ == "__main__":
    main() 