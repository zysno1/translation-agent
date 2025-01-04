# YouTube 视频转录工具

这是一个功能强大的 YouTube 视频转录工具，可以自动下载视频、提取音频、进行语音识别，并生成带时间戳的中文文稿。

## 主要功能

- 🎥 支持下载任意 YouTube 视频
- 🔊 自动提取和处理音频
- 🎯 高精度的语音识别（支持英文和中文）
- ⏱ 生成带时间戳的转录文本
- 🔄 英文内容自动翻译为中文
- 📝 文本智能优化和格式化
- 🖼 生成带视频截图的 HTML 报告
- 💾 支持断点续传和进度保存
- 📊 详细的处理进度和剩余时间显示
- 📝 Git 版本控制支持
- 🧹 资源清理功能

## 环境要求

- Python 3.8 或更高版本
- FFmpeg（用于音视频处理）
- Git（用于版本控制）

## 安装依赖

```bash
pip install -r requirements.txt
```

## 环境变量配置

在项目根目录创建 `.env` 文件，配置以下环境变量：

```
DASHSCOPE_API_KEY=your_api_key
OSS_ACCESS_KEY=your_oss_access_key
OSS_ACCESS_SECRET=your_oss_access_secret
OSS_ENDPOINT=your_oss_endpoint
OSS_BUCKET=your_oss_bucket
```

## 使用方法

### 处理单个视频
- `--url`: 指定单个YouTube视频URL进行处理
  ```bash
  python src/youtube_transcriber.py --url "https://www.youtube.com/watch?v=xxxxx"
  ```

### 批量处理视频
- `--file`: 指定包含YouTube视频URL列表的文件路径
  ```bash
  python src/youtube_transcriber.py --file "urls.txt"
  ```
  文件格式要求：
  - 每行一个URL
  - 忽略空行
  - 文本文件编码为UTF-8

### 清理资源
- `--clean`: 清理所有中间文件和缓存（包括日志、音视频文件和 OSS 资源）
  ```bash
  python src/youtube_transcriber.py --clean
  ```
  清理范围包括：
  - `outputs/` 目录下的所有文件（包括状态文件和图片）
  - `logs/` 目录下的所有日志文件
  - 临时音频文件（`audio_*.wav`、`*.wav_processed.wav`、`*.wav_chunk_*.wav`）
  - 临时视频文件（`video_*.mp4`）
  - OSS 存储中的音频文件
  - 可选：清理 `transcripts/` 目录（会提示确认）

## 输出文件

- `transcripts/`: 最终的转录文稿（Markdown 格式）
- `outputs/`: 中间处理文件和状态信息
- `logs/`: 处理日志文件

## 注意事项

1. 确保系统已安装 FFmpeg
2. 需要稳定的网络连接
3. 处理大视频时需要足够的磁盘空间
4. API 调用会产生费用，请注意余额
5. 批量处理时，如果某个视频处理失败，程序会继续处理下一个视频

## 常见问题

1. 使用 `--clean` 可以清理所有中间文件和日志
2. 清理操作会保留当前正在使用的日志文件
3. 批量处理时的错误会被记录在日志文件中

## 更新日志

### 2024.01
- 添加了批量处理视频功能
- 添加了资源清理功能
- 优化了错误处理和日志记录 