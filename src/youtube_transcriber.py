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
            
        except Exception as e:
            print(f"\n❌ 处理失败: {str(e)}")
            raise
            
        finally:
            pass
    
    def recognize_speech(self, file_url: str) -> str:
        """使用通义千问 SenseVoice API 进行语音识别"""
        try:
            print("→ 提交转写任务...")
            task_response = Transcription.async_call(
                model='sensevoice-v1',
                file_urls=[file_url],
                language_hints=['zh']
            )
            
            if task_response.status_code != HTTPStatus.OK:
                raise Exception(f"提交失败: {task_response.message}")
            
            task_id = task_response.output.task_id
            print(f"✓ 任务已提交 (ID: {task_id})")
            
            print("→ 等待转写结果...")
            transcribe_response = Transcription.wait(task=task_id)
            
            if transcribe_response.status_code == HTTPStatus.OK:
                transcription_url = transcribe_response.output['results'][0]['transcription_url']
                print("→ 下载转写结果...")
                
                text_response = requests.get(transcription_url)
                if text_response.status_code == 200:
                    text_result = text_response.json()
                    text = text_result['transcripts'][0]['text']
                    print("✓ 转写完成")
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
    
    def polish_text(self, text: str) -> str:
        """使用通义千问语言模型优化文本格式"""
        try:
            print("→ 优化文本中...")
            
            response = dashscope.Generation.call(
                model='qwen-plus',
                messages=[
                    {'role': 'system', 'content': self.POLISH_SYSTEM_PROMPT},
                    {'role': 'user', 'content': self.POLISH_USER_PROMPT.format(text=text)}
                ],
                result_format='message',
                max_tokens=5000,  # 增加输出长度限制
                temperature=0.2,
                top_p=0.9,
                enable_search=True,
                seed=random.randint(1, 10000)
            )
            
            if response.status_code == HTTPStatus.OK:
                polished_text = response.output.choices[0].message.content
                print("✓ 优化完成")
                return polished_text
            else:
                raise Exception(f"优化请求失败: {response.message}")
            
        except Exception as e:
            print(f"❌ 优化失败: {str(e)}")
            return text
    
    def translate_text(self, text: str) -> str:
        """使用通义千问翻译英文文本为中文"""
        try:
            # 检查输入文本长度
            input_length = len(text)
            print(f"→ 输入文本长度: {input_length} 字符")
            
            if not any(ord(c) < 128 for c in text):
                print("✓ 无需翻译（未检测到英文内容）")
                return text
                
            print("→ 翻译中...")
            
            # 估算tokens数量（粗略估计：英文单词约1.3个tokens，中文字符约2.5个tokens）
            def estimate_tokens(s: str) -> int:
                chinese_chars = sum(1 for c in s if ord(c) > 127)
                english_chars = sum(1 for c in s if ord(c) <= 127)
                return int(chinese_chars * 2.5 + english_chars * 0.25)
            
            # 计算系统提示词和用户提示词模板的基础tokens
            base_tokens = estimate_tokens(self.TRANSLATE_SYSTEM_PROMPT) + \
                         estimate_tokens(self.TRANSLATE_USER_PROMPT.replace("{text}", ""))
            print(f"→ 提示词基础tokens: {base_tokens}")
            
            # 考虑到qwen-plus的30K tokens限制，预留5K给输出，实际可用约24K
            # 减去基础提示词tokens后，计算单次能处理的最大文本长度
            max_text_tokens = 24000 - base_tokens
            max_chars = int(max_text_tokens / 0.25)  # 对于英文文本，平均每个字符0.25个token
            
            # 如果文本太长，需要分段处理
            if input_length > max_chars:
                print(f"→ 文本较长，将分段处理")
                print(f"  • 单次最大处理: {max_chars} 字符（约 {max_text_tokens} tokens）")
                # 按句子分割
                sentences = text.replace('。', '.').replace('！', '!').replace('？', '?').split('.')
                translated_parts = []
                current_part = []
                current_length = 0
                
                for i, sentence in enumerate(sentences, 1):
                    sentence = sentence.strip()
                    if not sentence:
                        continue
                        
                    # 如果当前句子加上已有内容超过限制，先处理已有内容
                    if current_length + len(sentence) > max_chars and current_part:
                        part_text = '. '.join(current_part)
                        print(f"  • 处理第 {len(translated_parts)+1} 批: {len(part_text)} 字符")
                        response = dashscope.Generation.call(
                            model='qwen-plus',
                            messages=[
                                {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                                {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=part_text)}
                            ],
                            result_format='message',
                            max_tokens=5000,  # 增加输出长度限制
                            temperature=0.3,
                            top_p=0.95,
                            enable_search=True,
                            seed=random.randint(1, 10000)
                        )
                        
                        if response.status_code == HTTPStatus.OK:
                            part_result = response.output.choices[0].message.content.strip()
                            translated_parts.append(part_result)
                        else:
                            print(f"  ❌ 第 {len(translated_parts)+1} 批翻译失败: {response.message}")
                            translated_parts.append(part_text)
                        
                        current_part = []
                        current_length = 0
                    
                    current_part.append(sentence)
                    current_length += len(sentence) + 2  # +2 for '. '
                
                # 处理最后一批
                if current_part:
                    part_text = '. '.join(current_part)
                    print(f"  • 处理最后一批: {len(part_text)} 字符")
                    response = dashscope.Generation.call(
                        model='qwen-plus',
                        messages=[
                            {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                            {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=part_text)}
                        ],
                        result_format='message',
                        max_tokens=5000,  # 增加输出长度限制
                        temperature=0.3,
                        top_p=0.95,
                        enable_search=True,
                        seed=random.randint(1, 10000)
                    )
                    
                    if response.status_code == HTTPStatus.OK:
                        part_result = response.output.choices[0].message.content.strip()
                        translated_parts.append(part_result)
                    else:
                        print(f"  ❌ 最后一批翻译失败: {response.message}")
                        translated_parts.append(part_text)
                
                translated_text = "。".join(translated_parts)
            else:
                print(f"→ 文本长度适中，单次处理")
                print(f"  • 预估tokens: {estimate_tokens(text) + base_tokens}")
                response = dashscope.Generation.call(
                    model='qwen-plus',
                    messages=[
                        {'role': 'system', 'content': self.TRANSLATE_SYSTEM_PROMPT},
                        {'role': 'user', 'content': self.TRANSLATE_USER_PROMPT.format(text=text)}
                    ],
                    result_format='message',
                    max_tokens=5000,  # 增加输出长度限制
                    temperature=0.3,
                    top_p=0.95,
                    enable_search=True,
                    seed=random.randint(1, 10000)
                )
                
                if response.status_code == HTTPStatus.OK:
                    translated_text = response.output.choices[0].message.content
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
            return text

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