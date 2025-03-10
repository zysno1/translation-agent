# -*- coding: utf-8 -*-

"""
翻译服务模块
负责文本翻译功能
"""

import os
from typing import Dict, Any, Optional, List, Union, Tuple
from concurrent.futures import ThreadPoolExecutor
import time
from functools import partial
import concurrent.futures

from src.config.config_manager import get_config
from src.utils.log import get_logger
from src.models.models import Models
# 导入段落优化器
from src.translation.segment_optimizer import SegmentOptimizer

# 获取日志器
logger = get_logger()


class TranslationResult:
    """翻译结果"""
    
    def __init__(self, text: str, source_lang: Optional[str] = None, 
                target_lang: str = "中文", source_text: Optional[str] = None):
        """
        初始化翻译结果
        
        Args:
            text: 翻译后的文本
            source_lang: 源语言
            target_lang: 目标语言
            source_text: 原始文本
        """
        self.text = text
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.source_text = source_text
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'text': self.text,
            'source_lang': self.source_lang,
            'target_lang': self.target_lang,
            'source_text': self.source_text
        }


class TranslationService:
    """翻译服务"""
    
    def __init__(self, model_name: Optional[str] = None):
        """
        初始化翻译服务
        
        Args:
            model_name: 翻译模型名称，默认从配置获取
        """
        config = get_config()
        self.config = config
        
        # 翻译模型
        self.model_name = model_name or config.get('defaults', {}).get('translation')
        
        # 初始化段落优化器
        max_segment_length = config.get('translation', {}).get('max_segment_length', 1800)
        min_segment_length = config.get('translation', {}).get('min_segment_length', 100)
        self.segment_optimizer = SegmentOptimizer(
            max_segment_length=max_segment_length,
            min_segment_length=min_segment_length
        )
        
        logger.info(f"翻译服务初始化，使用模型: {self.model_name}, 段落长度范围: {min_segment_length}-{max_segment_length}")
        
        # 其他配置项
        self.batch_size = config.get('batch', {}).get('max_batch_size', 5)  # 批处理大小
        self.max_retries = config.get('batch', {}).get('max_retries', 3)    # 最大重试次数
        self.retry_delay = config.get('batch', {}).get('retry_delay', 2)    # 重试延迟(秒)
        self.max_workers = config.get('batch', {}).get('max_workers', 3)    # 最大并发数
        
        # 并行翻译配置
        parallel_config = config.get('translation', {}).get('parallel', {})
        self.parallel_enabled = parallel_config.get('enabled', True)        # 是否启用并行翻译
        self.parallel_min_video_length = parallel_config.get('min_video_length', 3600)  # 启用并行翻译的最小视频长度（秒）
        self.parallel_max_workers = parallel_config.get('max_workers', 16)  # 最大并行工作线程数
        self.parallel_batch_size = parallel_config.get('batch_size', 20)    # 每批处理的段落数量
        self.parallel_progress_report = parallel_config.get('progress_report', True)  # 是否报告翻译进度
    
    def translate(self, text: str, target_lang: str = "中文") -> TranslationResult:
        """
        翻译文本
        
        Args:
            text: 待翻译文本
            target_lang: 目标语言
            
        Returns:
            翻译结果
        """
        # 记录开始翻译
        logger.info(f"开始翻译文本 ({len(text)} 字符) 到 {target_lang}")
        
        # 如果文本为空，直接返回空结果
        if not text or text.strip() == "":
            logger.warning("翻译文本为空")
            return TranslationResult(
                text="",
                target_lang=target_lang,
                source_text=text
            )
        
        # 检测语言，如果已经是目标语言，则直接返回
        if self._is_target_language(text, target_lang):
            logger.info(f"检测到输入已经是{target_lang}，保持原文")
            return TranslationResult(
                text=text,
                source_lang=target_lang,
                target_lang=target_lang,
                source_text=text
            )
        
        try:
            # 使用模型进行翻译
            result = self._translate_with_model(text, target_lang)
            
            # 创建翻译结果
            translation_result = TranslationResult(
                text=result.get('text', ""),
                source_lang="自动检测",
                target_lang=target_lang,
                source_text=text
            )
            
            logger.info(f"翻译完成 ({len(translation_result.text)} 字符)")
            return translation_result
            
        except Exception as e:
            logger.error(f"翻译失败: {e}")
            # 返回一个错误提示，避免程序崩溃
            return TranslationResult(
                text=f"[翻译错误: {str(e)}]",
                target_lang=target_lang,
                source_text=text
            )
    
    def batch_translate(self, texts: List[str], target_lang: str = "中文") -> List[TranslationResult]:
        """
        批量翻译文本
        
        Args:
            texts: 待翻译文本列表
            target_lang: 目标语言
            
        Returns:
            翻译结果列表
        """
        logger.info(f"开始批量翻译 {len(texts)} 条文本到 {target_lang}")
        
        # 处理空列表情况
        if not texts:
            logger.warning("翻译文本列表为空")
            return []
            
        # 过滤掉空文本
        texts = [t for t in texts if t and t.strip()]
        if not texts:
            logger.warning("过滤后翻译文本列表为空")
            return []
        
        # 批量处理
        results = []
        
        # 使用线程池并发处理
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交翻译任务
            future_to_text = {
                executor.submit(self.translate, text, target_lang): text 
                for text in texts
            }
            
            # 收集结果（按原始顺序）
            for future in future_to_text:
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    logger.error(f"批量翻译任务失败: {e}")
                    # 添加一个错误结果
                    results.append(TranslationResult(
                        text=f"[批量翻译错误: {str(e)}]",
                        target_lang=target_lang,
                        source_text=future_to_text[future]
                    ))
        
        logger.info(f"批量翻译完成，成功翻译 {len(results)} 条文本")
        return results
    
    def translate_segments(self, segments: List[Dict[str, Any]], target_lang: str = "中文", 
                         video_duration: Optional[float] = None) -> List[Dict[str, Any]]:
        """
        翻译带有时间戳的片段（通常用于字幕翻译）
        
        Args:
            segments: 包含文本和时间戳的片段列表
            target_lang: 目标语言
            video_duration: 视频时长（秒），用于决定是否使用并行翻译
            
        Returns:
            翻译后的片段列表
        """
        logger.info(f"开始翻译 {len(segments)} 个片段到 {target_lang}")
        
        # 判断是否使用并行翻译
        if self.parallel_enabled and video_duration and video_duration >= self.parallel_min_video_length:
            logger.info(f"检测到长视频 ({video_duration:.1f} 秒)，启用并行翻译")
            return self.translate_segments_parallel(segments, target_lang)
        
        # 使用段落优化器合并片段
        optimized_segments = self.segment_optimizer.optimize_segments(segments)
        logger.info(f"段落优化完成: 从 {len(segments)} 个时间戳段落合并为 {len(optimized_segments)} 个语义段落")
        
        # 提取文本
        texts = [segment.get('text', '') for segment in optimized_segments]
        
        # 批量翻译
        translation_results = self.batch_translate(texts, target_lang)
        
        # 合并优化后的段落结果
        optimized_translations = []
        for i, segment in enumerate(optimized_segments):
            # 复制原始片段
            translated_segment = segment.copy()
            
            # 更新翻译文本
            if i < len(translation_results):
                translated_segment['text'] = translation_results[i].text
                translated_segment['original_text'] = segment.get('text', '')
            
            optimized_translations.append(translated_segment)
        
        # 还原到原始时间戳段落
        final_translations = self._map_optimized_to_original(optimized_translations, segments, target_lang)
        
        logger.info(f"片段翻译完成")
        return final_translations
    
    def translate_segments_parallel(self, segments: List[Dict[str, Any]], 
                                  target_lang: str = "中文") -> List[Dict[str, Any]]:
        """
        并行翻译带有时间戳的片段（用于长视频处理）
        
        Args:
            segments: 包含文本和时间戳的片段列表
            target_lang: 目标语言
            
        Returns:
            翻译后的片段列表
        """
        logger.info(f"开始并行翻译 {len(segments)} 个片段到 {target_lang}")
        
        # 使用段落优化器合并片段（此步骤仍保留以减少总段落数）
        optimized_segments = self.segment_optimizer.optimize_segments(segments)
        logger.info(f"段落优化完成: 从 {len(segments)} 个时间戳段落合并为 {len(optimized_segments)} 个语义段落")
        
        # 将优化后的段落映射回原始段落（使用并行处理）
        final_translations = self._map_optimized_to_original_parallel(
            optimized_segments, segments, target_lang, self.parallel_max_workers
        )
        
        logger.info(f"并行片段翻译完成")
        return final_translations
    
    def _map_optimized_to_original(self, optimized_translations: List[Dict[str, Any]], 
                                  original_segments: List[Dict[str, Any]], 
                                  target_lang: str = "中文") -> List[Dict[str, Any]]:
        """
        将优化后的翻译映射回原始时间戳段落
        
        Args:
            optimized_translations: 优化后的翻译结果
            original_segments: 原始时间戳段落
            target_lang: 目标语言
            
        Returns:
            映射回原始时间戳的翻译结果
        """
        # 创建时间范围到翻译的映射
        time_range_to_translation = {}
        for segment in optimized_translations:
            start = segment.get('start', 0)
            end = segment.get('end', 0)
            text = segment.get('text', '')
            original_text = segment.get('original_text', '')
            time_range_to_translation[(start, end)] = {
                'text': text,
                'original_text': original_text
            }
        
        # 为每个原始段落分配翻译
        final_translations = []
        for segment in original_segments:
            start = segment.get('start', 0)
            end = segment.get('end', 0)
            original_text = segment.get('text', '')
            
            # 复制原始段落
            translated_segment = segment.copy()
            translated_segment['original_text'] = original_text
            
            # 查找最匹配的翻译
            best_match = None
            best_overlap = 0
            
            for (opt_start, opt_end), translation in time_range_to_translation.items():
                # 计算时间重叠
                overlap_start = max(start, opt_start)
                overlap_end = min(end, opt_end)
                overlap = max(0, overlap_end - overlap_start)
                
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_match = translation
            
            # 如果找到匹配，使用其翻译
            if best_match and best_overlap > 0:
                # 单独翻译每个segment，确保每个segment有独立的翻译
                translation = self.translate(original_text, target_lang)
                translated_segment['text'] = translation.text
            else:
                # 未找到匹配，单独翻译
                logger.warning(f"未找到与时间段 [{start}-{end}] 匹配的优化段落，单独翻译")
                translation = self.translate(original_text, target_lang)
                translated_segment['text'] = translation.text
            
            final_translations.append(translated_segment)
        
        return final_translations
    
    def _map_optimized_to_original_parallel(self, optimized_translations: List[Dict[str, Any]], 
                                          original_segments: List[Dict[str, Any]], 
                                          target_lang: str = "中文",
                                          max_workers: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        并行将优化后的翻译映射回原始时间戳段落
        
        Args:
            optimized_translations: 优化后的翻译结果
            original_segments: 原始时间戳段落
            target_lang: 目标语言
            max_workers: 最大工作线程数
            
        Returns:
            映射回原始时间戳的翻译结果
        """
        # 创建时间范围到翻译的映射
        time_range_to_translation = {}
        for segment in optimized_translations:
            start = segment.get('start', 0)
            end = segment.get('end', 0)
            text = segment.get('text', '')
            original_text = segment.get('original_text', '')
            time_range_to_translation[(start, end)] = {
                'text': text,
                'original_text': original_text
            }
        
        # 将原始段落分成多个批次进行处理
        # 如果未指定max_workers，则使用配置中的值或默认值
        if max_workers is None:
            max_workers = self.parallel_max_workers
        
        # 批次大小，根据配置或默认值确定
        batch_size = self.parallel_batch_size
        batches = [original_segments[i:i+batch_size] for i in range(0, len(original_segments), batch_size)]
        
        logger.info(f"分割为 {len(batches)} 批进行并行处理，每批约 {batch_size} 个段落，使用 {max_workers} 个工作线程")
        
        # 部分函数应用，创建用于并行处理的函数
        process_batch_func = partial(
            self._process_segment_batch, 
            time_range_to_translation=time_range_to_translation, 
            target_lang=target_lang
        )
        
        # 添加进度报告
        total_batches = len(batches)
        completed_batches = 0
        start_time = time.time()
        
        # 使用线程池进行并行处理
        final_translations = []
        batch_results = {}  # 存储批次结果的字典，键为批次索引
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有批次任务
            future_to_batch = {executor.submit(process_batch_func, batch): i for i, batch in enumerate(batches)}
            
            # 收集结果
            for future in concurrent.futures.as_completed(future_to_batch):
                batch_index = future_to_batch[future]
                completed_batches += 1
                
                # 进度报告
                if self.parallel_progress_report:
                    progress = (completed_batches / total_batches) * 100
                    elapsed_time = time.time() - start_time
                    remaining_batches = total_batches - completed_batches
                    eta = (elapsed_time / completed_batches) * remaining_batches if completed_batches > 0 else 0
                    
                    # 每完成10%或第一个批次或最后一个批次时报告进度
                    if (completed_batches % max(1, total_batches // 10) == 0 or 
                        completed_batches == 1 or completed_batches == total_batches):
                        logger.info(f"翻译进度: {progress:.1f}% ({completed_batches}/{total_batches} 批次), "
                                   f"已用时间: {elapsed_time:.1f}秒, 预计剩余时间: {eta:.1f}秒")
                
                try:
                    results = future.result()
                    # 存储结果，保持原始顺序
                    batch_results[batch_index] = results
                except Exception as e:
                    logger.error(f"批次 {batch_index} 处理失败: {e}")
                    # 对失败的批次进行回退处理
                    batch_results[batch_index] = self._process_segment_batch_fallback(
                        batches[batch_index], target_lang
                    )
        
        # 按批次索引顺序合并结果
        for i in range(len(batches)):
            if i in batch_results:
                final_translations.extend(batch_results[i])
        
        # 确保最终结果的顺序与原始段落顺序一致
        if final_translations:
            final_translations.sort(key=lambda x: (x.get('start', 0), x.get('index', 0)))
        
        return final_translations
    
    def _process_segment_batch(self, batch: List[Dict[str, Any]], 
                             time_range_to_translation: Dict[Tuple[float, float], Dict[str, Any]],
                             target_lang: str) -> List[Dict[str, Any]]:
        """
        处理一个段落批次
        
        Args:
            batch: 段落批次
            time_range_to_translation: 时间范围到翻译的映射
            target_lang: 目标语言
            
        Returns:
            处理后的段落批次
        """
        # 收集批次中所有需要翻译的文本
        texts_to_translate = []
        indices_to_translate = []  # 记录需要翻译的段落在批次中的索引
        result_segments = []
        
        # 为每个段落添加批次内索引
        for i, segment in enumerate(batch):
            # 复制原始段落，添加索引用于后续排序
            translated_segment = segment.copy()
            translated_segment['index'] = i  # 添加批次内索引
            translated_segment['original_text'] = segment.get('text', '')
            result_segments.append(translated_segment)
            
            # 收集所有文本进行批量翻译
            texts_to_translate.append(segment.get('text', ''))
            indices_to_translate.append(i)
        
        # 批量翻译所有文本
        if texts_to_translate:
            try:
                # 使用批量翻译，提高效率
                translation_results = self.batch_translate(texts_to_translate, target_lang)
                
                # 将翻译结果应用到对应段落
                for i, index in enumerate(indices_to_translate):
                    if i < len(translation_results):
                        result_segments[index]['text'] = translation_results[i].text
            except Exception as e:
                logger.error(f"批次翻译失败，回退到单独翻译: {e}")
                # 如果批量翻译失败，回退到单独翻译
                for index in indices_to_translate:
                    try:
                        original_text = result_segments[index].get('original_text', '')
                        translation = self.translate(original_text, target_lang)
                        result_segments[index]['text'] = translation.text
                    except Exception as e2:
                        logger.error(f"单独翻译段落失败: {e2}")
                        # 如果翻译失败，使用错误提示
                        result_segments[index]['text'] = f"[翻译错误: {str(e2)}]"
        
        return result_segments
    
    def _process_segment_batch_fallback(self, batch: List[Dict[str, Any]], target_lang: str) -> List[Dict[str, Any]]:
        """
        批次处理失败时的回退方法，逐个翻译段落
        
        Args:
            batch: 段落批次
            target_lang: 目标语言
            
        Returns:
            处理后的段落批次
        """
        result_segments = []
        
        for i, segment in enumerate(batch):
            # 复制原始段落
            translated_segment = segment.copy()
            translated_segment['index'] = i  # 添加批次内索引
            translated_segment['original_text'] = segment.get('text', '')
            
            try:
                # 单独翻译
                translation = self.translate(segment.get('text', ''), target_lang)
                translated_segment['text'] = translation.text
            except Exception as e:
                logger.error(f"回退翻译失败: {e}")
                translated_segment['text'] = f"[翻译错误: {str(e)}]"
            
            result_segments.append(translated_segment)
        
        return result_segments
    
    def _translate_with_model(self, text: str, target_lang: str) -> Dict[str, str]:
        """
        使用配置的模型进行翻译
        
        Args:
            text: 待翻译文本
            target_lang: 目标语言
            
        Returns:
            包含翻译结果的字典
        """
        # 根据不同模型进行翻译
        retries = 0
        last_error = None
        
        while retries < self.max_retries:
            try:
                logger.info(f"调用模型 {self.model_name} 进行翻译 (尝试 {retries+1}/{self.max_retries})")
                result = Models.translate(text, target_lang=target_lang, model_name=self.model_name)
                return result
            except Exception as e:
                last_error = e
                logger.warning(f"翻译失败，将重试: {e}")
                retries += 1
                if retries < self.max_retries:
                    time.sleep(self.retry_delay)
        
        # 所有重试都失败了
        logger.error(f"翻译重试耗尽: {last_error}")
        return {"text": f"[翻译失败: {str(last_error)}]"}
    
    def _is_target_language(self, text: str, target_lang: str) -> bool:
        """
        检测文本是否已经是目标语言
        
        Args:
            text: 待检测文本
            target_lang: 目标语言
            
        Returns:
            是否为目标语言
        """
        # 样本太小时，不做检测
        if len(text) < 10:
            return False
            
        # 检测中文（修复逻辑，只有当文本主要是中文时才返回True）
        if target_lang in ["中文", "zh", "chinese"]:
            # 计算中文字符的比例
            chinese_chars = sum(1 for char in text if '\u4e00' <= char <= '\u9fff')
            text_length = max(len(text.strip()), 1)  # 避免除零错误
            chinese_ratio = chinese_chars / text_length
            
            # 调试日志
            logger.debug(f"中文检测: 文本长度={text_length}, 中文字符数={chinese_chars}, 比例={chinese_ratio:.2f}")
            
            # 如果中文字符占比超过60%，认为是中文文本
            return chinese_ratio > 0.6
        
        # 检测英文
        if target_lang in ["英文", "en", "english"]:
            # 检测是否主要是英文字符（至少80%）
            english_chars = sum(1 for char in text if 'a' <= char.lower() <= 'z' or char in " ,.!?'\"")
            text_length = max(len(text.strip()), 1)
            english_ratio = english_chars / text_length
            
            # 调试日志
            logger.debug(f"英文检测: 文本长度={text_length}, 英文字符数={english_chars}, 比例={english_ratio:.2f}")
            
            return english_ratio > 0.8
        
        # 其他语言默认返回False（需要翻译）
        return False 