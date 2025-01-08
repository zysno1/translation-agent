# YouTube 视频转录与翻译工具 - 程序结构文档

## 1. 装饰器

### 1.1 log_service_call
- **功能**: 服务调用日志装饰器
- **参数**: 
  - service: 服务名称 ('ASR', 'Translate', 'OSS')
  - api: API名称
- **作用**: 记录API调用的开始、结束、耗时和结果

### 1.2 retry_on_timeout
- **功能**: 处理API调用超时的重试装饰器
- **参数**:
  - max_retries: 最大重试次数
  - base_delay: 基础延迟时间（秒）
- **作用**: 在超时或网络错误时自动重试

## 2. 工具类

### 2.1 ServiceFormatter (logging.Formatter)
- **功能**: 服务日志格式化器
- **属性**:
  - optional_fields: 可选字段及默认值
- **方法**:
  - format(record): 格式化日志记录

### 2.2 ProcessStep
- **功能**: 处理步骤的定义
- **属性**:
  - name: 步骤名称
  - weight: 权重
  - description: 描述
  - start_time: 开始时间
  - end_time: 结束时间
  - sub_progress: 子进度

### 2.3 ProgressTracker
- **功能**: 进度跟踪器
- **属性**:
  - STEPS: 处理步骤列表
  - current_step: 当前步骤
  - completed_steps: 已完成步骤
- **方法**:
  - start_step(step_name): 开始新步骤
  - complete_step(): 完成当前步骤
  - calculate_progress(): 计算总进度
  - update_progress(): 更新进度信息

## 3. 主类 YouTubeTranscriber

### 3.1 类属性
- DIRS: 目录结构配置
- FILE_TEMPLATES: 文件命名模板
- TRANSLATE_SYSTEM_PROMPT: 翻译系统提示词
- TRANSLATE_USER_PROMPT: 翻译用户提示词
- PRICE_PER_SECOND: 语音识别价格配置
- PRICE_PER_1K_TOKENS: Token价格配置

### 3.2 初始化相关方法
- **__init__(debug: bool = False)**
  - 初始化转写器
  - 加载配置
  - 创建目录
  - 设置日志
  - 初始化统计

- **setup_logging(debug: bool = False)**
  - 设置日志记录器
  - 配置不同类型的日志处理器

- **verify_env_variables()**
  - 验证必要的环境变量

### 3.3 核心功能方法
- **process_video(url: str) -> None**
  - 处理单个视频
  - 下载、转写、翻译的主流程

- **recognize_speech(audio_path: str, file_url: str) -> Optional[Dict]**
  - 识别音频文件中的语音
  - 调用语音识别API

- **translate_text(text: str) -> str**
  - 翻译文本
  - 调用翻译API

### 3.4 辅助功能方法
- **split_text_for_translation(text: str, max_tokens: int = 800) -> List[str]**
  - 分割文本用于翻译

- **merge_translated_segments(segments: List[str]) -> str**
  - 合并翻译后的文本片段

- **print_token_statistics() -> None**
  - 打印令牌使用和成本统计

### 3.5 文件处理方法
- **save_original_text(text: str, video_id: str, video_title: str) -> str**
  - 保存原始转写文本

- **save_translated_text(text: str, video_id: str, video_title: str) -> str**
  - 保存翻译后的文本

- **cleanup_temp_files(video_id: str = None) -> None**
  - 清理临时文件

## 4. 工作流程

### 4.1 初始化阶段
1. 加载环境变量和配置
2. 创建必要的目录结构
3. 设置日志记录器
4. 初始化模型配置和费用统计
5. 验证环境变量

### 4.2 视频处理流程
1. 下载视频并提取音频
2. 上传音频到OSS
3. 调用语音识别API
4. 处理识别结果
5. 翻译文本
6. 保存结果
7. 清理资源

### 4.3 错误处理机制
1. API调用重试机制
2. 错误日志记录
3. 资源清理
4. 异常处理和恢复

### 4.4 资源管理
1. 临时文件跟踪和清理
2. 输出文件管理
3. OSS资源管理
4. 日志文件管理

## 5. 配置系统

### 5.1 目录配置
- root: 根目录
- logs: 日志目录
- temp: 临时文件目录
- output: 输出目录
- transcripts: 转写文本目录

### 5.2 模型配置
- speech_recognition: 语音识别模型配置
- translation: 翻译模型配置
- text_optimization: 文本优化模型配置

### 5.3 OSS配置
- access_key: OSS访问密钥
- access_secret: OSS访问密钥密文
- endpoint: OSS访问端点
- bucket: OSS存储桶名称
- 其他OSS相关配置

## 6. 日志系统

### 6.1 日志类型
- info: 程序正常执行日志
- error: 错误日志
- debug: 调试日志
- asr: 语音识别模块日志
- translate: 翻译模块日志

### 6.2 日志格式
- 标准格式: 时间 - 级别 - 消息
- 服务格式: 时间 - 级别 - [服务] - 消息 - 请求ID - 耗时 - 状态 

## 7. 关键依赖关系

### 7.1 类之间的依赖
- ServiceFormatter -> logging.Formatter
- YouTubeTranscriber -> ServiceFormatter
- YouTubeTranscriber -> ProgressTracker
- ProgressTracker -> ProcessStep

### 7.2 外部服务依赖
- DashScope ASR API
  - 依赖配置: MODEL_CONFIG['speech_recognition']
  - 关键参数: model, api_params
  - 错误处理要求: 必须处理超时和网络错误

- DashScope Translation API
  - 依赖配置: MODEL_CONFIG['translation']
  - 关键参数: model, translation_options
  - 错误处理要求: 必须处理token限制和响应格式错误

- 阿里云 OSS
  - 依赖配置: OSS_CONFIG
  - 必需环境变量: access_key, access_secret, endpoint, bucket
  - 错误处理要求: 必须处理上传失败和URL过期

### 7.3 环境依赖
- Python 版本要求: >= 3.8
- 必需系统组件: ffmpeg
- 必需环境变量: 见 OSS_CONFIG['required_vars']

## 8. 状态管理

### 8.1 YouTubeTranscriber 实例状态
- total_tokens: 各模型的token使用统计
- total_costs: 各模型的成本统计
- temp_files: 临时文件列表
- output_files: 输出文件列表
- current_video_url: 当前处理的视频URL
- current_video_title: 当前处理的视频标题
- current_video_duration: 当前处理的视频时长

### 8.2 状态依赖和约束
1. 文件状态约束:
   - temp_files 中的文件必须存在
   - output_files 中的文件必须存在
   - 清理临时文件时不能删除正在使用的文件

2. 计费状态约束:
   - total_tokens 必须准确反映实际使用量
   - total_costs 必须与 total_tokens 对应
   - 费用计算必须使用正确的价格配置

3. 进度状态约束:
   - ProgressTracker 状态必须反映实际进度
   - 步骤状态转换必须遵循顺序

## 9. 数据流

### 9.1 视频处理流程
```
URL -> 视频ID -> 音频文件 -> OSS URL -> 识别结果 -> 文本片段 -> 翻译结果 -> 最终文件
```

### 9.2 关键数据转换点
1. 视频下载:
   - 输入: YouTube URL
   - 输出: 视频ID, 标题, 音频文件
   - 约束: 音频质量和大小限制

2. 语音识别:
   - 输入: 音频文件, OSS URL
   - 输出: 识别结果(包含时间戳)
   - 约束: API参数限制

3. 文本翻译:
   - 输入: 原始文本片段
   - 输出: 翻译后的文本
   - 约束: token数量限制

## 10. 关键约束和限制

### 10.1 资源限制
- 音频文件大小: <= 512MB (paraformer-v2)
- 单次翻译字符数: <= 2000
- 批量处理文件数: <= 100

### 10.2 API限制
- ASR API:
  - 支持的音频格式
  - 采样率要求
  - 并发请求限制

- Translation API:
  - 最大输入tokens
  - 最大输出tokens
  - 上下文长度限制

### 10.3 错误处理约束
- 必须处理的错误类型
- 重试策略要求
- 资源清理要求

### 10.4 性能约束
- 内存使用限制
- 临时文件处理策略
- 并发处理限制

## 11. 修改注意事项

### 11.1 高风险修改点
1. 费用计算逻辑
2. 文件清理逻辑
3. API参数处理
4. 错误重试逻辑
5. 状态管理逻辑

### 11.2 修改检查清单
1. 配置一致性检查
2. 状态完整性检查
3. 错误处理覆盖检查
4. 资源清理完整性检查
5. 日志记录完整性检查 