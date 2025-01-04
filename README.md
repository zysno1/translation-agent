# YouTube 视频转录与翻译工具

这是一个功能强大的 YouTube 视频转录和翻译工具，专门用于将 YouTube 视频内容转换为高质量的中文文本。本工具特别适合于 AI、机器学习系统(MLSys)、大语言模型(LLM) 和云原生领域的技术内容翻译。

## 功能特性

- 🎥 **视频处理**
  - 支持单个视频或批量处理
  - 自动提取视频音频
  - 智能音频格式转换和优化

- 🎯 **语音识别**
  - 使用阿里云 Paraformer-v2 模型
  - 支持时间戳标注
  - 高精度的语音转文字

- 🌐 **专业翻译**
  - 使用阿里云通义千问翻译引擎
  - 专注于技术领域翻译
  - 保留专业术语的准确性
  - 支持自定义术语表

- 📝 **文本处理**
  - Markdown 格式输出
  - 自动段落分割
  - 保留时间戳标记
  - Git 版本控制集成

- 🔄 **资源管理**
  - 自动清理临时文件
  - OSS 文件管理
  - 历史日志管理

- 📊 **详细日志**
  - 完整的处理过程记录
  - 调试模式支持
  - 错误追踪和异常处理
  - 成本估算和统计

## 环境要求

- Python 3.8+
- FFmpeg
- 阿里云账号和相关服务访问权限

## 安装步骤

1. 克隆仓库：
```bash
git clone [repository-url]
cd translation-agent
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
创建 `.env` 文件并设置以下变量：
```
OSS_ACCESS_KEY=你的OSS访问密钥
OSS_ACCESS_SECRET=你的OSS访问密钥密文
OSS_ENDPOINT=你的OSS访问端点
OSS_BUCKET=你的OSS存储桶名称
```

## 使用方法

### 处理单个视频

```bash
python src/youtube_transcriber.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 批量处理视频

```bash
python src/youtube_transcriber.py --file "video_urls.txt"
```

### 清理资源

```bash
python src/youtube_transcriber.py --clean
```

### 启用调试模式

添加 `--debug` 参数以获取详细日志：
```bash
python src/youtube_transcriber.py --url "VIDEO_URL" --debug
```

## 输出文件

- 原始转录文本：`transcripts/TIMESTAMP_TITLE_original.md`
- 翻译后文本：`transcripts/TIMESTAMP_TITLE_final.md`
- 处理日志：`logs/transcriber_TIMESTAMP.log`

## 注意事项

1. 确保有足够的磁盘空间用于临时文件
2. 检查网络连接稳定性
3. 注意 API 调用成本
4. 定期清理历史日志和临时文件

## 许可证

[许可证类型]

## 贡献指南

欢迎提交 Issue 和 Pull Request 