# YouTube视频转录工具

这是一个功能强大的YouTube视频转录工具，支持视频音频提取、语音识别、中文翻译等功能。

## 主要功能

- 支持单个视频和批量视频处理
- 自动下载YouTube视频音频
- 使用阿里云Paraformer-v2模型进行语音识别
- 使用通义千问进行英译中翻译
- 支持Token统计和费用计算
- 详细的日志记录系统
- 自动清理临时文件
- 支持OSS文件存储

## 环境要求

- Python 3.8+
- FFmpeg
- 阿里云账号（用于语音识别和翻译）
- OSS存储空间

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

- `transcripts/`: 存放转写和翻译结果
- `logs/`: 存放详细的运行日志
  - `info_{timestamp}.log`: 程序运行日志
  - `error_{timestamp}.log`: 错误日志
  - `debug_{timestamp}.log`: 调试日志
  - `asr_{timestamp}.log`: 语音识别日志
  - `translate_{timestamp}.log`: 翻译日志

## 高级功能

### 费用统计
- 自动统计语音识别和翻译的Token使用量
- 计算处理成本
- 支持费用预警

### 错误处理
- 自动重试机制
- 详细的错误日志
- 断点续传支持

### 格式化输出
- Markdown格式输出
- 时间戳对齐
- 分段处理长文本

## 配置说明

### 语音识别配置
- 模型：Paraformer-v2
- 采样率：16kHz
- 声道：单声道

### 翻译配置
- 模型：通义千问系列
- 支持批量翻译
- 自动分段处理

### OSS配置
- 支持临时文件自动清理
- 文件访问URL过期时间可配置
- 支持自定义存储路径

## 注意事项

1. 请确保有足够的磁盘空间
2. 需要稳定的网络连接
3. 注意API调用限制和费用
4. 定期清理临时文件
5. 遵守YouTube使用条款

## 许可证

MIT License 