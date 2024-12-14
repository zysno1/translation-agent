import logging
from fastapi import FastAPI
import gradio as gr
from pdf_translator import PDFTranslator
import asyncio
import os
from PyPDF2 import PdfReader

class PDFTranslatorAgent:
    def __init__(self):
        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
        
        self.app = FastAPI(title="PDF翻译助手")
        
        api_key = os.getenv("TRANSLATOR_API_KEY")
        if not api_key:
            raise ValueError("请设置 TRANSLATOR_API_KEY 环境变量")
            
        self.translator = PDFTranslator(api_key=api_key)
        
        # 创建 Gradio 界面
        self.interface = gr.Interface(
            fn=self.translate_file,
            inputs=[
                gr.File(label="上传PDF文件"),
                gr.Checkbox(label="保持原格式", value=True),
                gr.Checkbox(label="按段落分割", value=True)
            ],
            outputs=gr.Textbox(label="翻译结果", lines=10),
            title="PDF翻译助手",
            description="上传英文PDF文件，获取中英文对照翻译结果",
            allow_flagging="never"
        )
        
        # 将 Gradio 接口挂载到 FastAPI
        self.app = gr.mount_gradio_app(self.app, self.interface, path="/")
        
    async def translate_file(self, file, keep_format, split_paragraphs):
        try:
            if file is None:
                self.logger.warning("未上传文件")
                yield gr.update(value="请上传PDF文件")
                return
            
            self.logger.info(f"收到文件：{file.name}")
            
            # 创建临时进度显示
            progress_html = gr.update(value="<div>正在处理文件...</div>")
            yield progress_html
            
            # 设置翻译选项
            self.translator.keep_format = keep_format
            self.translator.split_paragraphs = split_paragraphs
            
            # 获取所有文本块
            chunks = await self._get_text_chunks(file.name)
            total_chunks = len(chunks)
            
            # 创建所有翻译任务
            tasks = []
            
            for chunk in chunks:
                task = asyncio.create_task(self._translate_chunk(chunk))
                tasks.append(task)
            
            # 等待所有任务完成
            completed_translations = await asyncio.gather(*tasks)
            
            # 生成最终的HTML结果
            output_html = "<div>翻译完成</div>"  # 直接返回一个简单的结果
            
            self.logger.info("翻译完成")
            
            yield gr.update(value=output_html)
            
        except Exception as e:
            self.logger.error(f"翻译过程出错：{str(e)}", exc_info=True)
            yield gr.update(value=f"<div class='error'>翻译出错：{str(e)}</div>")
    
    async def _translate_chunk(self, chunk):
        """翻译单个文本块并保持原始顺序"""
        # 如果 translate_text 是同步函数，使用 run_in_executor
        loop = asyncio.get_event_loop()
        translated_text = await loop.run_in_executor(None, self.translator.translate_text, chunk)
        return translated_text
    
    def _generate_html_output(self, translated_text):
        """生成格式化的HTML输出"""
        html_template = """
        <div class="translation-result">
            <style>
                .translation-result {
                    padding: 20px;
                    line-height: 1.6;
                    background-color: #f5f5f5;
                    border-radius: 8px;
                }
                .paragraph {
                    margin-bottom: 20px;
                    padding: 15px;
                    background-color: white;
                    border-radius: 5px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .original {
                    color: #2c3e50;
                    margin-bottom: 10px;
                    padding: 10px;
                    background-color: #ecf0f1;
                    border-radius: 4px;
                    font-family: 'Source Code Pro', monospace;
                }
                .translated {
                    color: #27ae60;
                    font-weight: 500;
                    padding: 10px;
                    border-left: 4px solid #27ae60;
                }
                .section-title {
                    font-weight: bold;
                    color: #7f8c8d;
                    font-size: 0.9em;
                    margin-bottom: 5px;
                }
            </style>
            {content}
        </div>
        """
        
        formatted_content = self._format_translation_content(translated_text)
        
        # 打印调试信息
        print(f"Formatted Content: {repr(formatted_content)}")  # 使用 repr() 查看原始字符串
        
        # 确保 formatted_content 是有效的字符串
        if not formatted_content.strip():
            formatted_content = "<div>没有可显示的翻译内容。</div>"
        
        try:
            return html_template.format(content=formatted_content)
        except KeyError as e:
            print(f"KeyError: {e}")
            print(f"HTML Template: {html_template}")
            print(f"Formatted Content: {formatted_content}")
            raise
    
    def _format_translation_content(self, text):
        """直接返回空字符串，去掉翻译内容的格式化"""
        return ""  # 或者直接删除这个方法
    
    async def _get_text_chunks(self, file_name):
        """从 PDF 文件中提取文本块"""
        text_chunks = []
        try:
            with open(file_name, "rb") as file:
                reader = PdfReader(file)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        text_chunks.extend(text.split('\n\n'))  # 按段落分割
        except Exception as e:
            self.logger.error(f"读取 PDF 文件出错：{str(e)}", exc_info=True)
            raise
        
        return text_chunks
    
    def run(self, host="0.0.0.0", port=7860):
        """运行服务"""
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)

def main():
    agent = PDFTranslatorAgent()
    agent.run()

if __name__ == "__main__":
    main() 