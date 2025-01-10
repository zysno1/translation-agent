# YouTube视频转录工具

这是一个功能强大的YouTube视频转录工具，支持视频音频提取、语音识别、中文翻译和内容总结等功能。

## 主要功能

- 支持单个视频和批量视频处理
- 自动下载YouTube视频音频
- 使用阿里云Paraformer-v2模型进行语音识别
- 使用通义千问进行英译中翻译
- 支持内容智能总结
- 详细的日志记录和进度跟踪
- Token使用统计和费用计算
- 自动清理临时文件
- 支持OSS文件存储

## 环境要求

- Python 3.8+
- FFmpeg
- 阿里云账号（用于语音识别和翻译）
- OSS存储空间
- DashScope API密钥

## 安装步骤

1. 克隆仓库：
```bash
git clone [repository_url]
cd translation-agent
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 安装FFmpeg：
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# 请从官网下载并添加到系统PATH
```

4. 配置环境变量：
创建 `.env` 文件并添加以下配置：
```
OSS_ACCESS_KEY=your_access_key
OSS_ACCESS_SECRET=your_access_secret
OSS_ENDPOINT=your_endpoint
OSS_BUCKET=your_bucket
DASHSCOPE_API_KEY=your_api_key
```

## 目录结构

```
translation-agent/
├── src/
│   ├── youtube_transcriber.py  # 主程序
│   └── config.py              # 配置文件
├── logs/                      # 日志目录
├── temp/                      # 临时文件目录
├── output/                    # 输出目录
├── transcripts/              # 转写文本目录
├── requirements.txt          # 依赖包列表
└── README.md                # 说明文档
```

## 使用说明

1. 处理单个视频：
```bash
python src/youtube_transcriber.py --url https://www.youtube.com/watch?v=xxxxx
```

2. 批量处理视频：
```bash
python src/youtube_transcriber.py --file video_urls.txt
```

3. 清理缓存：
```bash
python src/youtube_transcriber.py --clean
```

4. 调试模式：
```bash
python src/youtube_transcriber.py --url https://www.youtube.com/watch?v=xxxxx --debug
```

## 输出文件

程序会在 `transcripts` 目录下生成以下文件：

- `{timestamp}_{video_id}_original.md`: 原始英文转写文本
- `{timestamp}_{video_id}_translated.md`: 中文翻译文本
- `{timestamp}_{video_id}_summary.md`: 内容总结（如果启用）

## 日志系统

程序使用多级日志系统，所有日志文件存储在 `logs` 目录：

- `info_{timestamp}.log`: 程序正常执行的日志
- `error_{timestamp}.log`: 错误日志
- `debug_{timestamp}.log`: 调试日志
- `asr_{timestamp}.log`: 语音识别模块日志
- `translate_{timestamp}.log`: 翻译模块日志

## 费用说明

程序使用阿里云服务，包含以下费用：

- 语音识别 (Paraformer-v2): ¥0.00008/秒
- 文本翻译 (通义千问系列):
  - Qwen-Plus: ¥0.1/1K tokens
  - Qwen-Turbo: ¥0.008/1K tokens
  - Qwen-Max: ¥0.2/1K tokens

每次处理完成后会显示详细的费用统计。

## 注意事项

1. 请确保有足够的磁盘空间用于存储临时文件
2. 建议使用稳定的网络连接
3. 处理长视频时可能需要较长时间
4. 请注意API调用费用

## 错误处理

程序包含完善的错误处理机制：

- 自动重试机制（网络错误、超时等）
- 详细的错误日志记录
- 异常情况下的资源自动清理

## 开发说明

- 代码使用Python类型注解
- 遵循PEP 8编码规范
- 使用装饰器进行日志记录和重试处理
- 支持异步处理和并发操作

## 许可证

MIT License 