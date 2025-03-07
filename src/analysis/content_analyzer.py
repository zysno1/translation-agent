# -*- coding: utf-8 -*-

"""
内容分析模块
负责文本摘要和关键点提取
"""

from typing import List, Optional

from src.config.config_manager import get_config
from src.utils.log import get_logger
from src.models.models import Models

# 获取日志器
logger = get_logger()


class ContentAnalyzer:
    """内容分析器"""
    
    def __init__(self, model_name: Optional[str] = None):
        """
        初始化内容分析器
        
        Args:
            model_name: 分析模型名称，默认从配置获取
        """
        config = get_config()
        self.config = config
        
        # 分析模型
        self.model_name = model_name or config.get('defaults', {}).get('summarization')
        
        logger.info(f"内容分析器初始化，使用模型: {self.model_name}")
    
    def generate_summary(self, text: str, max_length: int = 200) -> str:
        """
        生成文本摘要
        
        Args:
            text: 待摘要文本
            max_length: 摘要最大长度
            
        Returns:
            摘要文本
        """
        logger.info(f"开始生成摘要 ({len(text)} 字符)")
        
        try:
            # 临时实现：使用模拟方式返回摘要
            try:
                # 尝试使用LangChain模型生成摘要
                summary = Models.summarize(text, max_length=max_length, model_name=self.model_name)
            except Exception as e:
                logger.warning(f"模型摘要生成失败，使用模拟摘要: {e}")
                summary = f"[模拟摘要] 这是一个关于'{text[:20]}...'的内容摘要，长度约{max_length}字。"
            
            logger.info(f"摘要生成完成 ({len(summary)} 字符)")
            return summary
            
        except Exception as e:
            logger.error(f"摘要生成失败: {e}")
            return f"[摘要生成失败: {str(e)}]"
    
    def extract_key_points(self, text: str, num_points: int = 5) -> List[str]:
        """
        提取文本关键点
        
        Args:
            text: 文本内容
            num_points: 关键点数量
            
        Returns:
            关键点列表
        """
        logger.info(f"开始提取关键点 ({len(text)} 字符)")
        
        try:
            # 临时实现：返回模拟关键点
            key_points = [f"关键点 {i+1}: 这是从文本中提取的示例关键点" for i in range(num_points)]
            
            logger.info(f"关键点提取完成 ({len(key_points)} 个)")
            return key_points
            
        except Exception as e:
            logger.error(f"关键点提取失败: {e}")
            return [f"关键点提取失败: {str(e)}"] 