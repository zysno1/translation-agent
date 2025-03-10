# YouTube视频处理系统

一个用于下载、转写、翻译和分析YouTube视频的个人工具。

## 功能特点

- **视频下载**：支持从YouTube和其他平台下载视频
- **转写功能**：将视频音频转为文本，支持时间戳
  - **智能转录策略**：自动根据音频长度选择最佳转录方法
  - **长音频支持**：通过OSS云存储支持超长音频文件转录
- **翻译能力**：将转写文本翻译成中文
- **智能分析**：生成内容摘要和关键点
- **多种输出**：支持多种格式导出(Markdown, SRT, TXT)
- **批量处理**：支持批量处理视频队列
- **性能监控**：精确追踪音频提取、转写和翻译的处理时间
- **详细报告**：生成包含处理统计和时间数据的详细报告

## 安装

### 环境要求

- Python 3.8+
- FFmpeg
- oss2 (用于阿里云OSS上传功能)

### 安装步骤

1. 克隆仓库
   ```bash
   git clone https://github.com/zysno1/translation-agent.git
   cd translation-agent
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 安装FFmpeg (如果尚未安装)
   - macOS: `brew install ffmpeg`
   - Ubuntu: `sudo apt install ffmpeg`
   - Windows: 使用[官方下载](https://ffmpeg.org/download.html)

4. 设置API密钥
   创建`.env`文件并添加以下内容:
   ```
   OPENAI_API_KEY=你的OpenAI密钥
   DASHSCOPE_API_KEY=你的通义千问密钥
   
   # OSS配置（用于长音频处理）
   OSS_BUCKET_NAME=你的OSS桶名
   OSS_ACCESS_KEY_ID=你的OSS访问密钥ID
   OSS_ACCESS_KEY_SECRET=你的OSS访问密钥密码
   OSS_ENDPOINT=oss-cn-beijing.aliyuncs.com
   ```

## 使用方法

### 命令行选项

```bash
python main.py --url "https://www.youtube.com/watch?v=example" --verbose
```

#### 输入选项(必选其一)

- `--url` - YouTube视频URL
- `--file` - 本地视频文件路径
- `--batch` - 批量处理队列文件

#### 输出选项

- `--template` - 报告模板，可选: default, academic, business (默认: default)
- `--cleanup` - 处理完成后清理中间文件
- `--config` - 指定配置文件路径 (默认: config.yaml)
- `--verbose` - 显示详细日志

> 注意：内容摘要现在是默认生成的，`--summarize` 参数仍然存在但已废弃。

### 示例

1. 处理单个YouTube视频:
   ```bash
   python main.py --url "https://www.youtube.com/watch?v=example"
   ```

2. 处理本地视频文件并使用学术报告模板:
   ```bash
   python main.py --file "path/to/video.mp4" --template academic
   ```

3. 批量处理视频队列:
   ```bash
   python main.py --batch "video_queue.txt" --cleanup
   ```

4. 启用详细日志输出:
   ```bash
   python main.py --url "https://www.youtube.com/watch?v=example" --verbose
   ```

## 配置文件

默认配置文件为`config.yaml`，包含以下主要设置:

```yaml
# 默认模型设置
defaults:
  transcription: "paraformer-v2"  # 默认转写模型
  translation: "qwen-max"         # 默认翻译模型
  summarization: "qwen-long"      # 默认摘要模型
  report_template: "default"      # 默认报告模板
  llm: "qwen-max"                 # 默认LLM模型

# 环境设置
environment: "personal"  # 可选: personal, work, test

# API密钥 (从环境变量加载)
api_keys:
  openai: "${OPENAI_API_KEY}"
  dashscope: "${DASHSCOPE_API_KEY}"
  qwen: "${DASHSCOPE_API_KEY}"

# 存储路径
storage:
  temp_dir: "./temp"
  data_dir: "./data"
  reports_dir: "./reports"
  logs_dir: "./logs"
  # OSS配置
  oss:
    access_key_id: "${OSS_ACCESS_KEY_ID}"
    access_key_secret: "${OSS_ACCESS_KEY_SECRET}"
    bucket_name: "${OSS_BUCKET_NAME}"
    endpoint: "${OSS_ENDPOINT}"
    prefix: "audio"

# 翻译设置
translation:
  parallel:
    enabled: true          # 是否启用并行翻译
    min_video_length: 1200 # 启用并行翻译的最小视频长度（秒），默认为20分钟
    max_workers: 16        # 最大并行工作线程数
```

完整配置文件包含更多高级设置，如摘要策略、日志配置、LangChain模板等。每个部分都有详细注释，便于理解和自定义。

## 时间追踪功能

系统内置了精确的时间追踪功能，用于监控处理管道中的各个阶段：

- **音频提取时间**：从视频中提取音频的处理时间
- **转写时间**：将音频转换为文本的处理时间
- **翻译时间**：将文本从源语言翻译到目标语言的处理时间
- **摘要生成时间**：生成内容摘要的处理时间

这些时间指标会自动计算并显示在生成的报告中，方便用户了解每个处理阶段的性能表现。时间信息也会在控制台输出中实时显示，特别是在启用`--verbose`模式时。

## 智能转录策略

系统采用智能转录策略，根据音频长度自动选择最佳转录方法：

- **短音频**（≤30分钟）：使用实时转录API，直接本地处理
- **长音频**（>30分钟）：使用文件转录API，先将文件上传到OSS，再通过预签名URL提交转录任务
- **备选策略**：如果OSS上传失败，系统会自动将长音频分段处理，并合并结果

## 目录结构

```
.
├── main.py                 # 主入口文件
├── config.yaml             # 配置文件
├── requirements.txt        # 依赖文件
├── README.md               # 本文件
├── src/                    # 源代码
│   ├── config/             # 配置管理
│   ├── models/             # 模型接口
│   ├── preprocessing/      # 视频预处理
│   ├── transcription/      # 转写服务
│   ├── translation/        # 翻译服务
│   ├── analysis/           # 内容分析
│   ├── reports/            # 报告生成
│   ├── storage/            # 存储管理
│   └── utils/              # 工具函数
│       ├── audio_utils.py  # 音频处理工具
│       ├── oss_utils.py    # OSS上传工具
│       └── ...
├── data/                   # 数据目录  
│   ├── transcripts/        # 转写结果
│   ├── translations/       # 翻译结果
│   ├── summaries/          # 摘要结果
│   ├── processed/          # 处理数据
│   ├── outputs/            # 输出数据
│   ├── raw/                # 原始数据
│   └── archive/            # 归档数据
├── reports/                # 输出报告
├── temp/                   # 临时文件
└── logs/                   # 日志文件
    ├── app.log             # 所有级别日志
    ├── debug.log           # 仅DEBUG级别日志
    └── error.log           # 仅ERROR及以上级别日志
```

## 许可证

本项目仅供个人学习和使用。