import os
import pytest
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

# 设置测试环境变量
@pytest.fixture(autouse=True)
def setup_test_env():
    """设置测试环境变量"""
    os.environ["DASHSCOPE_API_KEY"] = "test_api_key"
    os.environ["OSS_ACCESS_KEY"] = "test_access_key"
    os.environ["OSS_ACCESS_SECRET"] = "test_access_secret"
    os.environ["OSS_ENDPOINT"] = "test.endpoint.com"
    os.environ["OSS_BUCKET"] = "test-bucket"
    
    yield
    
    # 清理环境变量
    test_vars = [
        "DASHSCOPE_API_KEY",
        "OSS_ACCESS_KEY",
        "OSS_ACCESS_SECRET",
        "OSS_ENDPOINT",
        "OSS_BUCKET"
    ]
    for var in test_vars:
        os.environ.pop(var, None) 