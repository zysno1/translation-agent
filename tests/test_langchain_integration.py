import os
import sys
import unittest
import shutil
from datetime import datetime
from unittest.mock import patch, MagicMock

# 添加项目根目录到 Python 路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.youtube_transcriber import YouTubeTranscriber

class TestLangchainIntegration(unittest.TestCase):
    """测试 Langchain 集成的基础功能"""
    
    @classmethod
    def setUpClass(cls):
        """测试类初始化"""
        cls.test_dir = os.path.join(current_dir, "test_data")
        os.makedirs(cls.test_dir, exist_ok=True)
        cls.test_url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
        cls.transcriber = YouTubeTranscriber(debug=True)
    
    @classmethod
    def tearDownClass(cls):
        """测试类清理"""
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
    
    def setUp(self):
        """每个测试用例的初始化"""
        self.test_audio_path = os.path.join(self.test_dir, "test_audio.mp3")
        with open(self.test_audio_path, "wb") as f:
            f.write(b"test audio content")
    
    def tearDown(self):
        """每个测试用例的清理"""
        if os.path.exists(self.test_audio_path):
            os.remove(self.test_audio_path)
    
    def test_chain_initialization(self):
        """测试处理链初始化"""
        self.assertIsNotNone(self.transcriber.processing_chain)
        self.assertIsNotNone(self.transcriber.video_chain)
        self.assertIsNotNone(self.transcriber.transcription_chain)
        self.assertIsNotNone(self.transcriber.translation_chain)
    
    @patch('src.youtube_transcriber.YouTubeTranscriber.download_video')
    def test_video_transform(self, mock_download):
        """测试视频处理转换函数"""
        mock_download.return_value = ("test_id", "Test Video", self.test_audio_path)
        inputs = {"url": self.test_url}
        result = self.transcriber._video_transform(inputs)
        self.assertIsInstance(result, dict)
        self.assertIn("video_id", result)
        self.assertIn("video_title", result)
        self.assertIn("audio_path", result)
        self.assertEqual(result["video_id"], "test_id")
        self.assertEqual(result["video_title"], "Test Video")
        self.assertEqual(result["audio_path"], self.test_audio_path)
    
    @patch('src.youtube_transcriber.YouTubeTranscriber.recognize_speech')
    def test_transcription_transform(self, mock_recognize):
        """测试转写处理转换函数"""
        mock_recognize.return_value = "[00:00 - 00:05] Test transcription."
        inputs = {"audio_path": self.test_audio_path}
        result = self.transcriber._transcription_transform(inputs)
        self.assertIsInstance(result, dict)
        self.assertIn("original_text", result)
        self.assertIsNotNone(result["original_text"])
        self.assertRegex(result["original_text"], r'^\[\d{2}:\d{2} - \d{2}:\d{2}\]')
    
    @patch('src.youtube_transcriber.YouTubeTranscriber.translate_text')
    def test_translation_transform(self, mock_translate):
        """测试翻译处理转换函数"""
        test_text = "[00:00 - 00:05] This is a test sentence."
        mock_translate.return_value = "[00:00 - 00:05] 这是一个测试句子。"
        inputs = {"original_text": test_text}
        result = self.transcriber._translation_transform(inputs)
        self.assertIsInstance(result, dict)
        self.assertIn("translated_text", result)
        self.assertIsNotNone(result["translated_text"])
        self.assertRegex(result["translated_text"], r'^\[\d{2}:\d{2} - \d{2}:\d{2}\]')
    
    def test_error_handling(self):
        """测试错误处理"""
        # 测试无效的 URL
        result = self.transcriber.process_video("https://www.youtube.com/watch?v=invalid")
        self.assertFalse(result["success"])
        self.assertIn("error", result)
        
        # 测试空 URL
        result = self.transcriber.process_video("")
        self.assertFalse(result["success"])
        self.assertIn("error", result)

if __name__ == '__main__':
    unittest.main() 