# -*- coding: utf-8 -*-

"""
文件工具模块
提供文件操作相关的工具函数
"""

import os
import json
import shutil
import tempfile
from pathlib import Path
from typing import Union, Dict, Any, List, Optional
import re

from src.utils.log import get_logger

# 获取日志器
logger = get_logger()


def ensure_dir(directory: Union[str, Path]) -> str:
    """
    确保目录存在，如果不存在则创建
    
    Args:
        directory: 目录路径
        
    Returns:
        创建的目录路径
    """
    directory = Path(directory)
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
        logger.debug(f"创建目录: {directory}")
    return str(directory)


def get_temp_dir(prefix: str = "youtube_") -> str:
    """
    获取临时目录
    
    Args:
        prefix: 目录前缀
        
    Returns:
        临时目录路径
    """
    temp_dir = tempfile.mkdtemp(prefix=prefix)
    logger.debug(f"创建临时目录: {temp_dir}")
    return temp_dir


def safe_filename(filename: str, prefix: str = None, max_length: int = 200) -> str:
    """
    生成安全的文件名（去除非法字符）
    
    Args:
        filename: 原始文件名
        prefix: 文件名前缀，指示文件类型（如transcript、translation、summary等）
        max_length: 文件名最大长度
        
    Returns:
        安全的文件名
    """
    # 替换非法字符为下划线
    # 更全面的非法字符清理
    invalid_chars = '<>:"/\\|?*\t\n\r\x0b\x0c'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # 使用正则表达式替换所有非字母数字和基本标点的字符
    filename = re.sub(r'[^\w\-. ]', '_', filename)
    
    # 将多个连续下划线替换为单个下划线
    filename = re.sub(r'_+', '_', filename)
    
    # 将空格替换为下划线（避免命令行问题）
    filename = filename.replace(' ', '_')
    
    # 去除文件名前后的下划线或点
    filename = filename.strip('_.')
    
    # 添加前缀（如果提供）- 向后兼容保留此功能，但不再依赖
    if prefix:
        # 确保前缀以下划线结尾
        if not prefix.endswith('_'):
            prefix = f"{prefix}_"
        filename = f"{prefix}{filename}"
    
    # 限制长度
    if len(filename) > max_length:
        filename = filename[:max_length-3] + "..."
    
    # 确保文件名不为空
    if not filename:
        filename = "untitled"
        if prefix:
            filename = f"{prefix}{filename}"
    
    return filename


def read_text_file(file_path: Union[str, Path], encoding: str = 'utf-8') -> str:
    """
    读取文本文件
    
    Args:
        file_path: 文件路径
        encoding: 文件编码
        
    Returns:
        文件内容
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
        return content
    except Exception as e:
        logger.error(f"读取文件失败 {file_path}: {e}")
        raise


def write_text_file(content: str, file_path: Union[str, Path], encoding: str = 'utf-8') -> str:
    """
    写入文本文件
    
    Args:
        content: 文件内容
        file_path: 文件路径
        encoding: 文件编码
        
    Returns:
        文件路径
    """
    try:
        # 确保目录存在
        ensure_dir(os.path.dirname(file_path))
        
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
        
        logger.debug(f"写入文件: {file_path}")
        return str(file_path)
    except Exception as e:
        logger.error(f"写入文件失败 {file_path}: {e}")
        raise


def read_json_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    读取JSON文件
    
    Args:
        file_path: 文件路径
        
    Returns:
        JSON数据
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"读取JSON文件失败 {file_path}: {e}")
        raise


def write_json_file(data: Dict[str, Any], file_path: Union[str, Path], indent: int = 2) -> str:
    """
    写入JSON文件
    
    Args:
        data: JSON数据
        file_path: 文件路径
        indent: 缩进空格数
        
    Returns:
        文件路径
    """
    try:
        # 确保目录存在
        ensure_dir(os.path.dirname(file_path))
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
        
        logger.debug(f"写入JSON文件: {file_path}")
        return str(file_path)
    except Exception as e:
        logger.error(f"写入JSON文件失败 {file_path}: {e}")
        raise


def list_files(directory: Union[str, Path], pattern: str = "*") -> List[str]:
    """
    列出目录中的文件
    
    Args:
        directory: 目录路径
        pattern: 文件匹配模式
        
    Returns:
        文件路径列表
    """
    directory = Path(directory)
    files = [str(f) for f in directory.glob(pattern) if f.is_file()]
    return files


def remove_file(file_path: Union[str, Path]) -> bool:
    """
    删除文件
    
    Args:
        file_path: 文件路径
        
    Returns:
        是否成功删除
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.debug(f"删除文件: {file_path}")
            return True
        return False
    except Exception as e:
        logger.error(f"删除文件失败 {file_path}: {e}")
        return False


def remove_dir(directory: Union[str, Path], recursive: bool = True) -> bool:
    """
    删除目录
    
    Args:
        directory: 目录路径
        recursive: 是否递归删除
        
    Returns:
        是否成功删除
    """
    try:
        if os.path.exists(directory):
            if recursive:
                shutil.rmtree(directory)
            else:
                os.rmdir(directory)
            logger.debug(f"删除目录: {directory}")
            return True
        return False
    except Exception as e:
        logger.error(f"删除目录失败 {directory}: {e}")
        return False


def copy_file(src_path: Union[str, Path], dest_path: Union[str, Path]) -> str:
    """
    复制文件
    
    Args:
        src_path: 源文件路径
        dest_path: 目标文件路径
        
    Returns:
        目标文件路径
    """
    try:
        # 确保目标目录存在
        ensure_dir(os.path.dirname(dest_path))
        
        shutil.copy2(src_path, dest_path)
        logger.debug(f"复制文件: {src_path} -> {dest_path}")
        return str(dest_path)
    except Exception as e:
        logger.error(f"复制文件失败 {src_path} -> {dest_path}: {e}")
        raise


def get_file_extension(file_path: Union[str, Path]) -> str:
    """
    获取文件扩展名（不包含点号）
    
    Args:
        file_path: 文件路径
        
    Returns:
        文件扩展名
    """
    return os.path.splitext(str(file_path))[1][1:]


def get_file_size(file_path: Union[str, Path]) -> int:
    """
    获取文件大小（字节）
    
    Args:
        file_path: 文件路径
        
    Returns:
        文件大小（字节）
    """
    return os.path.getsize(file_path)


def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小
    
    Args:
        size_bytes: 文件大小（字节）
        
    Returns:
        格式化后的文件大小字符串
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0 or unit == 'TB':
            break
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} {unit}" 