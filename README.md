# YouTube 视频转录与翻译工具

这是一个功能强大的 YouTube 视频转录和翻译工具，可以自动下载 YouTube 视频的音频，进行语音识别，并将识别结果翻译成中文。

## 功能特点

- 支持单个视频处理和批量处理
- 自动下载 YouTube 视频音频
- 使用阿里云语音识别服务进行转录
- 使用通义千问进行高质量翻译
- 支持断点续传和错误重试
- 详细的日志记录和进度显示
- 自动清理临时文件

## 环境要求

- Python 3.8 或更高版本
- FFmpeg（用于音频处理）

## 安装步骤

1. 克隆仓库：
```bash
git clone [仓库地址]
cd translation-agent
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
创建 `.env` 文件并添加以下配置：
```
OSS_ACCESS_KEY=你的阿里云OSS访问密钥
OSS_ACCESS_SECRET=你的阿里云OSS访问密钥密文
OSS_ENDPOINT=你的阿里云OSS终端节点
OSS_BUCKET=你的阿里云OSS存储桶名称
DASHSCOPE_API_KEY=你的通义千问API密钥
```

## 使用方法

### 处理单个视频

```bash
python src/youtube_transcriber.py --url https://www.youtube.com/watch?v=xxxxx
```

### 批量处理视频

1. 创建包含视频URL的文本文件（每行一个URL）
2. 运行命令：
```bash
python src/youtube_transcriber.py --file video_urls.txt
```

### 清理缓存文件

```bash
python src/youtube_transcriber.py --clean
```

### 调试模式

```bash
python src/youtube_transcriber.py --url https://www.youtube.com/watch?v=xxxxx --debug
```

## 输出文件

程序会在 `transcripts` 目录下生成以下文件：
- `*_original.md`: 原始英文转写文本
- `*_translated.md`: 中文翻译文本

## 注意事项

1. 确保有足够的磁盘空间用于临时文件
2. 需要稳定的网络连接
3. 请确保已正确配置所有环境变量
4. 处理长视频时可能需要较长时间
5. 建议使用专业版通义千问API以获得更好的翻译质量

## 错误处理

- 如果遇到网络错误，程序会自动重试
- 详细的错误日志保存在 `logs` 目录下
- 使用 `--debug` 参数可以查看更详细的调试信息

## 许可证

MIT License 