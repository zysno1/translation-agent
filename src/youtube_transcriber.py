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
        """从YouTube视频中提取音频
        Args:
            video_url: YouTube视频链接
        Returns:
            音频文件路径
        """
        try:
            # 首先获取视频ID
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(video_url, download=False)
                video_id = info['id']
                audio_file = f"audio_{video_id}.wav"
            
            # 检查本地是否已存在可用的音频文件
            if self.is_valid_audio_file(audio_file):
                print(f"发现可用的本地音频文件: {audio_file}")
                return audio_file
            else:
                # 如果文件存在但无效，则删除
                if os.path.exists(audio_file):
                    print(f"发现无效的本地音频文件，将重新下载")
                    os.remove(audio_file)
            
            print("正在从视频中提取音频...")
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
                
                # 下载完成后再次验证文件
                if not self.is_valid_audio_file(audio_file):
                    raise Exception("音频文件下载或转换失败")
                    
                return audio_file
                
        except Exception as e:
            # 如果处理过程中出错，清理可能存在的损坏文件
            if os.path.exists(audio_file):
                os.remove(audio_file)
            raise Exception(f"音频提取失败: {str(e)}")
    
    def process_audio(self, input_file: str) -> str:
        """处理音频文件，确保符合API要求
        Args:
            input_file: 输入音频文件路径
        Returns:
            处理后的音频文件路径
        """
        try:
            print("正在处理音频格式...")
            audio = AudioSegment.from_wav(input_file)
            
            # 转换为16kHz采样率
            if audio.frame_rate != 16000:
                audio = audio.set_frame_rate(16000)
            
            # 转换为单声道
            if audio.channels > 1:
                audio = audio.set_channels(1)
            
            output_file = f"{input_file}_processed.wav"
            audio.export(output_file, format="wav")
            return output_file
            
        except Exception as e:
            raise Exception(f"音频处理失败: {str(e)}")
    
    def split_audio(self, audio_file: str, max_size_mb: int = 20) -> list:
        """将音频文件分割成较小的片段
        Args:
            audio_file: 音频文件路径
            max_size_mb: 每个分片的最大大小（MB），考虑到base64编码会增加约33%的大小
        Returns:
            list: 分片文件路径列表
        """
        try:
            print("正在分割音频...")
            audio = AudioSegment.from_wav(audio_file)
            
            # 获取音频总时长（毫秒）和文件大小
            total_duration = len(audio)
            file_size = os.path.getsize(audio_file)
            
            # 计算需要的分片数量（向上取整）
            # 考虑到base64编码后的大小增加，将限制调整为原来的75%
            adjusted_max_size = int(max_size_mb * 0.75 * 1024 * 1024)
            num_chunks = (file_size + adjusted_max_size - 1) // adjusted_max_size
            
            # 计算每个分片的时长
            chunk_duration = total_duration // num_chunks
            
            print(f"音频总时长: {total_duration}ms, 文件大小: {file_size/1024/1024:.2f}MB")
            print(f"将分割成 {num_chunks} 个片段，每个片段约 {chunk_duration}ms")
            
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
        """上传文件到OSS
        Args:
            local_file: 本地文件路径
        Returns:
            str: 文件的URL
        """
        try:
            print("正在上传文件到OSS...")
            # 生成OSS中的文件名
            file_name = f"audio/{str(uuid.uuid4())}/{os.path.basename(local_file)}"
            
            # 上传文件
            with open(local_file, 'rb') as f:
                self.bucket.put_object(file_name, f)
            
            # 生成文件URL（默认有效期24小时）
            url = self.bucket.sign_url('GET', file_name, 24 * 3600)
            print(f"文件已上传: {url}")
            return url
            
        except Exception as e:
            raise Exception(f"上传文件失败: {str(e)}")
    
    def process_video(self, video_url: str, output_file: str):
        """处理完整的视频转录流程
        Args:
            video_url: YouTube视频链接
            output_file: 输出文本文件路径
        """
        audio_file = None
        processed_file = None
        
        try:
            # 1. 提取音频
            audio_file = self.extract_audio(video_url)
            
            # 2. 处理音频
            processed_file = self.process_audio(audio_file)
            
            # 3. 上传到OSS
            file_url = self.upload_to_oss(processed_file)
            
            # 4. 语音识别
            text = self.recognize_speech(file_url)
            
            # 5. 使用通义千问优化文本
            polished_text = self.polish_text(text)
            
            # 6. 保存结果
            print("正在保存识别结果...")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(polished_text)
            
            print(f"处理完成！结果已保存至: {output_file}")
            
        except Exception as e:
            print(f"处理失败: {str(e)}")
            raise
            
        finally:
            # 清理临时文件
            if processed_file and os.path.exists(processed_file):
                os.remove(processed_file)
            if audio_file and os.path.exists(audio_file):
                os.remove(audio_file)
    
    def recognize_speech(self, file_url: str) -> str:
        """使用通义千问 SenseVoice API 进行语音识别
        Args:
            file_url: 音频文件的OSS URL
        Returns:
            识别的文本结果
        """
        try:
            print("正在进行语音识别...")
            
            # 提交转写任务
            print("正在提交转写任务...")
            task_response = Transcription.async_call(
                model='sensevoice-v1',
                file_urls=[file_url],  # 使用OSS文件URL
                language_hints=['zh']  # 中文识别
            )
            
            if task_response.status_code != HTTPStatus.OK:
                raise Exception(f"提交任务失败: {task_response.message}")
            
            # 等待任务完成并获取结果
            print("正在等待转写结果...")
            transcribe_response = Transcription.wait(task=task_response.output.task_id)
            
            if transcribe_response.status_code == HTTPStatus.OK:
                # 打印完整的响应内容以便调试
                print("转写响应内容:", transcribe_response.output)
                
                # 从 transcription_url 获取转写结果
                transcription_url = transcribe_response.output['results'][0]['transcription_url']
                print("正在下载转写结果...")
                text_response = requests.get(transcription_url)
                
                if text_response.status_code == 200:
                    text_result = text_response.json()
                    # 提取文本内容
                    text = text_result['transcripts'][0]['text']
                    return text
                else:
                    raise Exception(f"获取转写结果失败: {text_response.text}")
            else:
                raise Exception(f"任务失败: {transcribe_response.message}")
            
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
        """使用通义千问语言模型优化文本格式
        Args:
            text: 需要优化的文本
        Returns:
            str: 优化后的文本
        """
        try:
            print("正在使用通义千问优化文本格式...")
            
            # 构建系统提示词
            system_prompt = """你是一位专业的文本编辑，需要在保持原有内容和口语表达的基础上，优化文本的格式和可读性。
你需要：
1. 修正明显的语音识别错误（如果有）
2. 保持原有的口语表达方式不变
3. 添加合适的标点符号
4. 根据内容和语义分段
5. 确保段落结构清晰
6. 保持原有的表达方式和语气
请记住：不要将口语改写为书面语，保持原有的表达特点。"""

            # 构建用户提示词
            user_prompt = f"""请帮我优化以下文本的格式，使其更容易阅读：

{text}

要求：
1. 保持原有的内容和口语表达完全不变
2. 只优化格式，使文本更有条理
3. 合理使用标点符号
4. 按照内容和语义分段
5. 修正明显的语音识别错误（如果有）
6. 不要改变说话人的语气和表达方式"""

            # 调用通义千问API
            response = dashscope.Generation.call(
                model='qwen-max',  # 使用通义千问最新模型
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': user_prompt}
                ],
                result_format='message',  # 返回消息格式
                max_tokens=2000,  # 最大输出长度
                temperature=0.2,  # 使用更低的温度以减少创造性改写
                top_p=0.9,  # 保持输出的准确性
                enable_search=True,  # 启用搜索增强
                seed=random.randint(1, 10000)  # 随机种子
            )
            
            if response.status_code == HTTPStatus.OK:
                # 提取优化后的文本
                polished_text = response.output.choices[0].message.content
                return polished_text
            else:
                raise Exception(f"文本优化失败: {response.message}")
            
        except Exception as e:
            print(f"文本优化失败: {str(e)}")
            # 如果优化失败，返回原文本
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