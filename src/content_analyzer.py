from typing import Dict, Any
from datetime import datetime
from log import logger
from models import Models

class ContentAnalyzer:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_summary(self, text: str, original_lang: str = 'en', max_length: int = 300) -> Dict[str, Any]:
        """
        生成文本摘要。

        Args:
            text: 要摘要的文本内容
            original_lang: 原始语言
            max_length: 摘要的最大长度（字符数）

        Returns:
            包含摘要内容的字典
        """
        logger.info(f"开始生成摘要 ({len(text)} 字符)")
        try:
            # 使用首选的LLM生成摘要
            summary_result = Models.summarize(text, max_length, self.model_name)
            summary = summary_result["text"]
            
            logger.info(f"摘要生成完成 ({len(summary)} 字符)")
            
            # 构建返回结果
            result = {
                "summary": summary,
                "original_language": original_lang,
                "summary_language": "zh" if original_lang != "zh" else original_lang,
                "model": summary_result["model"],
                "timestamp": datetime.utcnow().isoformat(),
                "original_length": len(text),
                "summary_length": len(summary)
            }
            
            # 添加元数据
            if "execution_time" in summary_result:
                result["execution_time"] = summary_result["execution_time"]
                
            return result
        except Exception as e:
            logger.error(f"摘要生成失败: {e}")
            # 即使出错也要返回一些内容，不能导致整个处理流程中断
            return {
                "summary": f"摘要生成失败: {str(e)}",
                "original_language": original_lang,
                "summary_language": "zh" if original_lang != "zh" else original_lang,
                "model": self.model_name,
                "timestamp": datetime.utcnow().isoformat(),
                "original_length": len(text),
                "summary_length": 0,
                "error": str(e)
            } 