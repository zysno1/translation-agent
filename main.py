#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
YouTube视频处理系统 - 主入口
支持视频下载、转写、翻译和分析功能
"""

import os
import sys
import argparse
from pathlib import Path
import datetime

# 添加src到Python路径
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.config.config_manager import load_config
from src.utils.log import setup_logger
from src.preprocessing.video_preprocessor import VideoPreprocessor
from src.transcription.audio_transcriber import AudioTranscriber
from src.translation.translation_service import TranslationService
from src.storage.storage_manager import StorageManager
from src.analysis.content_analyzer import ContentAnalyzer
from src.reports.report_generator import ReportGenerator


def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="YouTube视频处理系统")
    
    # 输入源参数组（互斥）
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--url", help="YouTube视频URL")
    input_group.add_argument("--file", type=Path, help="本地视频文件路径")
    input_group.add_argument("--batch", type=Path, help="批量处理队列文件")
    
    # 输出选项参数组
    output_group = parser.add_argument_group("输出选项")
    output_group.add_argument("--template", choices=["default", "academic", "business"], 
                            default="default", help="报告模板")
    output_group.add_argument("--summarize", action="store_true", 
                           help="生成内容摘要 (已废弃：现在摘要生成是默认行为)")
    
    # 其他选项
    parser.add_argument("--cleanup", action="store_true", 
                      help="清理所有中间文件")
    parser.add_argument("--config", type=Path, default="config.yaml",
                      help="配置文件路径")
    parser.add_argument("--verbose", action="store_true",
                      help="显示详细日志")
    
    return parser.parse_args()


def process_single_video(args, logger):
    """处理单个视频"""
    logger.info("开始处理视频")
    
    try:
        # 1. 初始化存储管理器
        storage = StorageManager()
        
        # 2. 预处理
        preprocessor = VideoPreprocessor()
        
        if args.url:
            logger.info(f"处理YouTube URL: {args.url}")
            # 从URL中下载视频、提取音频并获取视频信息
            audio_path, video_info = preprocessor.process(args.url)
            logger.info(f"视频信息获取完成: {len(video_info)} 个字段")
        elif args.file:
            logger.info(f"处理本地文件: {args.file}")
            # 视频预处理（可能会转换格式）
            audio_path = preprocessor.process(args.file)
            # 对于本地文件，创建基本视频信息
            file_name = os.path.basename(args.file)
            video_info = {
                "title": os.path.splitext(file_name)[0],
                "source": "Local File",
                "path": str(args.file),
                "language": "英语",  # 假设源语言为英语
                "target_language": "中文"
            }
        else:
            raise ValueError("必须提供URL或文件路径")
            
        # 3. 音频转写
        transcriber = AudioTranscriber()
        transcript = transcriber.transcribe(audio_path)
        
        # 确保transcript是字典类型
        if hasattr(transcript, 'to_dict'):
            transcript_dict = transcript.to_dict()
            # 将视频信息添加到转写结果中
            if video_info:
                transcript_dict['video_info'] = video_info
        else:
            transcript_dict = transcript
            # 将视频信息添加到转写结果中
            if isinstance(transcript_dict, dict) and video_info:
                transcript_dict['video_info'] = video_info
        
        transcript_path = storage.save_transcript(transcript_dict)
        logger.info(f"转写完成，保存至: {transcript_path}")
        
        # 4. 翻译
        translator = TranslationService()
        translation = translator.translate(transcript.text)
        
        # 将视频信息添加到翻译结果中
        if hasattr(translation, 'to_dict'):
            translation_dict = translation.to_dict()
            if video_info:
                translation_dict['video_info'] = video_info
            translation_path = storage.save_translation(translation_dict)
        else:
            # 已经是字典或其他类型
            translation_dict = translation
            if isinstance(translation_dict, dict) and video_info:
                translation_dict['video_info'] = video_info
            translation_path = storage.save_translation(translation_dict)
        
        logger.info(f"翻译完成，保存至: {translation_path}")
        
        # 5. 生成摘要 (现在作为默认流程的一部分)
        analyzer = ContentAnalyzer()
        # 使用译文文本生成摘要
        summary_text = None
        if hasattr(translation, 'text'):
            summary_text = translation.text
        elif isinstance(translation, dict) and 'text' in translation:
            summary_text = translation['text']
        else:
            summary_text = str(translation)
            
        summary_dict = analyzer.generate_summary(summary_text)
        
        # 确保summary_dict是一个字典
        if isinstance(summary_dict, str):
            # 如果返回的是字符串，转换为字典
            summary_dict = {
                'text': summary_dict,
                'type': 'summary'
            }
            
        # 将视频信息添加到摘要结果中
        if isinstance(summary_dict, dict) and video_info:
            summary_dict['video_info'] = video_info
            
        summary_path = storage.save_summary(summary_dict)
        logger.info(f"摘要生成完成，保存至: {summary_path}")
        
        # 收集处理统计信息
        processing_stats = {
            "start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "audio_duration": getattr(transcript, 'duration', 0),
            "audio_extraction_time": 0,  # 这里可以添加实际的音频提取耗时
            "transcription_time": 0,  # 这里可以添加实际的转写耗时
            "translation_time": 0,  # 这里可以添加实际的翻译耗时
            "transcript_length": len(getattr(transcript, 'text', '')),
            "translation_length": len(translation_dict.get('text', '')),
            "summary_length": len(summary_dict.get('text', '')) if isinstance(summary_dict, dict) else len(str(summary_dict)),
            "source_word_count": len(getattr(transcript, 'text', '').split()) if hasattr(transcript, 'text') else 0,
            "target_word_count": len(translation_dict.get('text', '').replace('\n', ' ').split()) if isinstance(translation_dict, dict) else 0,
            "num_chapters": 1,  # 默认至少有一个章节
            "files": {
                "audio": audio_path,
                "transcript": transcript_path,
                "translation": translation_path,
                "summary": summary_path
            },
            "exported_files": {
                "报告文件 (Markdown)": ""  # 这里会在生成报告后由报告生成器更新
            },
            "summary_data": summary_dict  # 添加摘要数据供报告生成器使用
        }
        
        # 6. 生成报告
        report_generator = ReportGenerator()
        try:
            # 确保所有数据都是字典类型
            report_path = report_generator.generate_report(
                transcript_dict,
                translation_dict,
                video_info,
                processing_stats
            )
            logger.info(f"报告已生成: {report_path}")
            return audio_path, transcript_path, translation_path, summary_path, report_path
        except Exception as e:
            logger.error(f"报告生成失败: {str(e)}")
            raise
        
    except Exception as e:
        logger.error(f"处理失败: {str(e)}")
        raise


def process_batch(batch_file, args, logger):
    """批量处理视频队列"""
    logger.info(f"开始批量处理: {batch_file}")
    
    # 加载URL队列
    with open(batch_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    results = []
    for i, url in enumerate(urls):
        logger.info(f"处理队列项 [{i+1}/{len(urls)}]: {url}")
        args.url = url
        try:
            output_path = process_single_video(args, logger)
            results.append((url, output_path, "成功"))
        except Exception as e:
            logger.error(f"处理 {url} 失败: {str(e)}")
            results.append((url, None, f"失败: {str(e)}"))
    
    # 生成批处理报告
    report_path = os.path.join("output", "batch_report.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# 批处理报告\n\n")
        for url, path, status in results:
            f.write(f"- {url}: {status}\n")
            if path:
                f.write(f"  - 输出: {path}\n")
    
    logger.info(f"批处理完成，报告已保存至: {report_path}")
    return report_path


def main():
    """主函数"""
    args = parse_arguments()
    
    # 设置日志
    log_level = "DEBUG" if args.verbose else "INFO"
    logger = setup_logger(log_level)
    
    logger.info("YouTube视频处理系统启动")
    
    try:
        # 加载配置
        config = load_config(args.config)
        logger.info(f"配置加载完成: {args.config}")
        
        # 处理视频
        if args.batch:
            process_batch(args.batch, args, logger)
        else:
            process_single_video(args, logger)
            
    except Exception as e:
        logger.error(f"程序执行出错: {str(e)}")
        return 1
        
    logger.info("程序执行完成")
    return 0


if __name__ == "__main__":
    sys.exit(main()) 