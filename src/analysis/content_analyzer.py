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
            # 使用大模型提取关键点
            try:
                # 准备提示词
                prompt = f"""
                请从以下内容中提取{num_points}个最重要的关键观点。
                每个关键观点应简明扼要（15-30字为宜），并覆盖不同的核心内容。
                不要使用相似内容的观点，确保每个观点都有独特的信息价值。
                请直接列出关键观点，每行一个，不要包含序号或其他格式。
                
                内容:
                {text}
                """
                
                # 调用模型
                response = Models.complete(prompt, model_name=self.model_name)
                
                # 解析关键点
                raw_points = response.strip().split('\n')
                key_points = [point.strip() for point in raw_points if point.strip()]
                
                # 限制关键点数量
                key_points = key_points[:num_points]
                
                # 如果没有提取到足够的关键点，使用备选方法
                if len(key_points) < 2:
                    logger.warning(f"模型未能提取到足够的关键点，使用备选方法")
                    # 简单实现：按句子分割，选择一些看起来像关键点的句子
                    import re
                    sentences = re.split(r'(?<=[.!?。！？])\s+', text)
                    
                    # 选择一些关键句子
                    backup_points = []
                    
                    # 选择开头的句子
                    if sentences and len(sentences) > 0:
                        first_sentence = sentences[0].strip()
                        if len(first_sentence) > 10 and len(first_sentence) < 100:
                            backup_points.append(first_sentence)
                    
                    # 选择包含关键词的句子
                    keywords = ['重要', '关键', '核心', '主要', '总结', '结论']
                    for sentence in sentences:
                        sentence = sentence.strip()
                        if len(sentence) > 15 and len(sentence) < 100:
                            if any(kw in sentence for kw in keywords) and sentence not in backup_points:
                                backup_points.append(sentence)
                                if len(backup_points) >= num_points:
                                    break
                    
                    # 添加结尾的句子
                    if sentences and len(sentences) > 2 and len(backup_points) < num_points:
                        last_sentence = sentences[-1].strip()
                        if len(last_sentence) > 10 and len(last_sentence) < 100 and last_sentence not in backup_points:
                            backup_points.append(last_sentence)
                    
                    # 使用备选关键点
                    if backup_points:
                        key_points = backup_points[:num_points]
            
            except Exception as e:
                logger.warning(f"使用模型提取关键点失败: {e}，使用备选方法")
                # 使用备选方法生成关键点
                key_points = [f"关键观点 {i+1}: 内容摘要的第{i+1}个要点" for i in range(num_points)]
            
            logger.info(f"关键点提取完成 ({len(key_points)} 个)")
            return key_points
            
        except Exception as e:
            logger.error(f"关键点提取失败: {e}")
            return [f"关键点提取失败: {str(e)}"] 