import os
import pytest
from unittest.mock import Mock, patch
from src.youtube_transcriber import (
    YouTubeTranscriber,
    VideoProcessingTool,
    TranscriptionTool,
    TranslationTool,
    StorageTool
)

@pytest.fixture
def mock_transcriber():
    """创建 YouTubeTranscriber 的 Mock 对象"""
    transcriber = Mock(spec=YouTubeTranscriber)
    transcriber.logger = Mock()
    return transcriber

class TestVideoProcessingTool:
    """测试视频处理工具"""
    
    def test_init(self, mock_transcriber):
        """测试工具初始化"""
        tool = VideoProcessingTool(mock_transcriber)
        assert tool.name == "video_processor"
        assert tool.transcriber == mock_transcriber
        
    def test_run_success(self, mock_transcriber):
        """测试正常执行"""
        # 设置 mock 返回值
        mock_transcriber.download_video.return_value = ("video123", "Test Video", "test.mp3")
        mock_transcriber.extract_audio.return_value = "test.wav"
        
        tool = VideoProcessingTool(mock_transcriber)
        result = tool._run("https://youtube.com/test")
        
        assert result == {
            "video_id": "video123",
            "video_title": "Test Video",
            "audio_path": "test.wav"
        }
        mock_transcriber.download_video.assert_called_once_with("https://youtube.com/test")
        mock_transcriber.extract_audio.assert_called_once_with("test.mp3", "video123")
        
    def test_run_download_failure(self, mock_transcriber):
        """测试下载失败的情况"""
        mock_transcriber.download_video.side_effect = Exception("Download failed")
        
        tool = VideoProcessingTool(mock_transcriber)
        with pytest.raises(RuntimeError) as exc_info:
            tool._run("https://youtube.com/test")
        assert "视频处理失败" in str(exc_info.value)

class TestTranscriptionTool:
    """测试音频转写工具"""
    
    def test_init(self, mock_transcriber):
        """测试工具初始化"""
        tool = TranscriptionTool(mock_transcriber)
        assert tool.name == "transcriber"
        assert tool.transcriber == mock_transcriber
        
    def test_run_success(self, mock_transcriber):
        """测试正常执行"""
        # 设置 mock 返回值
        mock_transcriber.upload_audio.return_value = "http://test.com/audio.wav"
        mock_transcriber.recognize_speech.return_value = {"results": [{"text": "test text"}]}
        mock_transcriber.extract_text_from_result.return_value = [("test text", 0, 10)]
        mock_transcriber.format_segments.return_value = "Test text with timestamp"
        
        tool = TranscriptionTool(mock_transcriber)
        result = tool._run("test.wav")
        
        assert result == "Test text with timestamp"
        mock_transcriber.upload_audio.assert_called_once_with("test.wav")
        mock_transcriber.recognize_speech.assert_called_once()
        mock_transcriber.extract_text_from_result.assert_called_once()
        mock_transcriber.format_segments.assert_called_once()
        
    def test_run_no_text_extracted(self, mock_transcriber):
        """测试未提取到文本的情况"""
        mock_transcriber.upload_audio.return_value = "http://test.com/audio.wav"
        mock_transcriber.recognize_speech.return_value = {"results": []}
        mock_transcriber.extract_text_from_result.return_value = []
        
        tool = TranscriptionTool(mock_transcriber)
        with pytest.raises(RuntimeError) as exc_info:
            tool._run("test.wav")
        assert "未能提取到任何文本" in str(exc_info.value)

class TestTranslationTool:
    """测试文本翻译工具"""
    
    def test_init(self, mock_transcriber):
        """测试工具初始化"""
        tool = TranslationTool(mock_transcriber)
        assert tool.name == "translator"
        assert tool.transcriber == mock_transcriber
        
    def test_run_success(self, mock_transcriber):
        """测试正常执行"""
        mock_transcriber.translate_text.return_value = "测试文本"
        
        tool = TranslationTool(mock_transcriber)
        result = tool._run("test text")
        
        assert result == "测试文本"
        mock_transcriber.translate_text.assert_called_once_with("test text")
        
    def test_run_translation_failure(self, mock_transcriber):
        """测试翻译失败的情况"""
        mock_transcriber.translate_text.return_value = None
        
        tool = TranslationTool(mock_transcriber)
        with pytest.raises(RuntimeError) as exc_info:
            tool._run("test text")
        assert "翻译失败" in str(exc_info.value)

class TestStorageTool:
    """测试存储工具"""
    
    def test_init(self, mock_transcriber):
        """测试工具初始化"""
        tool = StorageTool(mock_transcriber)
        assert tool.name == "storage"
        assert tool.transcriber == mock_transcriber
        
    def test_run_save_original(self, mock_transcriber):
        """测试保存原始文本"""
        mock_transcriber.save_original_text.return_value = "/path/to/original.md"
        
        tool = StorageTool(mock_transcriber)
        result = tool._run("test text", "original", "video123", "Test Video")
        
        assert result == "/path/to/original.md"
        mock_transcriber.save_original_text.assert_called_once_with(
            "test text", "video123", "Test Video"
        )
        
    def test_run_save_translated(self, mock_transcriber):
        """测试保存翻译文本"""
        mock_transcriber.save_translated_text.return_value = "/path/to/translated.md"
        
        tool = StorageTool(mock_transcriber)
        result = tool._run("测试文本", "translated", "video123", "Test Video")
        
        assert result == "/path/to/translated.md"
        mock_transcriber.save_translated_text.assert_called_once_with(
            "测试文本", "video123", "Test Video"
        )
        
    def test_run_invalid_type(self, mock_transcriber):
        """测试无效的文件类型"""
        tool = StorageTool(mock_transcriber)
        with pytest.raises(ValueError) as exc_info:
            tool._run("test text", "invalid", "video123", "Test Video")
        assert "不支持的文件类型" in str(exc_info.value)

def test_tool_integration(mock_transcriber):
    """测试工具链集成"""
    # 设置所有必要的 mock 返回值
    mock_transcriber.download_video.return_value = ("video123", "Test Video", "test.mp3")
    mock_transcriber.extract_audio.return_value = "test.wav"
    mock_transcriber.upload_audio.return_value = "http://test.com/audio.wav"
    mock_transcriber.recognize_speech.return_value = {"results": [{"text": "test text"}]}
    mock_transcriber.extract_text_from_result.return_value = [("test text", 0, 10)]
    mock_transcriber.format_segments.return_value = "Test text with timestamp"
    mock_transcriber.translate_text.return_value = "测试文本"
    mock_transcriber.save_translated_text.return_value = "/path/to/translated.md"
    
    # 创建工具实例
    video_tool = VideoProcessingTool(mock_transcriber)
    transcription_tool = TranscriptionTool(mock_transcriber)
    translation_tool = TranslationTool(mock_transcriber)
    storage_tool = StorageTool(mock_transcriber)
    
    # 执行完整的处理流程
    video_result = video_tool._run("https://youtube.com/test")
    transcription_result = transcription_tool._run(video_result["audio_path"])
    translation_result = translation_tool._run(transcription_result)
    storage_result = storage_tool._run(
        translation_result,
        "translated",
        video_result["video_id"],
        video_result["video_title"]
    )
    
    # 验证结果
    assert video_result["video_id"] == "video123"
    assert transcription_result == "Test text with timestamp"
    assert translation_result == "测试文本"
    assert storage_result == "/path/to/translated.md" 