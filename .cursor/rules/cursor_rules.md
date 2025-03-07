# Cursor 行为约束规则

## 0. 代码保护规则

### 0.1 受保护模块定义
以下模块被视为稳定模块，除非用户明确要求，否则禁止修改：

1. **核心基础设施**
```text
src/
├── config/          # 配置管理模块
├── logger/          # 日志系统模块
└── cli/            # 命令行接口模块
```

2. **关键接口定义**
```text
src/
├── interfaces/     # 接口定义文件
└── types/         # 类型定义文件
```

3. **稳定工具类**
```text
src/utils/
├── decorators.py   # 装饰器
├── validators.py   # 验证器
└── constants.py    # 常量定义
```

### 0.2 保护级别定义

1. **完全锁定（Level 3）**
- 适用范围：配置结构、接口定义、命令行参数
- 限制条件：除非用户明确要求，完全禁止修改
- 示例文件：
  ```text
  src/config/schema.py
  src/interfaces/*.py
  src/cli/parser.py
  ```

2. **高度保护（Level 2）**
- 适用范围：日志系统、核心工具类、异常定义
- 限制条件：只允许修复严重bug，禁止功能改动
- 示例文件：
  ```text
  src/logger/*.py
  src/utils/core/*.py
  src/exceptions/*.py
  ```

3. **普通保护（Level 1）**
- 适用范围：辅助工具、非核心功能
- 限制条件：允许bug修复，但需要明确说明原因
- 示例文件：
  ```text
  src/utils/helpers/*.py
  src/tools/common/*.py
  ```

### 0.3 修改请求规范

当需要修改受保护模块时，必须：

1. **明确声明修改意图**
```text
请求修改受保护模块：src/logger/formatter.py
修改原因：修复日志格式化错误
影响范围：仅影响日志输出格式，不影响日志记录逻辑
```

2. **提供详细的修改计划**
```text
修改内容：
- 修复 ServiceFormatter 中的时间格式化问题
- 不涉及其他格式化逻辑
- 不改变现有的日志结构
```

3. **评估修改风险**
```text
风险评估：
- 影响范围：仅影响日志时间显示
- 兼容性：完全向后兼容
- 依赖关系：不影响其他模块
```

### 0.4 文件匹配规则

使用 glob 模式定义受保护文件：

```python
PROTECTED_PATTERNS = [
    # 完全锁定
    "src/config/schema.py",
    "src/interfaces/*.py",
    "src/cli/*.py",
    
    # 高度保护
    "src/logger/**/*.py",
    "src/utils/core/*.py",
    
    # 普通保护
    "src/utils/helpers/*.py"
]

def is_protected(file_path: str) -> Tuple[bool, int]:
    """检查文件是否受保护
    
    Returns:
        (is_protected, protection_level)
    """
    for pattern in PROTECTED_PATTERNS:
        if fnmatch(file_path, pattern):
            return True, get_protection_level(pattern)
    return False, 0
```

## 1. 代码修改基本原则

### 1.1 最小修改原则
- 仅修改与 bug 直接相关的代码行
- 禁止"优化"或"重构"周边代码
- 禁止更改现有函数签名
- 禁止修改配置结构

### 1.2 保持一致性原则
- 必须遵循现有的代码风格
- 必须使用已定义的异常类型
- 必须使用现有的日志格式
- 禁止引入新的依赖

### 1.3 配置访问原则
- 必须通过 transcriber.config 访问配置
- 禁止创建配置副本
- 禁止使用硬编码值
- 禁止修改配置结构

## 2. 代码修改范围限制

### 2.1 允许的修改
```python
# 允许的修改示例
def process_video(self, url: str) -> Dict[str, str]:
    # 允许添加参数验证
    if not url:
        raise ValueError("URL cannot be empty")
        
    # 允许添加日志
    self.logger.debug(f"Processing video: {url}")
    
    # 允许修复错误的配置访问
    temp_dir = self.transcriber.config.dirs.temp_dir  # 正确
    # temp_dir = self.config.dirs['temp']  # 错误
```

### 2.2 禁止的修改
```python
# 禁止的修改示例
# 1. 禁止修改类定义
class VideoProcessingTool(BaseTool):  # 禁止修改继承关系
    def __init__(self, config):  # 禁止修改初始化参数
        pass

# 2. 禁止添加新的类属性
class TranscriptionTool(BaseTool):
    custom_config = {}  # 禁止添加新的类属性

# 3. 禁止修改现有方法签名
def process_video(self, url: str, options: Dict = None):  # 禁止添加新参数
    pass
```

## 3. 错误修复规范

### 3.1 异常处理
```python
# 正确的异常处理
try:
    result = self._process_video(url)
except VideoProcessError as e:
    self.logger.error(f"Video processing failed: {str(e)}")
    raise  # 必须向上传递异常

# 错误的异常处理
try:
    result = self._process_video(url)
except Exception as e:  # 禁止捕获通用异常
    print(f"Error: {e}")  # 禁止使用 print
    return None  # 禁止吞掉异常
```

### 3.2 日志记录
```python
# 正确的日志记录
self.logger.error(
    "Failed to process video",
    extra={
        "url": url,
        "error": str(e),
        "stack_trace": traceback.format_exc()
    }
)

# 错误的日志记录
print(f"Error: {e}")  # 禁止使用 print
logging.error(f"Failed: {e}")  # 禁止使用全局 logging
```

## 4. 资源管理规范

### 4.1 文件操作
```python
# 正确的文件操作
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 错误的文件操作
f = open(file_path, 'w')  # 禁止不使用 with 语句
f.write(content)
f.close()
```

### 4.2 临时文件管理
```python
# 正确的临时文件管理
temp_path = os.path.join(self.transcriber.config.dirs.temp_dir, filename)
try:
    # 使用临时文件
    pass
finally:
    if os.path.exists(temp_path):
        os.remove(temp_path)

# 错误的临时文件管理
temp_path = "/tmp/file.txt"  # 禁止使用硬编码路径
# 禁止不清理临时文件
```

## 5. 配置访问规范

### 5.1 正确的配置访问
```python
# 正确的配置访问
class VideoProcessingTool(BaseTool):
    def __init__(self, transcriber: Any):
        self.transcriber = transcriber
        self.config = transcriber.config  # 通过 transcriber 访问配置

    def process(self):
        temp_dir = self.transcriber.config.dirs.temp_dir
        model_name = self.transcriber.config.models.video.name
```

### 5.2 禁止的配置访问
```python
# 错误的配置访问
class VideoProcessingTool(BaseTool):
    def __init__(self, config: Any):
        self.config = config  # 禁止直接保存配置对象
        
    def process(self):
        temp_dir = "/tmp"  # 禁止硬编码
        model_name = self.config.get('model', 'default')  # 禁止使用字典访问
```

## 6. 代码修改检查清单

### 6.1 修改前检查
- [ ] 确认 bug 的根本原因
- [ ] 确认修改范围最小化
- [ ] 确认不影响其他功能
- [ ] 确认符合程序结构文档

### 6.2 修改后检查
- [ ] 验证异常处理完整性
- [ ] 验证日志记录规范性
- [ ] 验证资源释放及时性
- [ ] 验证配置访问正确性

## 7. 禁止事项清单

### 7.1 绝对禁止
1. 禁止修改现有类的继承关系
2. 禁止修改现有方法的签名
3. 禁止添加新的类属性
4. 禁止修改配置结构
5. 禁止引入新的依赖
6. 禁止使用硬编码值
7. 禁止直接使用 print 语句
8. 禁止捕获通用 Exception
9. 禁止不清理临时资源
10. 禁止跳过任何初始化步骤

### 7.2 条件禁止
1. 禁止修改日志格式（除非修复日志相关bug）
2. 禁止修改错误码（除非修复错误处理相关bug）
3. 禁止修改配置键名（除非修复配置相关bug）
4. 禁止修改文件命名规则（除非修复存储相关bug） 