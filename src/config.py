import os

# 目录配置
DIR_CONFIG = {
    'root': '.',  # 根目录
    'logs': 'logs',  # 日志目录
    'temp': 'temp',  # 临时文件目录
    'output': 'output',  # 输出目录
    'transcripts': 'transcripts'  # 转写文本目录
}

# 模型配置
MODEL_CONFIG = {
    # 语音识别模型配置
    'speech_recognition': {
        'model': 'paraformer-v2',  # 默认使用 paraformer-v2
        'timeout': 600,  # 请求超时时间（秒）
        'api_params': {
            'channel_id': [0],  # 指定音轨ID，默认处理首轨
            'language_hints': ['en'],  # 语言提示，默认英语
            'enable_timestamp': True,  # 启用时间戳
            'enable_punctuation': True,  # 启用标点符号
            'hot_words': None  # 热词功能，用于提高特定词汇的识别准确率
        },
        # 可用的语音识别模型
        'available_models': {
            'paraformer-v2': {
                'description': 'Paraformer最新语音识别模型，支持多个语种的语音识别',
                'price_per_second': 0.00008,  # 元/秒
                'sample_rate': '16kHz',
                'max_file_size': 512,  # 单位：MB
                'max_batch_size': 100,  # 最大批处理文件数
                'api_params': {
                    'channel_id': [0],  # 指定音轨ID，默认处理首轨
                    'language_hints': ['zh'],  # 语言提示，默认中文
                    'enable_timestamp': True,  # 启用时间戳
                    'enable_punctuation': True,  # 启用标点符号
                    'hot_words': None  # 热词功能，用于提高特定词汇的识别准确率
                },
                'supported_languages': {
                    'zh': '中文（包含普通话和方言）',
                    'en': '英文',
                    'ja': '日语',
                    'ko': '韩语'
                },
                'supported_dialects': [
                    '上海话', '吴语', '闽南语', '东北话', '甘肃话', 
                    '贵州话', '河南话', '湖北话', '湖南话', '江西话', 
                    '宁夏话', '山西话', '陕西话', '山东话', '四川话', 
                    '天津话', '云南话', '粤语'
                ],
                'supported_formats': [
                    'aac', 'amr', 'avi', 'flac', 'flv', 'm4a', 'mkv',
                    'mov', 'mp3', 'mp4', 'mpeg', 'ogg', 'opus', 'wav',
                    'webm', 'wma', 'wmv'
                ],
                'features': [
                    '通用场景',
                    '高准确率',
                    '支持多语种识别',
                    '支持中文方言',
                    '支持热词定制',
                    '支持标点符号预测',
                    '支持时间戳'
                ]
            },
            'paraformer-realtime-8k-v2': {
                'description': 'Paraformer-realtime-8k-v2 实时语音识别模型',
                'price_per_second': 0.00024,  # 元/秒
                'sample_rate': '8kHz',
                'max_file_size': 512,  # 单位：MB
                'max_batch_size': 100,  # 最大批处理文件数
                'api_params': {
                    'channel_id': [0],  # 指定音轨ID，默认处理首轨
                    'language_hints': ['zh'],  # 语言提示，默认中文
                    'enable_timestamp': True,  # 启用时间戳
                    'enable_punctuation': True  # 启用标点符号
                },
                'supported_formats': [
                    'aac', 'amr', 'avi', 'flac', 'flv', 'm4a', 'mkv',
                    'mov', 'mp3', 'mp4', 'mpeg', 'ogg', 'opus', 'wav',
                    'webm', 'wma', 'wmv'
                ],
                'features': [
                    '实时语音识别',
                    '电话语音',
                    '支持标点符号预测',
                    '支持时间戳'
                ]
            },
            'sensevoice-v1': {
                'description': '语音识别大模型，提供超过50种语言的高精度语音识别',
                'price_per_second': 0.0007,  # 元/秒
                'free_quota': 36000,  # 每月免费额度（秒）
                'sample_rate': '16kHz',
                'max_file_size': 2048,  # 单位：MB，最大支持2GB
                'max_batch_size': 100,  # 最大批处理文件数
                'api_params': {
                    'channel_id': [0],  # 指定音轨ID，默认处理首轨
                    'language_hints': ['en'],  # 语言提示，默认英语
                    'enable_timestamp': True,  # 启用时间戳
                    'enable_punctuation': True,  # 启用标点符号
                    'enable_emotion': False,  # 启用情感检测
                    'enable_audio_event': False  # 启用音频事件检测
                },
                'supported_languages': {
                    'zh': '中文',
                    'en': '英语',
                    'ja': '日语',
                    'ko': '韩语',
                    'th': '泰语',
                    'fr': '法语',
                    'de': '德语',
                    'es': '西班牙语',
                    'ar': '阿拉伯语',
                    'id': '印尼语',
                    'vi': '越南语',
                    'pt': '葡萄牙语',
                    'it': '意大利语',
                    'nl': '荷兰语',
                    'ru': '俄语',
                    'km': '柬埔寨语',
                    'lo': '老挝语',
                    'my': '缅甸语',
                    'ceb': '宿务语',
                    'fil': '菲律宾语',
                    'cs': '捷克语',
                    'pl': '波兰语',
                    'fa': '波斯语',
                    'he': '希伯来语',
                    'tr': '土耳其语',
                    'hi': '印地语',
                    'bn': '孟加拉语',
                    'ur': '乌尔都语'
                },
                'billing_note': '仅对音轨中被判定为语音内容的时长进行计费，非语音内容不计费',
                'supported_formats': [
                    'aac', 'amr', 'avi', 'flac', 'flv', 'm4a', 'mkv', 
                    'mov', 'mp3', 'mp4', 'mpeg', 'ogg', 'opus', 'wav', 
                    'webm', 'wma', 'wmv'
                ],
                'features': [
                    '多语言支持（50+种语言）',
                    '高精度语音识别',
                    '情感检测',
                    '音频事件检测',
                    '支持多种音视频格式',
                    '支持标点符号预测',
                    '支持时间戳',
                    '支持多轨道音频'
                ]
            }
        }
    },
    
    # 文本翻译模型配置
    'translation': {
        'model': 'qwen-mt-plus',  # 默认使用 plus 版本
        'timeout': 300,  # 请求超时时间（秒）
        'batch_size': 12,  # 批量翻译时每批的段落数
        'max_chars_per_segment': 2000,  # 单次翻译的最大字符数
        'retry_delay': 2,  # 批次间延迟（秒）
        'api_params': {
            'translation_options': {
                'source_lang': 'English',  # 默认源语言
                'target_lang': 'Chinese',  # 默认目标语言
                'domains': 'The sentence is from AI and technology domain. It mainly involves artificial intelligence, machine learning systems, and cloud computing related content. Pay attention to professional terminologies when translating.'
            }
        },
        # 可用的翻译模型
        'available_models': {
            'qwen-mt-plus': {
                'description': '通义千问 MT-Plus 模型',
                'max_input_tokens': 1024,
                'max_output_tokens': 1024,
                'max_context_length': 2048,
                'input_price_per_1k_tokens': 0.03,  # 元/1K tokens，输入价格
                'output_price_per_1k_tokens': 0.06,  # 元/1K tokens，输出价格
                'features': ['高质量翻译', '多语言互译', '术语干预', '领域提示']
            },
            'qwen-mt-turbo': {
                'description': '通义千问 MT-Turbo 模型',
                'max_input_tokens': 1024,
                'max_output_tokens': 1024,
                'max_context_length': 2048,
                'input_price_per_1k_tokens': 0.015,  # 元/1K tokens，输入价格
                'output_price_per_1k_tokens': 0.03,  # 元/1K tokens，输出价格
                'features': ['快速翻译', '多语言互译', '成本更低']
            }
        }
    },
    
    # 文本优化模型配置
    'text_optimization': {
        'model': 'qwen-plus',  # 默认使用 plus 版本
        'timeout': 300,  # 请求超时时间（秒）
        'batch_size': 12,  # 批量处理时每批的段落数
        'max_chars_per_segment': 2000,  # 单次处理的最大字符数
        'retry_delay': 2,  # 批次间延迟（秒）
        'api_params': {
            'result_format': 'message',
            'temperature': 0.7,
            'top_p': 0.8,
            'enable_search': False
        },
        # 可用的文本优化模型
        'available_models': {
            'qwen-plus': {
                'description': '通义千问-Plus 模型',
                'max_tokens': 131072,  # 更新为文档中的最大上下文长度
                'input_price_per_1k_tokens': 0.0008,  # 元/1K tokens，输入价格
                'output_price_per_1k_tokens': 0.002,  # 元/1K tokens，输出价格
                'features': ['文本优化', '内容改写', '风格调整']
            },
            'qwen-turbo': {
                'description': '通义千问-Turbo 模型',
                'max_tokens': 1000000,  # 更新为文档中的最大上下文长度
                'input_price_per_1k_tokens': 0.0003,  # 元/1K tokens，输入价格
                'output_price_per_1k_tokens': 0.0006,  # 元/1K tokens，输出价格
                'features': ['文本优化', '内容改写', '风格调整']
            }
        }
    },
    
    # 内容总结模型配置
    'content_summary': {
        'model': 'qwen-plus',
        'timeout': 300,
        'batch_size': 1,
        'max_chars_per_segment': 8000,
        'retry_delay': 2,
        'api_params': {
            'result_format': 'json',
            'temperature': 0,
            'top_p': 1,
            'enable_search': False,
            'prompt_template': 'Please analyze the following transcript and provide a structured summary based on the content type (technical sharing, academic training, or industry keynote). Include key points and insights while maintaining the original structure and technical accuracy.'
        },
        'available_models': {
            'qwen-plus': {
                'description': '通义千问-Plus 模型',
                'max_tokens': 131072,
                'input_price_per_1k_tokens': 0.0008,
                'output_price_per_1k_tokens': 0.002,
                'features': ['内容分类', '结构化总结', 'JSON输出']
            }
        }
    },
    
    # 支持的语言列表
    'supported_languages': {
        'Chinese': '中文',
        'English': '英语',
        'Japanese': '日语',
        'Korean': '韩语',
        'Thai': '泰语',
        'French': '法语',
        'German': '德语',
        'Spanish': '西班牙语',
        'Arabic': '阿拉伯语',
        'Indonesian': '印尼语',
        'Vietnamese': '越南语',
        'Portuguese': '巴西葡萄牙语',
        'Italian': '意大利语',
        'Dutch': '荷兰语',
        'Russian': '俄语',
        'Khmer': '高棉语',
        'Lao': '老挝语',
        'Burmese': '缅甸语',
        'Cebuano': '宿务语',
        'Filipino': '菲律宾语',
        'Czech': '捷克语',
        'Polish': '波兰语',
        'Persian': '波斯语',
        'Hebrew': '希伯来语',
        'Turkish': '土耳其语',
        'Hindi': '印地语',
        'Bengali': '孟加拉语',
        'Urdu': '乌尔都语'
    }
}

# 系统提示词配置
PROMPT_CONFIG = {
    'translation': {
        'system_prompt': """你是一位专业的英译中翻译专家，专门从事人工智能、机器学习系统(MLSys)、大语言模型(LLM)和云原生领域的技术文档翻译。你需要：

1. 保持专业性：
- 准确理解并翻译专业术语
- 保持技术文档的严谨性
- 确保翻译后的内容对目标领域的技术人员友好

2. 翻译风格：
- 采用中性、专业的语气
- 保持句式流畅自然
- 避免过度口语化
- 适当保留关键的英文术语

3. 术语处理：
- 优先使用领域内约定俗成的中文译名
- 首次出现的专业术语可采用"中文(英文)"的形式
- 对于新兴概念，可保留原有英文表述
- 参考已提供的专业术语对照表

4. 特殊要求：
- 保留代码片段、变量名和函数名中的英文
- 保持文本的格式和结构
- 确保数字、单位和标点符号的正确性
- 注意上下文的连贯性

请基于以上要求，提供准确、专业、流畅的中文翻译。""",
        
        'user_prompt': """请将以下英文文本翻译成中文：

{text}

要求：
1. 保持专业性和准确性
2. 遵循术语表中的标准翻译
3. 适当保留关键英文术语
4. 确保翻译流畅自然"""
    }
}

# OSS配置
OSS_CONFIG = {
    'access_key': os.getenv('OSS_ACCESS_KEY', ''),  # OSS访问密钥
    'access_secret': os.getenv('OSS_ACCESS_SECRET', ''),  # OSS访问密钥密文
    'endpoint': os.getenv('OSS_ENDPOINT', ''),  # OSS访问端点
    'bucket': os.getenv('OSS_BUCKET', ''),  # OSS存储桶名称
    'internal': os.getenv('OSS_USE_INTERNAL', 'false').lower() == 'true',  # 是否使用内网
    'temp_dir': 'audio',  # 临时音频文件存储目录
    'url_expiration': int(os.getenv('OSS_URL_EXPIRATION', '86400')),  # URL签名过期时间（秒）
    'retry_times': int(os.getenv('OSS_RETRY_TIMES', '3')),  # 上传重试次数
    'retry_delay': int(os.getenv('OSS_RETRY_DELAY', '1')),  # 重试间隔（秒）
    'required_vars': [  # 必需的环境变量列表
        'OSS_ACCESS_KEY',
        'OSS_ACCESS_SECRET',
        'OSS_ENDPOINT',
        'OSS_BUCKET'
    ]
} 
