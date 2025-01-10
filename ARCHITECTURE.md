# 程序架构说明

## 核心模块结构

```
YouTubeTranscriber
├── 初始化组件
│   ├── 配置管理 (config.py)
│   ├── 日志系统 (ServiceFormatter)
│   └── 进度跟踪 (ProgressTracker)
├── 视频处理流水线
│   ├── 下载模块
│   ├── 音频处理模块
│   ├── 语音识别模块
│   ├── 文本处理模块
│   └── 翻译模块
└── 资源管理模块
    ├── 文件管理
    ├── OSS存储
    └── 清理机制
```

## 模块依赖关系

### 1. 配置层
- `config.py`: 全局配置中心
  - 目录配置 (DIR_CONFIG)
  - 模型配置 (MODEL_CONFIG)
  - OSS配置 (OSS_CONFIG)
  - 提示词配置 (PROMPT_CONFIG)

### 2. 核心服务层
- `ServiceFormatter`: 日志格式化
  - 依赖: logging
  - 扩展点: 可自定义日志字段

- `ProgressTracker`: 进度跟踪
  - 依赖: logging
  - 扩展点: 可添加新的处理步骤

### 3. 处理流水线
- 下载模块
  - 主要类: `YouTubeTranscriber.download_video`
  - 依赖: yt-dlp
  - 扩展点: 支持其他视频平台

- 音频处理模块
  - 主要类: `YouTubeTranscriber.extract_audio`
  - 依赖: ffmpeg, pydub
  - 扩展点: 支持更多音频格式

- 语音识别模块
  - 主要类: `YouTubeTranscriber.recognize_speech`
  - 依赖: dashscope
  - 扩展点: 支持其他ASR服务

- 文本处理模块
  - 主要类: `YouTubeTranscriber.process_text`
  - 依赖: re
  - 扩展点: 自定义文本处理规则

- 翻译模块
  - 主要类: `YouTubeTranscriber.translate_text`
  - 依赖: dashscope
  - 扩展点: 支持其他翻译服务

### 4. 资源管理层
- 文件管理
  - 主要类: `YouTubeTranscriber.track_temp_file`, `track_output_file`
  - 依赖: os
  - 扩展点: 自定义文件命名规则

- OSS存储
  - 主要类: `YouTubeTranscriber.upload_to_oss`
  - 依赖: oss2
  - 扩展点: 支持其他云存储服务

## 扩展指南

### 1. 添加新的处理步骤
1. 在 `ProgressTracker.STEPS` 中添加新步骤
2. 实现相应的处理方法
3. 在 `process_video` 中集成新步骤

### 2. 支持新的服务提供商
1. 在 `config.py` 中添加新的服务配置
2. 实现服务调用接口
3. 添加相应的日志处理

### 3. 自定义输出格式
1. 修改 `save_*_text` 方法
2. 更新文件模板定义
3. 实现新的格式化逻辑

### 4. 优化性能
1. 使用 `@retry_on_timeout` 装饰器处理超时
2. 实现并行处理逻辑
3. 优化资源清理策略

## 关键扩展点

### 1. 服务适配器
```python
class ServiceAdapter:
    """服务适配器基类"""
    def __init__(self, config):
        self.config = config
        
    @abstractmethod
    def process(self, input_data):
        pass
```

### 2. 处理器链
```python
class ProcessorChain:
    """处理器链基类"""
    def __init__(self):
        self.processors = []
        
    def add_processor(self, processor):
        self.processors.append(processor)
        
    def process(self, data):
        for processor in self.processors:
            data = processor.process(data)
        return data
```

### 3. 输出格式器
```python
class OutputFormatter:
    """输出格式器基类"""
    def __init__(self, template):
        self.template = template
        
    @abstractmethod
    def format(self, data):
        pass
```

## 最佳实践

### 1. 添加新功能
1. 确定功能所属模块
2. 实现必要的接口
3. 添加配置项
4. 更新进度跟踪
5. 添加日志记录
6. 实现错误处理
7. 更新文档

### 2. 修改现有功能
1. 确认影响范围
2. 保持接口兼容
3. 更新配置文件
4. 添加必要的日志
5. 进行充分测试
6. 更新文档

### 3. 性能优化
1. 识别瓶颈
2. 实现缓存机制
3. 优化并发处理
4. 改进资源管理
5. 监控性能指标

## 注意事项

1. 保持模块间低耦合
2. 遵循单一职责原则
3. 保持配置的灵活性
4. 确保日志的完整性
5. 妥善处理异常情况
6. 注意资源的及时释放
7. 保持代码的可测试性

## 常见修改场景

### 1. 添加新的翻译模型
```python
# 1. 在config.py中添加模型配置
MODEL_CONFIG['translation']['available_models']['new_model'] = {
    'api_params': {...},
    'price_per_1k_tokens': 0.xx
}

# 2. 实现模型调用
def translate_with_new_model(self, text):
    # 实现翻译逻辑
    pass
```

### 2. 优化音频处理
```python
# 1. 添加新的音频处理选项
AUDIO_CONFIG = {
    'format': 'wav',
    'sample_rate': 16000,
    'channels': 1,
    'quality': 'high'
}

# 2. 实现处理逻辑
def process_audio(self, audio_path, config):
    # 实现音频处理逻辑
    pass
```

### 3. 扩展输出格式
```python
# 1. 添加新的输出格式器
class JSONFormatter(OutputFormatter):
    def format(self, data):
        return json.dumps(data, ensure_ascii=False)

# 2. 注册格式器
self.formatters['json'] = JSONFormatter()
``` 