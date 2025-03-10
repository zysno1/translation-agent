#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
模型接口
提供与LangChain和各种AI模型交互的统一接口

设计原则:
1. 统一接口原则: 所有AI模型访问必须通过Models类提供的静态方法
2. LangChain中介原则: 所有模型交互必须通过LangChain框架实现
3. 直接访问禁止原则: 禁止在业务代码中直接引入或调用模型SDK
4. 统一错误处理原则: 所有模型调用错误必须经过统一处理和转换
5. 可扩展性优先原则: 设计必须支持无缝切换模型和添加新模型功能
"""

import os
import time
import json
import functools
from typing import Optional, Dict, Any, Union, List, Callable
from pathlib import Path
from datetime import datetime
import logging
import urllib.request
import librosa
import soundfile as sf

# LangChain导入
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.documents import Document
from langchain_community.callbacks.manager import get_openai_callback
from langchain_community.chat_models.tongyi import ChatTongyi

from src.config.config_manager import get_config
from src.utils.log import get_logger
from src.utils.oss_utils import OSSClient

# 获取日志器
logger = get_logger()


# 重试装饰器
def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """
    为模型调用提供重试功能的装饰器
    
    Args:
        max_attempts: 最大重试次数
        delay: 初始延迟(秒)
        backoff: 延迟倍数
        exceptions: 需要重试的异常类型
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= max_attempts:
                        logger.error(f"重试耗尽 ({max_attempts}次): {str(e)}")
                        raise
                    
                    logger.warning(f"调用失败，将在{current_delay}秒后重试 [{attempt}/{max_attempts}]: {str(e)}")
                    time.sleep(current_delay)
                    current_delay *= backoff
                    
        return wrapper
    return decorator


# 模型调用异常
class ModelError(Exception):
    """模型调用异常基类"""
    pass


class ModelAPIError(ModelError):
    """模型API调用错误"""
    pass


class ModelTimeoutError(ModelError):
    """模型调用超时错误"""
    pass


class ModelAudit:
    """模型调用审计和监控"""
    
    # 统计数据存储
    _stats = {
        "calls": 0,          # 总调用次数
        "failures": 0,       # 失败次数
        "tokens": {          # token使用统计
            "input": 0,      # 输入token
            "output": 0,     # 输出token
        },
        "models": {},        # 各模型使用统计
        "costs": 0.0,        # 估计成本
        "methods": {         # 方法调用统计
            "get_llm": 0,
            "translate": 0,
            "transcribe": 0,
            "summarize": 0,
            "analyze": 0,
        }
    }
    
    @classmethod
    def log_call(cls, model_name: str, method: str, 
                input_tokens: int = 0, output_tokens: int = 0, 
                success: bool = True, cost: float = 0.0,
                metadata: Dict = None):
        """
        记录模型调用
        
        Args:
            model_name: 模型名称
            method: 调用方法名
            input_tokens: 输入token数
            output_tokens: 输出token数
            success: 是否成功
            cost: 调用成本
            metadata: 其他元数据
        """
        # 更新总计数
        cls._stats["calls"] += 1
        if not success:
            cls._stats["failures"] += 1
            
        # 更新token统计
        cls._stats["tokens"]["input"] += input_tokens
        cls._stats["tokens"]["output"] += output_tokens
        
        # 更新成本
        cls._stats["costs"] += cost
        
        # 更新方法调用统计
        if method in cls._stats["methods"]:
            cls._stats["methods"][method] += 1
        else:
            cls._stats["methods"][method] = 1
            
        # 更新模型统计
        if model_name not in cls._stats["models"]:
            cls._stats["models"][model_name] = {
                "calls": 0,
                "failures": 0,
                "tokens": {"input": 0, "output": 0},
                "costs": 0.0
            }
            
        model_stats = cls._stats["models"][model_name]
        model_stats["calls"] += 1
        if not success:
            model_stats["failures"] += 1
        model_stats["tokens"]["input"] += input_tokens
        model_stats["tokens"]["output"] += output_tokens
        model_stats["costs"] += cost
        
        # 记录调用日志
        log_message = (
            f"模型调用: {model_name}, 方法: {method}, "
            f"输入: {input_tokens}tokens, 输出: {output_tokens}tokens, "
            f"成本: {cost:.6f}, 状态: {'成功' if success else '失败'}"
        )
        
        if metadata:
            log_message += f", 元数据: {json.dumps(metadata, ensure_ascii=False)}"
            
        if success:
            logger.info(log_message)
        else:
            logger.error(log_message)
    
    @classmethod
    def get_stats(cls) -> Dict:
        """获取统计数据"""
        return cls._stats.copy()
    
    @classmethod
    def get_success_rate(cls) -> float:
        """获取成功率"""
        if cls._stats["calls"] == 0:
            return 1.0
        return 1.0 - (cls._stats["failures"] / cls._stats["calls"])
    
    @classmethod
    def get_model_stats(cls, model_name: str) -> Dict:
        """获取特定模型的统计数据"""
        return cls._stats.get("models", {}).get(model_name, {})
    
    @classmethod
    def reset_stats(cls):
        """重置统计数据"""
        cls._stats = {
            "calls": 0,
            "failures": 0,
            "tokens": {"input": 0, "output": 0},
            "models": {},
            "costs": 0.0,
            "methods": {
                "get_llm": 0,
                "translate": 0,
                "transcribe": 0,
                "summarize": 0,
                "analyze": 0,
            }
        }
    
    @classmethod
    def export_report(cls) -> Dict:
        """导出审计报告"""
        success_rate = cls.get_success_rate() * 100
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_calls": cls._stats["calls"],
                "success_rate": f"{success_rate:.2f}%",
                "total_tokens": sum(cls._stats["tokens"].values()),
                "total_cost": cls._stats["costs"],
            },
            "models": {},
            "methods": cls._stats["methods"]
        }
        
        # 处理每个模型的统计
        for model, stats in cls._stats.get("models", {}).items():
            if stats["calls"] > 0:
                model_success_rate = (1.0 - (stats["failures"] / stats["calls"])) * 100
                report["models"][model] = {
                    "calls": stats["calls"],
                    "success_rate": f"{model_success_rate:.2f}%",
                    "tokens": stats["tokens"],
                    "cost": stats["costs"]
                }
        
        return report


# 模型调用装饰器
def audit_model_call(method_name: str):
    """
    审计模型调用的装饰器
    
    Args:
        method_name: 方法名称
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            model_name = kwargs.get("model_name", "unknown")
            # 如果没有明确指定，则从配置获取默认值
            if model_name is None:
                config = get_config()
                model_name = config.get('defaults', {}).get(method_name, "unknown")
                
            start_time = time.time()
            success = True
            input_tokens = 0
            output_tokens = 0
            cost = 0.0
            
            try:
                # 使用OpenAI回调来跟踪token使用
                with get_openai_callback() as cb:
                    result = func(*args, **kwargs)
                    
                    # 仅当使用OpenAI模型时才有效
                    if "gpt" in model_name:
                        input_tokens = cb.prompt_tokens
                        output_tokens = cb.completion_tokens
                        cost = cb.total_cost
                
                return result
            except Exception as e:
                success = False
                raise
            finally:
                # 计算执行时间
                execution_time = time.time() - start_time
                
                # 记录调用统计
                ModelAudit.log_call(
                    model_name=model_name,
                    method=method_name,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    success=success,
                    cost=cost,
                    metadata={"execution_time": execution_time}
                )
                
        return wrapper
    return decorator


class QwenModel:
    """通义千问模型接口"""
    
    def __init__(self, model_name: str, temperature: float = 0.7):
        """
        初始化通义千问模型
        
        Args:
            model_name: 模型名称
            temperature: 温度参数
        """
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = get_config().get('api_keys', {}).get('qwen')
        
        if not self.api_key:
            # 尝试从环境变量DASHSCOPE_API_KEY获取
            self.api_key = os.environ.get('DASHSCOPE_API_KEY')
            
        if not self.api_key:
            logger.warning("未配置通义千问API密钥")
        
        logger.info(f"初始化通义千问模型: {model_name}")
        
        # 初始化DashScope客户端
        try:
            from dashscope import Generation
            self.client = Generation()
            logger.info("成功初始化DashScope客户端")
        except ImportError as e:
            logger.error(f"导入DashScope SDK失败: {e}")
            self.client = None
    
    def __call__(self, prompt):
        """
        调用模型
        
        Args:
            prompt: 提示文本
            
        Returns:
            模型输出
        """
        try:
            # 使用DashScope API调用千问模型
            if self.client is None:
                raise ImportError("DashScope SDK未成功导入")
                
            from dashscope import Generation
            
            logger.info(f"调用通义千问模型: {self.model_name}")
            
            response = Generation.call(
                model=self.model_name,
                prompt=prompt,
                temperature=self.temperature,
                api_key=self.api_key
            )
            
            if response.status_code == 200:
                output = response.output.text
                logger.info(f"通义千问模型响应成功，输出长度: {len(output)}")
                return output
            else:
                logger.error(f"通义千问API错误: {response.status_code} - {response.message}")
                return f"模型API错误: {response.status_code} - {response.message}"
        except Exception as e:
            logger.error(f"通义千问模型调用失败: {e}")
            return f"模型调用失败: {str(e)}"


class Models:
    """统一的LangChain模型接口
    
    所有AI模型访问都必须通过此类提供的静态方法，禁止直接调用底层SDK
    """
    
    @staticmethod
    @audit_model_call("get_llm")
    @retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,))
    def get_llm(model_name: Optional[str] = None, temperature: float = 0.7):
        """
        获取LLM实例
        
        Args:
            model_name: 模型名称，如果为None则从配置获取
            temperature: 温度参数
            
        Returns:
            LLM模型实例
        """
        try:
            # 从配置加载模型名称（如果未提供）
            config = get_config()
            if model_name is None:
                model_name = config.get('defaults', {}).get('llm')
                logger.info(f"使用默认LLM模型: {model_name}")
            
            # 导入需要的库（延迟导入）
            if "qwen" in model_name.lower():
                # 使用通义千问模型
                try:
                    logger.info(f"初始化通义千问模型: {model_name}")
                    
                    # 尝试使用LangChain的通义千问集成
                    try:
                        from langchain_community.llms import Tongyi
                        
                        api_key = os.environ.get('DASHSCOPE_API_KEY')
                        if not api_key:
                            api_key = config.get('api_keys', {}).get('qwen')
                            
                        logger.info(f"使用LangChain Tongyi集成")
                        return Tongyi(
                            model_name=model_name,
                            temperature=temperature,
                            tongyi_api_key=api_key
                        )
                    except ImportError as e:
                        logger.warning(f"导入LangChain Tongyi集成失败: {e}，使用自定义封装")
                        # 使用自定义封装
                        from src.models.qwen_llm import QwenAdapter
                        return QwenAdapter(model_name, temperature=temperature)
                except Exception as e:
                    logger.error(f"初始化通义千问模型失败: {e}")
                    raise ModelAPIError(f"通义千问模型初始化失败: {str(e)}")
            
            elif "deepseek" in model_name.lower():
                # 使用DeepSeek模型
                try:
                    # 首先尝试使用LangChain的DeepSeek集成
                    try:
                        from langchain_community.chat_models import ChatDeepSeek
                        
                        logger.info(f"初始化DeepSeek模型: {model_name}")
                        api_key = config.get('api_keys', {}).get('deepseek')
                        base_url = config.get('providers', {}).get('deepseek', {}).get('api_base', 
                                                                                      "https://api.deepseek.com/v1")
                        
                        return ChatDeepSeek(
                            model_name=model_name,
                            temperature=temperature,
                            deepseek_api_key=api_key,
                            deepseek_api_base=base_url,
                            max_tokens=4000
                        )
                    except ImportError:
                        # 如果找不到ChatDeepSeek，尝试使用OpenAI兼容模式
                        logger.warning(f"找不到LangChain的DeepSeek集成，尝试使用兼容接口")
                        from langchain_openai import ChatOpenAI
                        
                        api_key = config.get('api_keys', {}).get('deepseek')
                        base_url = config.get('providers', {}).get('deepseek', {}).get('api_base', 
                                                                                      "https://api.deepseek.com/v1")
                        
                        return ChatOpenAI(
                            model_name=model_name,
                            temperature=temperature,
                            openai_api_key=api_key,
                            openai_api_base=base_url,
                            max_tokens=4000
                        )
                except Exception as e:
                    logger.error(f"初始化DeepSeek模型失败: {e}")
                    raise ModelAPIError(f"DeepSeek模型初始化失败: {str(e)}")
            
            elif "doubao" in model_name.lower():
                # 使用抖报(Doubao)模型
                try:
                    # 尝试使用LangChain集成
                    try:
                        from langchain_community.chat_models import ChatDoubao
                        
                        logger.info(f"初始化抖报模型: {model_name}")
                        api_key = config.get('api_keys', {}).get('doubao')
                        base_url = config.get('providers', {}).get('doubao', {}).get('api_base', 
                                                                                   "https://api.doubao.com/v1")
                        
                        return ChatDoubao(
                            model_name=model_name,
                            temperature=temperature,
                            doubao_api_key=api_key,
                            doubao_api_base=base_url,
                            max_tokens=4000
                        )
                    except ImportError:
                        # 如果找不到直接集成，尝试使用OpenAI兼容模式
                        logger.warning(f"找不到LangChain的抖报模型集成，尝试使用兼容接口")
                        from langchain_openai import ChatOpenAI
                        
                        api_key = config.get('api_keys', {}).get('doubao')
                        base_url = config.get('providers', {}).get('doubao', {}).get('api_base', 
                                                                                   "https://api.doubao.com/v1")
                        
                        return ChatOpenAI(
                            model_name=model_name,
                            temperature=temperature,
                            openai_api_key=api_key,
                            openai_api_base=base_url,
                            max_tokens=4000
                        )
                except Exception as e:
                    logger.error(f"初始化抖报模型失败: {e}")
                    raise ModelAPIError(f"抖报模型初始化失败: {str(e)}")
            
            else:
                # 默认使用通义千问
                logger.warning(f"未识别的模型类型: {model_name}，使用默认通义千问模型")
                try:
                    # 获取默认通义千问模型名称
                    default_qwen = config.get('defaults', {}).get('qwen_fallback', 'qwen-max')
                    logger.info(f"使用默认通义千问模型: {default_qwen}")
                    
                    from langchain_community.llms import Tongyi
                    
                    api_key = os.environ.get('DASHSCOPE_API_KEY')
                    if not api_key:
                        api_key = config.get('api_keys', {}).get('qwen')
                    
                    return Tongyi(
                        model_name=default_qwen,
                        temperature=temperature,
                        tongyi_api_key=api_key
                    )
                except Exception as e:
                    logger.error(f"初始化默认通义千问模型失败: {e}")
                    raise ModelAPIError(f"模型初始化失败: {str(e)}")
            
        except Exception as e:
            logger.error(f"LLM初始化失败: {e}")
            raise ModelAPIError(f"LLM初始化错误: {str(e)}")
    
    @staticmethod
    @audit_model_call("transcribe")
    @retry(max_attempts=2, delay=2, backoff=2, exceptions=(Exception,))
    def transcribe_realtime(audio_path: Union[str, Path], model_name: Optional[str] = None, batch_size: int = 16384) -> Dict[str, Any]:
        """
        使用DashScope的Paraformer实时转录音频
        
        Args:
            audio_path: 音频文件路径
            model_name: 模型名称，如果为None则从配置获取
            batch_size: 处理的音频数据批次大小，较大的值可能提高长音频处理效率
            
        Returns:
            包含转录文本和时间戳的字典
        """
        try:
            # 从配置加载模型名称（如果未提供）
            config = get_config()
            if model_name is None:
                model_name = config.get('defaults', {}).get('transcription')
                logger.info(f"使用默认转录模型: {model_name}")
            
            # 确保文件路径是绝对路径
            audio_path_str = str(Path(audio_path).resolve())
            logger.info(f"准备转录音频文件: {audio_path_str}")
            
            # 优化音频格式
            optimized_audio = Models._prepare_audio_for_transcription(audio_path_str)
            logger.info(f"使用优化后的音频文件: {optimized_audio}")
            
            # 根据不同模型处理
            if model_name == "paraformer-v2":
                try:
                    # 使用LangChain集成的阿里云ASR服务
                    from langchain_community.document_loaders import AlibabaASRLoader
                    
                    # 获取API密钥
                    api_key = os.environ.get('DASHSCOPE_API_KEY')
                    if not api_key:
                        api_key = config.get('api_keys', {}).get('qwen')
                    
                    if not api_key:
                        raise ValueError("未配置DashScope API密钥")
                    
                    # 使用LangChain的AlibabaASRLoader加载文档
                    loader = AlibabaASRLoader(
                        file_path=optimized_audio,
                        api_key=api_key,
                        model="paraformer-realtime-v2"
                    )
                    transcript_doc = loader.load()[0]  # 返回Document对象列表
                    
                    # 提取转录文本和其他信息
                    full_text = transcript_doc.page_content
                    metadata = transcript_doc.metadata
                    
                    # 构建结果字典
                    result = {
                        "text": full_text,
                        "segments": [],
                        "metadata": metadata
                    }
                    
                    # 如果元数据中包含句子信息，提取为段落
                    if "sentences" in metadata:
                        for sentence in metadata["sentences"]:
                            result["segments"].append({
                                "start": sentence.get("begin_time", 0) / 1000.0,  # 毫秒转秒
                                "end": sentence.get("end_time", 0) / 1000.0,  # 毫秒转秒
                                "text": sentence.get("text", "")
                            })
                    
                    logger.info(f"转录成功，生成 {len(result.get('segments', []))} 个片段，总长度: {len(full_text)} 字符")
                    return result
                except ImportError:
                    # 降级到原生实现
                    logger.warning("找不到LangChain的AlibabaASRLoader，降级到原生实现")
                    return Models._transcribe_with_dashscope(optimized_audio, model_name)
                
            elif "whisper" in model_name:
                # 使用LangChain的OpenAI Whisper集成
                try:
                    from langchain_community.document_loaders import WhisperLoader
                    
                    logger.info(f"使用Whisper模型转录: {model_name}")
                    
                    # 获取API密钥
                    api_key = config.get('api_keys', {}).get('openai')
                    
                    # 使用LangChain的WhisperLoader
                    loader = WhisperLoader(
                        path=optimized_audio,  # 使用优化后的音频文件
                        openai_api_key=api_key,
                        model=model_name
                    )
                    
                    # 加载文档
                    transcript_doc = loader.load()[0]  # 返回Document对象列表
                    
                    # 构建结果
                    result = {
                        "text": transcript_doc.page_content,
                        "segments": [],
                        "metadata": transcript_doc.metadata
                    }
                    
                    logger.info(f"Whisper转录成功，文本长度: {len(result['text'])} 字符")
                    return result
                    
                except ImportError:
                    logger.error("找不到LangChain的WhisperLoader")
                    raise ModelAPIError("Whisper模型依赖缺失")
            else:
                # 默认使用模拟转录（用于测试）
                logger.warning(f"未支持的转录模型: {model_name}，使用模拟转录")
                return Models._mock_transcription(optimized_audio)  # 使用优化后的音频文件
                
        except Exception as e:
            logger.error(f"音频转录失败: {e}")
            raise ModelAPIError(f"音频转录错误: {str(e)}")
    
    @staticmethod
    @audit_model_call("transcribe_file")
    @retry(max_attempts=3, delay=2, backoff=2, exceptions=(Exception,))
    def transcribe_file(audio_path, model_name=None):
        """
        Transcribes a long audio file using the DashScope file transcription API.
        
        Args:
            audio_path (str): Path to the audio file.
            model_name (str, optional): The model name to use for transcription.
                                       Defaults to None, which will use the configured model.
            
        Returns:
            dict: A dictionary containing the transcribed text and segments with timestamps.
        """
        # Load model name from config if not provided
        if model_name is None:
            model_name = config.get("transcription.model_name", "paraformer-v1")
        
        # Convert to absolute path if it's not already
        if not os.path.isabs(audio_path):
            audio_path = os.path.abspath(audio_path)
        
        # Make sure the file exists
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found at {audio_path}")
        
        # Optimize audio format for transcription if needed
        audio_path = Models._prepare_audio_for_transcription(audio_path)
        
        try:
            # Import here to avoid circular imports
            from dashscope.audio.asr import Transcription
            from dashscope import api_key as dashscope_api_key
            
            # Get API key from environment or config
            api_key = os.environ.get("DASHSCOPE_API_KEY") or config.get("dashscope.api_key")
            if api_key:
                dashscope_api_key = api_key
            
            # Get the correct model name based on input model_name
            # 使用最新的模型，无论SDK中是否有定义
            transcription_model = "paraformer-v2"  # 默认使用最新的标准模型
            if "paraformer-8k" in model_name:
                transcription_model = "paraformer-8k-v2"  # 使用8k采样率优化的模型
            elif "paraformer-mtl" in model_name:
                transcription_model = "paraformer-mtl-v1"  # 使用多语言模型
            
            logging.info(f"Using model {transcription_model} for file transcription")
            
            # Structure for storing results
            result = {
                "text": "",
                "segments": []
            }
            
            # 上传音频文件到OSS获取URL
            logging.info(f"Uploading audio file to OSS: {audio_path}")
            from src.utils.oss_utils import OSSClient
            oss_client = OSSClient()
            success, object_key, file_url = oss_client.upload_file(audio_path)
            
            if not success or not file_url:
                raise Exception(f"Failed to upload audio file to OSS: {audio_path}")
            
            logging.info(f"Audio file uploaded successfully, URL: {file_url}")
            
            # Call the DashScope Transcription API with the file URL
            response = Transcription.async_call(
                model=transcription_model,
                file_urls=[file_url]
            )
            
            if not response or not hasattr(response, "output") or not hasattr(response.output, "task_id"):
                raise Exception(f"Failed to start transcription: {response}")
            
            task_id = response.output.task_id
            logging.info(f"Transcription task started with ID: {task_id}")
            
            # Wait for the transcription to complete
            transcription_response = Transcription.wait(task=task_id)
            
            # 清理OSS上的临时文件
            try:
                logging.info(f"Cleaning up temporary file from OSS: {object_key}")
                oss_client.delete_file(object_key)
                logging.info("Temporary file deleted from OSS")
            except Exception as e:
                logging.warning(f"Failed to delete temporary file from OSS: {e}")
            
            if transcription_response.status_code == 200:
                # Process the transcription results
                if hasattr(transcription_response, "output") and "results" in transcription_response.output:
                    for transcription in transcription_response.output["results"]:
                        if transcription["subtask_status"] == "SUCCEEDED":
                            url = transcription["transcription_url"]
                            try:
                                transcription_json = json.loads(urllib.request.urlopen(url).read().decode("utf8"))
                                
                                # Extract text and segments from transcription
                                if "transcripts" in transcription_json:
                                    for transcript in transcription_json["transcripts"]:
                                        if "text" in transcript:
                                            result["text"] += transcript["text"]
                                        
                                        if "sentences" in transcript:
                                            for sentence in transcript["sentences"]:
                                                segment = {
                                                    "text": sentence["text"],
                                                    "start": sentence["begin_time"] / 1000,  # Convert to seconds
                                                    "end": sentence["end_time"] / 1000       # Convert to seconds
                                                }
                                                result["segments"].append(segment)
                            except Exception as e:
                                logging.error(f"Error processing transcription result: {e}")
                                raise Exception(f"Failed to process transcription result: {e}")
            
                logging.info(f"Transcription completed successfully: {len(result['segments'])} segments")
                return result
            else:
                error_msg = getattr(transcription_response.output, "message", "Unknown error")
                logging.error(f"Transcription failed with error: {error_msg}")
                raise Exception(f"Transcription failed: {error_msg}")
        
        except Exception as e:
            logging.error(f"Error in file transcription: {str(e)}")
            raise Exception(f"Failed to transcribe file: {str(e)}")
    
    @staticmethod
    @audit_model_call("translate")
    @retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,))
    def translate(text: str, target_lang: str = "中文", model_name: Optional[str] = None) -> Dict[str, str]:
        """
        使用LangChain翻译文本
        
        Args:
            text: 待翻译文本
            target_lang: 目标语言
            model_name: 模型名称，如果为None则从配置获取
            
        Returns:
            包含翻译文本的字典
        """
        try:
            # 从配置加载模型名称（如果未提供）
            config = get_config()
            if model_name is None:
                model_name = config.get('defaults', {}).get('translation')
                logger.info(f"使用默认翻译模型: {model_name}")
            
            # 获取LLM实例
            llm = Models.get_llm(model_name=model_name)
            
            # 准备翻译提示词
            template = config.get('langchain', {}).get('chains', {}).get('translation', {}).get(
                'prompt_template', "将以下文本翻译成{target_lang}，保持原始格式:\n\n{text}")
            
            # 创建提示模板
            prompt = PromptTemplate(
                template=template,
                input_variables=["text", "target_lang"]
            )
            
            # 创建处理链
            chain = prompt | llm
            
            # 执行翻译
            logger.info(f"开始翻译文本({len(text)} 字符)到 {target_lang}")
            start_time = time.time()
            result = chain.invoke({"text": text, "target_lang": target_lang})
            end_time = time.time()
            
            logger.info(f"翻译完成，耗时: {end_time - start_time:.2f}秒，输出: {len(result)} 字符")
            
            return {"text": result}
                
        except Exception as e:
            logger.error(f"文本翻译失败: {e}")
            raise ModelAPIError(f"翻译错误: {str(e)}")
    
    @staticmethod
    @audit_model_call("summarize")
    @retry(max_attempts=2, delay=1, backoff=2, exceptions=(Exception,))
    def summarize(text: str, max_length: int = 300, model_name: Optional[str] = None) -> Dict[str, Any]:
        """生成文本摘要，使用长上下文文本模型"""
        # 如果没有指定模型，使用配置中的摘要模型
        config = get_config()
        model_name = model_name or config.get('defaults', {}).get('summarization')
        
        # 使用指定的模型处理所有摘要任务
        logger.info(f"使用{model_name}处理摘要，文本长度: {len(text)} 字符")
        return Models._generate_summary_with_long_context_model(text, max_length, model_name)
    
    @staticmethod
    def _generate_summary_with_long_context_model(text: str, max_length: int = 300, model_name: str = None) -> Dict[str, Any]:
        """使用长上下文文本模型生成摘要"""
        start_time = time.time()
        
        try:
            # 获取API密钥和配置
            config = get_config()
            api_key = os.getenv('DASHSCOPE_API_KEY') or config.get('api_keys', {}).get('dashscope')
            
            # 获取模型特定的配置参数
            model_config = config.get('summarization', {}).get('models', {}).get(model_name, {})
            temperature = model_config.get('temperature', 0.3)
            top_p = model_config.get('top_p', 0.8)
            max_tokens = model_config.get('max_tokens', 2000)
            
            logger.info(f"使用模型 {model_name} 生成摘要，参数: temperature={temperature}, top_p={top_p}")
            
            # 根据模型名称选择合适的处理方法
            if model_name.startswith("qwen"):
                # 通义千问系列模型
                chat = ChatTongyi(
                    model=model_name,
                    dashscope_api_key=api_key,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens
                )
            elif model_name.startswith("kimi"):
                # Kimi模型系列 - 未来实现
                # 为未来实现预留接口
                raise NotImplementedError(f"模型 {model_name} 尚未实现")
            else:
                # 默认使用通义千问处理
                logger.warning(f"未知模型类型 {model_name}，使用默认处理方法")
                chat = ChatTongyi(
                    model=model_name,
                    dashscope_api_key=api_key,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens
                )
            
            # 准备提示词
            prompt_template = config.get('langchain', {}).get('chains', {}).get('summarization', {}).get(
                'prompt_template', "请用{max_length}字左右对以下内容进行简明扼要的总结:\n\n{text}")
            
            prompt = prompt_template.format(text=text, max_length=max_length)
            
            # 调用模型
            response = chat.invoke(prompt)
            summary_text = response.content
            
            execution_time = time.time() - start_time
            
            logger.info(f"摘要生成完成，长度: {len(summary_text)} 字符，耗时: {execution_time:.2f}秒")
            
            return {
                "text": summary_text,
                "model": model_name,
                "execution_time": execution_time,
                "parameters": {
                    "temperature": temperature,
                    "top_p": top_p,
                    "max_tokens": max_tokens
                }
            }
            
        except Exception as e:
            logger.error(f"使用{model_name}生成摘要时出错: {str(e)}")
            raise ModelAPIError(f"摘要生成错误: {str(e)}")
    
    @staticmethod
    @audit_model_call("analyze")
    def analyze(text: str, analysis_type: str = "sentiment", model_name: Optional[str] = None) -> Dict[str, Any]:
        """
        使用LangChain进行内容分析
        
        Args:
            text: 待分析文本
            analysis_type: 分析类型 (sentiment, keywords, entities)
            model_name: 模型名称，如果为None则从配置获取
            
        Returns:
            分析结果字典
        """
        try:
            # 从配置加载模型名称（如果未提供）
            config = get_config()
            if model_name is None:
                model_name = config.get('defaults', {}).get('llm')
                logger.info(f"使用默认LLM模型进行分析: {model_name}")
            
            # 获取LLM实例
            llm = Models.get_llm(model_name=model_name)
            
            # 根据分析类型选择提示词
            if analysis_type == "sentiment":
                template = "分析以下文本的情感，返回JSON格式，包含sentiment(positive/negative/neutral)和confidence(0-1):\n\n{text}"
            elif analysis_type == "keywords":
                template = "提取以下文本的5-10个关键词，返回JSON格式数组:\n\n{text}"
            elif analysis_type == "entities":
                template = "识别以下文本中的实体(人名、地名、组织名等)，返回JSON格式数组:\n\n{text}"
            else:
                template = f"对以下文本进行{analysis_type}分析，返回JSON格式:\n\n{{text}}"
            
            # 创建LangChain的提示模板
            prompt = PromptTemplate(
                template=template,
                input_variables=["text"]
            )
            
            # 创建处理链
            chain = prompt | llm
            
            # 执行分析
            logger.info(f"开始{analysis_type}分析，文本长度: {len(text)} 字符")
            start_time = time.time()
            result = chain.invoke({"text": text})
            end_time = time.time()
            
            logger.info(f"{analysis_type}分析完成，耗时: {end_time - start_time:.2f}秒")
            
            # 尝试解析JSON结果
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                logger.warning(f"无法解析分析结果为JSON: {result}")
                return {"result": result, "error": "无法解析为JSON"}
                
        except Exception as e:
            logger.error(f"内容分析失败: {e}")
            raise ModelAPIError(f"内容分析错误: {str(e)}")
    
    @staticmethod
    def _transcribe_with_dashscope(audio_path: str, model_name: str) -> Dict[str, Any]:
        """使用DashScope API直接调用（备用方法）"""
        # 此方法仅作为备用，应优先使用LangChain集成
        try:
            import dashscope
            from dashscope.audio.asr import Recognition
            
            # 获取配置
            config = get_config()
            
            # 获取API密钥
            api_key = os.environ.get('DASHSCOPE_API_KEY')
            if not api_key:
                api_key = config.get('api_keys', {}).get('qwen')
            
            if not api_key:
                raise ValueError("未配置DashScope API密钥")
            
            dashscope.api_key = api_key
            
            # 创建结果存储
            result_dict = {
                'text': '',
                'segments': []
            }
            
            # 定义回调函数
            def recognition_callback(result):
                nonlocal result_dict
                if result.status_code == 200:
                    # 提取文本和时间戳
                    # 获取句子列表
                    sentences = result.get_sentence() or []
                    
                    for sentence in sentences:
                        text = sentence.get('text', '')
                        begin_time = sentence.get('begin_time', 0) / 1000.0  # 毫秒转秒
                        end_time = sentence.get('end_time', 0) / 1000.0  # 毫秒转秒
                        
                        result_dict['segments'].append({
                            'start': begin_time,
                            'end': end_time,
                            'text': text
                        })
                        
                        result_dict['text'] += text
                    
                    logger.info(f"转录回调成功，当前有 {len(result_dict['segments'])} 个片段")
                    return True
                else:
                    error_msg = f"DashScope API错误: {result.status_code} - {result.message}"
                    logger.error(error_msg)
                    return False
            
            # 根据传入的模型名称选择正确的DashScope模型
            if model_name == "paraformer-v2":
                dashscope_model = "paraformer-realtime-v2"  # 使用实时版本
            else:
                dashscope_model = "paraformer-realtime-v1"  # 默认使用v1版本
                
            logger.info(f"使用DashScope模型: {dashscope_model}")
            
            recognition = Recognition(
                model=dashscope_model,  # 使用正确的DashScope模型名称
                callback=recognition_callback,   # 第二个参数是callback
                format='wav',                    # 第三个参数是format
                sample_rate=16000,               # 第四个参数是sample_rate
                channel=1                        # 其他参数作为kwargs传递
            )
            
            # 同步调用方式
            response = recognition.call(audio_path)
            
            # 检查总体结果
            if response.status_code == 200:
                logger.info(f"直接API转录成功，生成 {len(result_dict['segments'])} 个片段，长度: {len(result_dict['text'])}")
                return result_dict
            else:
                error_msg = f"DashScope API错误: {response.status_code} - {response.message}"
                logger.error(error_msg)
                raise ModelAPIError(error_msg)
        except ImportError as e:
            logger.error(f"导入DashScope SDK失败: {e}")
            raise ModelAPIError(f"DashScope SDK缺失: {str(e)}")
        except Exception as e:
            logger.error(f"DashScope调用失败: {e}")
            raise ModelAPIError(f"DashScope错误: {str(e)}")
    
    @staticmethod
    def _mock_transcription(audio_path: Union[str, Path]) -> Dict[str, Any]:
        """生成模拟转录（用于测试）"""
        logger.warning(f"使用模拟转录: {audio_path}")
        
        # 生成模拟的段落（用于测试）
        segments = [
            {"start": 0.0, "end": 5.0, "text": "这是模拟转录的第一句话。"},
            {"start": 5.1, "end": 10.0, "text": "这是第二句话，用于测试。"},
            {"start": 10.1, "end": 15.0, "text": "这是最后一句话，谢谢使用。"}
        ]
        
        return {
            "text": full_text,
            "segments": segments,
            "metadata": {"mock": True, "file": str(audio_path)}
        }
    
    @staticmethod
    def _prepare_audio_for_transcription(audio_path: str) -> str:
        """准备适合转录的音频（转换为16kHz单声道WAV）"""
        # 检查文件是否存在
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"找不到音频文件: {audio_path}")
            
        # 获取配置
        config = get_config()
        
        # 使用新的目录结构
        temp_dir = config.get('storage', {}).get('temp_dir', './temp')
        convert_dir = os.path.join(temp_dir, "converted_audio")
        
        # 确保临时目录存在
        os.makedirs(convert_dir, exist_ok=True)
        
        # 输出文件路径
        output_filename = f"{os.path.splitext(os.path.basename(audio_path))[0]}_16k.wav"
        output_path = os.path.join(convert_dir, output_filename)
        
        # 如果已经存在转换后的文件，直接返回
        if os.path.exists(output_path):
            logger.info(f"使用已存在的转换文件: {output_path}")
            return output_path
            
        # 如果文件不存在，进行转换
        try:
            # 使用librosa加载音频并重采样
            logger.info(f"转换音频: {audio_path} -> {output_path}")
            y, sr = librosa.load(audio_path, sr=16000, mono=True)
            sf.write(output_path, y, 16000)
            return output_path
        except Exception as e:
            logger.error(f"音频转换失败: {e}")
            raise RuntimeError(f"音频转换失败: {e}")
    
    @staticmethod
    @retry(max_attempts=2, delay=1, backoff=2, exceptions=(Exception,))
    def complete(prompt: str, model_name: Optional[str] = None, max_tokens: int = 1000, temperature: float = 0.3) -> str:
        """
        通用文本补全接口，用于生成文本回复
        
        Args:
            prompt: 提示词
            model_name: 模型名称，未指定时使用配置中的默认模型
            max_tokens: 最大生成令牌数
            temperature: 温度参数，控制生成的随机性
            
        Returns:
            生成的文本
        """
        # 如果没有指定模型，使用配置中的摘要模型
        config = get_config()
        model_name = model_name or config.get('defaults', {}).get('summarization')
        
        try:
            logger.info(f"使用{model_name}进行文本补全，提示词长度: {len(prompt)}")
            
            # 获取API密钥和配置
            api_key = os.getenv('DASHSCOPE_API_KEY') or config.get('api_keys', {}).get('dashscope')
            
            # 根据模型名称选择合适的处理方法
            if model_name.startswith("qwen"):
                # 通义千问系列模型
                chat = ChatTongyi(
                    model=model_name,
                    dashscope_api_key=api_key,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
            else:
                # 默认使用通义千问处理
                logger.warning(f"未知模型类型 {model_name}，使用默认处理方法")
                chat = ChatTongyi(
                    model=model_name,
                    dashscope_api_key=api_key,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
            
            # 调用模型
            response = chat.invoke(prompt)
            result_text = response.content
            
            logger.info(f"文本补全完成，生成文本长度: {len(result_text)}")
            return result_text
            
        except Exception as e:
            logger.error(f"文本补全失败: {e}")
            raise 