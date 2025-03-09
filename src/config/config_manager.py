# -*- coding: utf-8 -*-

"""
配置管理器
负责加载、解析和提供应用配置
"""

import os
import yaml
from pathlib import Path
import logging
from typing import Dict, Any, Optional

# 全局配置对象
_CONFIG = {}

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    加载配置文件
    
    Args:
        config_path: 配置文件路径，如果为None则使用默认路径
        
    Returns:
        配置字典
    """
    global _CONFIG
    
    # 默认配置路径
    if config_path is None:
        config_path = os.environ.get('CONFIG_PATH', 'config.yaml')
    
    config_path = Path(config_path)
    
    # 检查配置文件是否存在
    if not config_path.exists():
        # 如果配置文件不存在，创建默认配置
        _CONFIG = _create_default_config()
        
        # 保存默认配置
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(_CONFIG, f, default_flow_style=False, allow_unicode=True)
            
        logging.info(f"创建默认配置文件: {config_path}")
    else:
        # 加载现有配置
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                _CONFIG = yaml.safe_load(f)
            logging.info(f"加载配置文件: {config_path}")
        except Exception as e:
            logging.error(f"配置文件加载失败: {e}")
            _CONFIG = _create_default_config()
    
    # 处理环境变量替换
    _process_env_vars(_CONFIG)
    
    return _CONFIG


def get_config() -> Dict[str, Any]:
    """
    获取当前配置
    
    Returns:
        配置字典
    """
    global _CONFIG
    
    if not _CONFIG:
        return load_config()
    
    return _CONFIG


def _create_default_config() -> Dict[str, Any]:
    """
    创建默认配置
    
    Returns:
        默认配置字典
    """
    return {
        'defaults': {
            'transcription': 'paraformer-v2',  # 默认转写模型
            'translation': 'qwen-max',         # 默认翻译模型
            'summarization': 'qwen-plus',      # 默认摘要模型
            'output_format': 'md',             # 默认输出格式
        },
        'environment': 'personal',  # 可选: personal, work, test
        
        # API密钥 (从环境变量加载)
        'api_keys': {
            'openai': '${OPENAI_API_KEY}',
            'baidu': '${BAIDU_API_KEY}',
            'qwen': '${QWEN_API_KEY}',
        },
        
        # 存储路径
        'storage': {
            # 临时文件目录
            'temp_dir': './temp',
            'audio_dir': './temp/audio',
            'video_dir': './temp/video',
            'downloads_dir': './temp/downloads',
            'converted_audio_dir': './temp/converted_audio',
            
            # 数据目录
            'data_dir': './data',
            'transcripts_dir': './data/transcripts',
            'translations_dir': './data/translations',
            'summaries_dir': './data/summaries',
            'processed_dir': './data/processed',
            
            # 报告目录
            'reports_dir': './reports',
            
            # 日志目录
            'logs_dir': './logs',
            
            # OSS配置
            'oss': {
                'bucket': '${OSS_BUCKET_NAME}',
                'access_key_id': '${OSS_ACCESS_KEY_ID}',
                'access_key_secret': '${OSS_ACCESS_KEY_SECRET}',
                'endpoint': '${OSS_ENDPOINT}',
                'prefix': 'audio'
            },
        },
        
        # 日志配置
        'logging': {
            'level': 'INFO',
            'max_size': '10MB',
            'retention_days': 7,
            'format': '[%(asctime)s] [%(session_id)s] %(levelname)s - %(message)s',
        },
        
        # LangChain配置
        'langchain': {
            'chains': {
                'translation': {
                    'prompt_template': '将以下文本翻译成{target_lang}，保持原始格式:\n\n{text}'
                },
                'summarization': {
                    'prompt_template': '用{max_length}字左右总结以下内容:\n\n{text}'
                }
            }
        }
    }


def _process_env_vars(config: Dict[str, Any]) -> None:
    """
    处理配置中的环境变量引用
    替换${ENV_VAR}格式的值为实际环境变量值
    
    Args:
        config: 配置字典（递归处理）
    """
    for key, value in config.items():
        if isinstance(value, dict):
            _process_env_vars(value)
        elif isinstance(value, str) and value.startswith('${') and value.endswith('}'):
            env_var = value[2:-1]
            env_value = os.environ.get(env_var)
            if env_value is not None:
                config[key] = env_value 