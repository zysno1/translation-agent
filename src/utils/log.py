# -*- coding: utf-8 -*-

"""
日志模块
提供统一的日志记录功能
"""

import os
import logging
import uuid
from logging.handlers import RotatingFileHandler
from typing import Optional

from src.config.config_manager import get_config

# 全局日志对象
_LOGGER = None


class SessionAdapter(logging.LoggerAdapter):
    """
    会话日志适配器
    为每个日志消息添加会话ID
    """
    def process(self, msg, kwargs):
        """处理日志消息，添加会话ID"""
        if 'extra' not in kwargs:
            kwargs['extra'] = {}
        if 'session_id' not in kwargs['extra']:
            kwargs['extra']['session_id'] = getattr(self, 'session_id', 'MAIN')
        return msg, kwargs


def setup_logger(log_level: Optional[str] = None, log_dir: Optional[str] = None, session_id: Optional[str] = None) -> logging.LoggerAdapter:
    """
    设置日志器
    
    Args:
        log_level: 日志级别，默认从配置文件获取
        log_dir: 日志目录，默认从配置文件获取，若为None则使用'logs'
        session_id: 会话ID，默认自动生成
        
    Returns:
        日志适配器
    """
    global _LOGGER
    
    config = get_config()
    
    # 默认值
    if log_level is None:
        log_level = config.get('logging', {}).get('level', 'INFO')
    
    if log_dir is None:
        log_dir = config.get('logging', {}).get('log_dir', 'logs')
    
    # 确保日志目录存在
    os.makedirs(log_dir, exist_ok=True)
    
    # 日志格式
    log_format = config.get('logging', {}).get('format', 
                                              '[%(asctime)s] [%(session_id)s] %(levelname)s - %(message)s')
    formatter = logging.Formatter(fmt=log_format, datefmt='%Y-%m-%d %H:%M:%S')
    
    # 创建日志器
    logger = logging.getLogger('youtube_processor')
    
    # 避免重复配置
    if _LOGGER is not None:
        return _LOGGER
    
    # 清除已有处理器
    if logger.handlers:
        logger.handlers.clear()
    
    # 设置日志级别
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)
    
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 文件处理器参数
    max_size = config.get('logging', {}).get('max_size', '10MB')
    max_size_bytes = _parse_size(max_size)
    retention_days = config.get('logging', {}).get('retention_days', 7)
    
    # 应用日志文件处理器（所有日志）
    app_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, 'app.log'),
        maxBytes=max_size_bytes,
        backupCount=retention_days
    )
    app_handler.setFormatter(formatter)
    logger.addHandler(app_handler)
    
    # DEBUG日志文件处理器
    debug_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, 'debug.log'),
        maxBytes=max_size_bytes,
        backupCount=retention_days
    )
    debug_handler.setFormatter(formatter)
    debug_handler.setLevel(logging.DEBUG)
    # 只记录DEBUG级别的日志
    debug_handler.addFilter(lambda record: record.levelno == logging.DEBUG)
    logger.addHandler(debug_handler)
    
    # ERROR日志文件处理器（包括ERROR和CRITICAL级别）
    error_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, 'error.log'),
        maxBytes=max_size_bytes,
        backupCount=retention_days
    )
    error_handler.setFormatter(formatter)
    error_handler.setLevel(logging.ERROR)
    logger.addHandler(error_handler)
    
    # 创建会话ID
    if session_id is None:
        session_id = str(uuid.uuid4())[:8]
    
    # 创建适配器
    adapter = SessionAdapter(logger, {'session_id': session_id})
    _LOGGER = adapter
    
    adapter.info(f"日志系统初始化完成 (级别: {log_level}, 会话ID: {session_id})")
    return adapter


def get_logger(session_id: Optional[str] = None) -> logging.LoggerAdapter:
    """
    获取日志器
    
    Args:
        session_id: 会话ID，若为None则使用现有会话ID
        
    Returns:
        日志适配器
    """
    global _LOGGER
    
    if _LOGGER is None:
        return setup_logger(session_id=session_id)
    
    if session_id is not None:
        new_adapter = SessionAdapter(_LOGGER.logger, {'session_id': session_id})
        return new_adapter
    
    return _LOGGER


def _parse_size(size_str: str) -> int:
    """
    解析大小字符串为字节数
    
    Args:
        size_str: 大小字符串，如"10MB"
        
    Returns:
        字节数
    """
    size_str = size_str.strip().upper()
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024**2,
        'GB': 1024**3
    }
    
    for unit, multiplier in units.items():
        if size_str.endswith(unit):
            try:
                value = float(size_str[:-len(unit)])
                return int(value * multiplier)
            except ValueError:
                pass
    
    # 默认为字节
    try:
        return int(size_str)
    except ValueError:
        return 10 * 1024 * 1024  # 默认10MB 