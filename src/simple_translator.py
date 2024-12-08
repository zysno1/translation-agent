import gradio as gr
from pdf_translator import PDFTranslator
import logging
import os
from dotenv import load_dotenv

def create_translator_interface():
    # 加载环境变量
    load_dotenv()
    api_key = os.getenv('DASHSCOPE_API_KEY')
    
    if not api_key:
        raise ValueError("请设置 DASHSCOPE_API_KEY 环境变量")
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    
    # 初始化翻译器
    translator = PDFTranslator(api_key)
    
    def translate_file(file, keep_format, split_paragraphs):
        try:
            if file is None:
                logger.warning("未上传文件")
                return "请上传PDF文件"
            
            logger.info(f"收到文件：{file.name}")
            
            # 设置翻译选项
            translator.keep_format = keep_format
            translator.split_paragraphs = split_paragraphs
            
            # 执行翻译
            output_path = f"{file.name}_translated.html"
            translator.translate_pdf(file.name, output_path)
            
            # 读取结果
            with open(output_path, 'r', encoding='utf-8') as f:
                result = f.read()
            
            return result
            
        except Exception as e:
            logger.error(f"翻译出错：{str(e)}", exc_info=True)
            return f"翻译出错：{str(e)}"
    
    # 创建界面
    interface = gr.Interface(
        fn=translate_file,
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Checkbox(label="保持原格式", value=True),
            gr.Checkbox(label="按段落分割", value=True)
        ],
        outputs=gr.HTML(label="翻译��果"),
        title="PDF翻译助手",
        description="上传英文PDF文件，获取中英文对照翻译结果"
    )
    
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )

if __name__ == "__main__":
    create_translator_interface() 