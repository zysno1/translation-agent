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
import time  # 添加time模块

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
    input_group = parser.add_mutually_exclusive_group(required=False)
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
        
        # 记录音频提取开始时间
        audio_extraction_start = time.time()
        
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
        
        # 计算音频提取耗时
        audio_extraction_time = time.time() - audio_extraction_start
        logger.info(f"音频提取耗时: {audio_extraction_time:.2f}秒")
            
        # 3. 音频转写
        # 记录转写开始时间
        transcription_start = time.time()
        
        transcriber = AudioTranscriber()
        transcript = transcriber.transcribe(audio_path)
        
        # 计算转写耗时
        transcription_time = time.time() - transcription_start
        logger.info(f"转写耗时: {transcription_time:.2f}秒")
        
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
        # 记录翻译开始时间
        translation_start = time.time()
        
        translator = TranslationService()
        
        # 检查transcript_dict中是否包含segments
        if isinstance(transcript_dict, dict) and 'segments' in transcript_dict and transcript_dict['segments']:
            # 获取视频时长，决定是否使用并行翻译
            video_duration = 0
            if video_info and 'duration' in video_info:
                video_duration = video_info.get('duration', 0)
            elif hasattr(transcript, 'duration'):
                video_duration = transcript.duration
            
            # 使用translate_segments处理带时间戳的段落，传入视频时长参数
            logger.info(f"使用分段翻译处理 {len(transcript_dict['segments'])} 个段落，视频时长: {video_duration} 秒")
            translated_segments = translator.translate_segments(
                transcript_dict['segments'],
                video_duration=video_duration
            )
            
            # 创建翻译结果字典，保持与原始transcript_dict结构一致
            # 合并所有翻译后的文本作为完整翻译
            full_translated_text = " ".join([seg.get('text', '') for seg in translated_segments])
            
            translation_dict = {
                'text': full_translated_text,  # 合并后的完整翻译文本
                'segments': translated_segments,  # 翻译后的分段
                'source_lang': 'auto',
                'target_lang': '中文',
                'source_text': transcript.text
            }
            
            # 添加视频信息
            if video_info:
                translation_dict['video_info'] = video_info
        else:
            # 回退到整体翻译
            logger.warning("转录结果中没有分段信息，使用整体翻译")
            translation = translator.translate(transcript.text)
            
            # 将视频信息添加到翻译结果中
            if hasattr(translation, 'to_dict'):
                translation_dict = translation.to_dict()
                if video_info:
                    translation_dict['video_info'] = video_info
            else:
                # 已经是字典或其他类型
                translation_dict = translation
                if isinstance(translation_dict, dict) and video_info:
                    translation_dict['video_info'] = video_info
        
        # 计算翻译耗时
        translation_time = time.time() - translation_start
        logger.info(f"翻译耗时: {translation_time:.2f}秒")
        
        translation_path = storage.save_translation(translation_dict)
        logger.info(f"翻译完成，保存至: {translation_path}")
        
        # 5. 生成摘要 (现在作为默认流程的一部分)
        analyzer = ContentAnalyzer()
        # 使用译文文本生成摘要
        summary_text = None
        
        # 获取翻译后的文本
        if isinstance(translation_dict, dict):
            if 'text' in translation_dict:
                # 首先尝试使用完整文本
                summary_text = translation_dict['text']
            elif 'segments' in translation_dict and translation_dict['segments']:
                # 如果没有完整文本但有分段，则拼接所有分段的文本
                segment_texts = [seg.get('text', '') for seg in translation_dict['segments'] if seg.get('text')]
                summary_text = ' '.join(segment_texts)
        else:
            # 回退处理
            if hasattr(translation_dict, 'text'):
                summary_text = translation_dict.text
            else:
                summary_text = str(translation_dict)
            
        summary_dict = analyzer.generate_summary(summary_text)
        
        # 确保summary_dict是一个字典
        if isinstance(summary_dict, str):
            # 如果返回的是字符串，转换为字典
            summary_dict = {
                'text': summary_dict,
                'summary': summary_dict,  # 同时添加summary字段以确保兼容性
                'type': 'summary'
            }
        elif isinstance(summary_dict, dict):
            # 确保同时有text和summary字段，保持两者同步
            if 'text' in summary_dict and 'summary' not in summary_dict:
                summary_dict['summary'] = summary_dict['text']
            elif 'summary' in summary_dict and 'text' not in summary_dict:
                summary_dict['text'] = summary_dict['summary']
        
        # 提取关键点并添加到summary_dict中
        if isinstance(summary_dict, dict):
            try:
                key_points = analyzer.extract_key_points(summary_text)
                summary_dict['key_points'] = key_points
                logger.info(f"成功提取{len(key_points)}个关键点")
            except Exception as e:
                logger.warning(f"提取关键点失败: {e}")
                # 失败时添加默认关键点，避免报告生成错误
                summary_dict['key_points'] = ["未能成功提取关键点，请查看完整摘要内容。"]
            
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
            "audio_extraction_time": audio_extraction_time,  # 添加实际的音频提取耗时
            "transcription_time": transcription_time,  # 添加实际的转写耗时
            "translation_time": translation_time,  # 添加实际的翻译耗时
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


def cleanup_files(logger):
    """清理所有中间文件"""
    logger.info("开始清理中间文件...")
    
    try:
        # 初始化存储管理器
        storage = StorageManager()
        
        # 执行清理操作
        storage.cleanup(keep_important=False)
        
        logger.info("中间文件清理完成")
        return True
        
    except Exception as e:
        logger.error(f"清理文件失败: {str(e)}")
        return False


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
        
        # 如果只是清理文件，执行清理后退出
        if args.cleanup and not (args.url or args.file or args.batch):
            success = cleanup_files(logger)
            return 0 if success else 1
        
        # 处理视频
        if args.batch:
            process_batch(args.batch, args, logger)
        elif args.url or args.file:
            process_single_video(args, logger)
        else:
            logger.error("必须提供 --url、--file 或 --batch 参数之一")
            return 1
            
    except Exception as e:
        logger.error(f"程序执行出错: {str(e)}")
        return 1
        
    logger.info("程序执行完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())