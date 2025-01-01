# YouTube 视频转录与翻译工具

这是一个功能强大的 YouTube 视频处理工具，可以自动提取视频音频、进行语音识别、翻译和文本优化。该工具使用通义千问的 AI 模型进行语音识别和文本处理，特别适合处理 AI 和技术相关的内容。

## 主要功能

1. **视频音频提取**
   - 自动从 YouTube 视频中提取音频
   - 支持音频格式转换和预处理
   - 智能处理大文件，自动分片处理

2. **语音识别**
   - 使用通义千问 SenseVoice API 进行高精度语音识别
   - 支持中文语音识别
   - 自动合并分片识别结果

3. **智能翻译**
   - 自动检测英文内容并翻译为中文
   - 保持 IT 和 AI 领域专业术语的准确性
   - 保留重要的英文术语和缩写

4. **文本优化**
   - 智能分段和格式化
   - 添加合适的标点符号
   - 保持原有的口语表达特点
   - 修正可能的识别错误

## 使用方法

### 1. 基础配置

1. **环境配置**
   ```bash
   # 克隆项目
   git clone https://github.com/your-username/translation-agent.git
   cd translation-agent

   # 安装依赖
   pip install -r requirements.txt

   # 配置环境变量
   cp .env.example .env
   # 编辑 .env 文件，填入你的 API 密钥
   ```

2. **配置密钥**
   在 `.env` 文件中设置以下环境变量：
   ```
   DASHSCOPE_API_KEY=your_api_key_here
   ```

### 2. 使用示例

#### 基本使用
```bash
# 直接运行程序
python src/youtube_transcriber.py

# 程序会提示输入视频链接
请输入 YouTube 视频链接: https://www.youtube.com/watch?v=xxxxx
```

#### 处理不同类型的视频

1. **处理中文视频**
```python
from youtube_transcriber import YouTubeTranscriber

transcriber = YouTubeTranscriber()
# 中文技术分享视频
transcriber.process_video(
    "https://www.youtube.com/watch?v=xxxxx",
    "output_chinese.txt"
)
```

2. **处理英文视频（自动翻译）**
```python
# 英文 AI 技术讲座，将自动翻译为中文
transcriber.process_video(
    "https://www.youtube.com/watch?v=yyyyy",
    "output_translated.txt"
)
```

3. **处理长视频**
```python
# 处理长视频时会自动分片
# 支持处理超过1小时的视频
transcriber.process_video(
    "https://www.youtube.com/watch?v=zzzzz",
    "output_long.txt"
)
```

#### 自定义处理

1. **仅提取音频**
```python
transcriber = YouTubeTranscriber()
audio_file = transcriber.extract_audio("https://www.youtube.com/watch?v=xxxxx")
print(f"音频已保存至: {audio_file}")
```

2. **仅进行语音识别**
```python
# 如果已有音频文件
audio_file = "path/to/your/audio.wav"
processed_file = transcriber.process_audio(audio_file)
text = transcriber.recognize_speech(processed_file)
print(text)
```

3. **仅进行翻译**
```python
# 如果已有英文文本
with open("english_text.txt", "r", encoding="utf-8") as f:
    english_text = f.read()
    
translated_text = transcriber.translate_text(english_text)
print(translated_text)
```

4. **仅进行文本优化**
```python
# 优化已有文本的格式
with open("raw_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    
polished_text = transcriber.polish_text(raw_text)
print(polished_text)
```

### 3. 输出示例

原始英文内容：
```
Today we're going to talk about machine learning and AI. First, let's look at what CNN and RNN are...
```

翻译后的内容：
```
今天我们将讨论机器学习和 AI。首先，让我们来看看什么是 CNN 和 RNN...
```

### 4. 常见使用场景

1. **技术演讲转录**
   - AI 会议演讲
   - 技术分享会
   - 在线课程

2. **多语言内容处理**
   - 英文技术视频翻译
   - 国际会议记录
   - 技术文档本地化

3. **学习资料整理**
   - MOOC 课程笔记
   - 技术讲座归档
   - 研究资料整理

### 5. 处理提示

- 建议将较长的视频分成小段处理
- 确保音频质量良好，背景噪音较少
- 对于专业术语较多的内容，可以多次优化翻译结果
- 处理大文件时，确保有足够的磁盘空间

## 技术特点

- 使用 `yt_dlp` 进行视频下载和音频提取
- 使用 `pydub` 进行音频处理
- 集成通义千问的 AI 模型进行语音识别和文本处理
- 智能处理大文件，自动分片上传和处理
- 专业的 AI 和 IT 领域翻译能力

## 未来计划

1. **功能增强**
   - [ ] 支持更多视频平台（如 Bilibili、Twitter 等）
   - [ ] 添加字幕生成功能
   - [ ] 支持更多语言的翻译
   - [ ] 添加语音识别结果的时间戳

2. **性能优化**
   - [ ] 优化大文件处理性能
   - [ ] 添加并行处理能力
   - [ ] 实现断点续传功能

3. **用户体验**
   - [ ] 添加图形用户界面
   - [ ] 提供批量处理功能
   - [ ] 添加处理进度显示
   - [ ] 支持自定义输出格式

4. **其他计划**
   - [ ] 添加更多文本后处理选项
   - [ ] 支持导出不同格式（如 SRT、VTT 等）
   - [ ] 添加语音识别质量评估
   - [ ] 提供 API 接口

## 注意事项

- 需要有效的通义千问 API 密钥
- 处理大视频时需要足够的磁盘空间
- 确保网络连接稳定
- 遵守 YouTube 的使用条款和版权规定

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License 