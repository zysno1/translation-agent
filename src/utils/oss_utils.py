#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
阿里云OSS工具类
负责文件上传和URL生成
"""

import os
import uuid
import time
from typing import Optional, Dict, Any, Tuple
from pathlib import Path

import oss2

from src.config.config_manager import get_config
from src.utils.log import get_logger

# 获取日志器
logger = get_logger()


class OSSClient:
    """阿里云OSS客户端工具类"""
    
    def __init__(self, access_key_id: Optional[str] = None, access_key_secret: Optional[str] = None, 
                 endpoint: Optional[str] = None, bucket_name: Optional[str] = None):
        """
        初始化OSS客户端
        
        Args:
            access_key_id: 访问密钥ID，默认从配置获取
            access_key_secret: 访问密钥Secret，默认从配置获取
            endpoint: 访问域名，默认从配置获取
            bucket_name: 存储桶名称，默认从配置获取
        """
        config = get_config()
        oss_config = config.get('storage', {}).get('oss', {})
        
        # 从配置或环境变量获取OSS认证信息
        self.access_key_id = access_key_id or os.environ.get('OSS_ACCESS_KEY_ID') or oss_config.get('access_key_id')
        self.access_key_secret = access_key_secret or os.environ.get('OSS_ACCESS_KEY_SECRET') or oss_config.get('access_key_secret')
        self.endpoint = endpoint or os.environ.get('OSS_ENDPOINT') or oss_config.get('endpoint')
        self.bucket_name = bucket_name or os.environ.get('OSS_BUCKET_NAME') or oss_config.get('bucket_name')
        
        # 验证配置完整性
        if not all([self.access_key_id, self.access_key_secret, self.endpoint, self.bucket_name]):
            missing = []
            if not self.access_key_id: missing.append("access_key_id")
            if not self.access_key_secret: missing.append("access_key_secret")
            if not self.endpoint: missing.append("endpoint")
            if not self.bucket_name: missing.append("bucket_name")
            
            raise ValueError(f"OSS配置不完整，缺少以下配置项: {', '.join(missing)}")
        
        # 初始化OSS客户端
        self.auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)
        
        logger.info(f"OSS客户端初始化成功，Endpoint: {self.endpoint}, 存储桶: {self.bucket_name}")
    
    def upload_file(self, local_file_path: str, object_key: Optional[str] = None) -> Tuple[bool, str, str]:
        """
        上传文件到OSS
        
        Args:
            local_file_path: 本地文件路径
            object_key: OSS中的对象键（文件路径），如果为None则自动生成
            
        Returns:
            (成功标志, 对象键, 文件URL)
        """
        try:
            local_file_path = str(Path(local_file_path).resolve())
            
            # 检查文件是否存在
            if not os.path.exists(local_file_path):
                raise FileNotFoundError(f"要上传的文件不存在: {local_file_path}")
            
            # 如果没有提供对象键，则生成一个唯一的对象键
            if object_key is None:
                file_ext = os.path.splitext(local_file_path)[1]
                timestamp = int(time.time())
                random_id = str(uuid.uuid4()).replace('-', '')[:8]
                file_name = os.path.basename(local_file_path)
                base_name = os.path.splitext(file_name)[0]
                
                # 将文件路径组织在audio文件夹下，并使用原始文件名加时间戳和随机ID
                object_key = f"audio/{base_name}_{timestamp}_{random_id}{file_ext}"
            
            # 上传文件
            logger.info(f"开始上传文件到OSS, 本地路径: {local_file_path}, 对象键: {object_key}")
            self.bucket.put_object_from_file(object_key, local_file_path)
            
            # 生成URL（公开访问URL，有效期1小时）
            url = self.bucket.sign_url('GET', object_key, 3600)
            
            logger.info(f"文件上传成功，对象键: {object_key}, URL: {url}")
            return True, object_key, url
            
        except Exception as e:
            logger.error(f"文件上传失败: {e}")
            return False, "", ""
    
    def download_file(self, object_key: str, local_file_path: str) -> bool:
        """
        从OSS下载文件
        
        Args:
            object_key: OSS中的对象键（文件路径）
            local_file_path: 本地保存路径
            
        Returns:
            是否下载成功
        """
        try:
            # 确保目标目录存在
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            
            # 下载文件
            logger.info(f"开始从OSS下载文件, 对象键: {object_key}, 本地路径: {local_file_path}")
            self.bucket.get_object_to_file(object_key, local_file_path)
            
            logger.info(f"文件下载成功: {local_file_path}")
            return True
            
        except Exception as e:
            logger.error(f"文件下载失败: {e}")
            return False
    
    def delete_file(self, object_key: str) -> bool:
        """
        删除OSS中的文件
        
        Args:
            object_key: OSS中的对象键（文件路径）
            
        Returns:
            是否删除成功
        """
        try:
            logger.info(f"开始删除OSS文件, 对象键: {object_key}")
            self.bucket.delete_object(object_key)
            
            logger.info(f"文件删除成功: {object_key}")
            return True
                
        except Exception as e:
            logger.error(f"文件删除失败: {e}")
            return False

    def get_file_url(self, object_key: str, expires: int = 3600) -> str:
        """
            获取OSS文件的临时访问URL
            
            Args:
                object_key: OSS中的对象键（文件路径）
                expires: URL有效期（秒），默认1小时
            
            Returns:
                文件访问URL
            """
        try:
            url = self.bucket.sign_url('GET', object_key, expires)
            logger.info(f"生成临时访问URL: {url}, 有效期: {expires}秒")
            return url
            
        except Exception as e:
            logger.error(f"生成URL失败: {e}")
            return "" 