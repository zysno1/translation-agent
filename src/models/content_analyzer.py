# -*- coding: utf-8 -*-

"""
内容分析模块
提供对转录文本内容的分析能力，包括摘要生成、关键点提取等
"""

import os
from typing import Dict, List, Optional, Union, Any
import json
from pathlib import Path

from src.config.config_manager import get_config
from src.utils.log import get_logger
from src.models.models import Models

# 获取日志器
logger = get_logger()


class ContentAnalyzer:
    """内容分析器，提供对转录文本的分析功能"""
    
    def __init__(self, model_name: Optional[str] = None):
        """
        初始化内容分析器
        
        Args:
            model_name: 使用的模型名称，如果为None则从配置获取
        """
        # 从配置加载模型名称（如果未提供）
        config = get_config()
        self.model_name = model_name or config.get('defaults', {}).get('llm')
        logger.info(f"初始化内容分析器，使用模型: {self.model_name}")
    
    def generate_summary(self, text: str, max_length: int = 200) -> Dict[str, Any]:
        """
        生成文本摘要
        
        Args:
            text: 待摘要的文本
            max_length: 摘要最大长度
            
        Returns:
            包含摘要的字典
        """
        try:
            logger.info(f"生成摘要，文本长度: {len(text)}, 最大摘要长度: {max_length}")
            
            # 调用模型生成摘要
            summary = Models.summarize(text, max_length, self.model_name)
            
            logger.info(f"摘要生成成功，长度: {len(summary)}")
            
            return {
                'summary': summary,
                'length': len(summary)
            }
        except Exception as e:
            logger.error(f"摘要生成失败: {e}")
            return {'summary': f"摘要生成失败: {str(e)}", 'error': str(e)}
    
    def extract_key_points(self, text: str, num_points: int = 5) -> Dict[str, Any]:
        """
        提取文本中的关键点
        
        Args:
            text: 转录文本
            num_points: 要提取的关键点数量
            
        Returns:
            包含关键点列表的字典
        """
        try:
            logger.info(f"提取关键点，文本长度: {len(text)}, 关键点数量: {num_points}")
            
            # 获取LLM
            llm = Models.get_llm(self.model_name)
            
            # 创建提示
            prompt = f"""
            从以下文本中提取{num_points}个最重要的关键点。
            每个关键点应该简洁明了，并以有序列表的形式呈现，不要包含额外的解释。
            
            文本内容:
            {text}
            
            关键点:
            """
            
            response = llm(prompt)
            
            # 解析响应中的关键点
            key_points = []
            for line in response.split('\n'):
                line = line.strip()
                if line and (line.startswith('-') or 
                             line.startswith('•') or 
                             line.startswith('*') or
                             (line[0].isdigit() and ')' in line[:3] or '.' in line[:3])):
                    # 移除序号或列表符号
                    point = line
                    for prefix in ['-', '•', '*']:
                        if point.startswith(prefix):
                            point = point[len(prefix):].strip()
                            break
                    
                    if point[0].isdigit() and ('.' in point[:3] or ')' in point[:3]):
                        point = point[point.find('.')+1:].strip() if '.' in point[:3] else point[point.find(')')+1:].strip()
                    
                    key_points.append(point)
            
            logger.info(f"关键点提取成功，找到 {len(key_points)} 个关键点")
            
            return {
                'key_points': key_points,
                'count': len(key_points)
            }
        except Exception as e:
            logger.error(f"关键点提取失败: {e}")
            return {'key_points': [], 'error': str(e)}
    
    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """
        分析文本情感
        
        Args:
            text: 转录文本
            
        Returns:
            包含情感分析结果的字典
        """
        try:
            logger.info(f"分析情感，文本长度: {len(text)}")
            
            # 获取LLM
            llm = Models.get_llm(self.model_name)
            
            # 创建提示
            prompt = f"""
            请分析以下文本的情感倾向，并给出一个从-1到1的分数，其中：
            -1表示非常消极
            0表示中性
            1表示非常积极
            
            同时，请用一句话描述文本的主要情感色彩。
            
            文本内容:
            {text}
            
            回答格式：
            {{
                "score": 情感分数,
                "description": "情感描述"
            }}
            """
            
            response = llm(prompt)
            
            # 尝试解析JSON响应
            try:
                # 提取响应中的JSON部分
                json_str = response
                if '```json' in response:
                    json_str = response.split('```json')[1].split('```')[0].strip()
                elif '```' in response:
                    json_str = response.split('```')[1].split('```')[0].strip()
                
                result = json.loads(json_str)
                logger.info(f"情感分析成功，分数: {result.get('score')}")
                return result
            except json.JSONDecodeError:
                # 如果无法解析JSON，尝试手动解析
                logger.warning(f"无法解析JSON响应，尝试手动解析: {response}")
                
                score = 0
                description = "无法确定"
                
                # 尝试提取分数
                for line in response.split('\n'):
                    if 'score' in line.lower() and ':' in line:
                        try:
                            score_str = line.split(':')[1].strip().rstrip(',').strip('"')
                            score = float(score_str)
                        except (ValueError, IndexError):
                            pass
                    
                    # 尝试提取描述
                    if 'description' in line.lower() and ':' in line:
                        try:
                            description = line.split(':')[1].strip().rstrip(',').strip('"')
                        except IndexError:
                            pass
                
                return {
                    'score': score,
                    'description': description
                }
            
        except Exception as e:
            logger.error(f"情感分析失败: {e}")
            return {'score': 0, 'description': f"分析失败: {str(e)}", 'error': str(e)}
    
    def perform_full_analysis(self, text: str) -> Dict[str, Any]:
        """
        对文本执行完整分析，包括摘要、关键点和情感分析
        
        Args:
            text: 转录文本
            
        Returns:
            包含所有分析结果的字典
        """
        logger.info(f"执行完整内容分析，文本长度: {len(text)}")
        
        results = {
            'text_length': len(text)
        }
        
        # 生成摘要
        summary_result = self.generate_summary(text)
        results['summary'] = summary_result
        
        # 提取关键点
        key_points_result = self.extract_key_points(text)
        results['key_points'] = key_points_result
        
        # 分析情感
        sentiment_result = self.analyze_sentiment(text)
        results['sentiment'] = sentiment_result
        
        logger.info("完整内容分析完成")
        return results 