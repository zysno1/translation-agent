import pdfplumber
import dashscope
import html
import logging
from typing import List
from dashscope import Generation

class PDFTranslator:
    """PDF翻译器类"""
    
    def __init__(self, api_key: str):
        # 设置 API key
        dashscope.api_key = api_key
        self.keep_format = True
        self.split_paragraphs = True
        self.logger = logging.getLogger(__name__)
        
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """从PDF中提取文本"""
        self.logger.info(f"开始提取PDF文本：{pdf_path}")
        text_content = []
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages, 1):
                    self.logger.info(f"正在处理第 {i} 页")
                    text = page.extract_text()
                    if text:
                        text_content.append(text)
        except Exception as e:
            self.logger.error(f"PDF文本提取失败: {str(e)}", exc_info=True)
            raise Exception(f"PDF文本提取失败: {str(e)}")
            
        return '\n'.join(text_content)
    
    def translate_text(self, text: str) -> str:
        """使用阿里云 Qwen API 翻译文本"""
        try:
            self.logger.info("开始翻译文本")
            
            if self.split_paragraphs:
                paragraphs = text.split('\n\n')
                self.logger.info(f"文本已分割为 {len(paragraphs)} 个段落")
                translated_parts = []
                
                for i, para in enumerate(paragraphs, 1):
                    if not para.strip():
                        continue
                        
                    self.logger.info(f"正在翻译第 {i}/{len(paragraphs)} 个段落")
                    
                    # 构建提示词
                    messages = [{
                        'role': 'system',
                        'content': '你是一个专业的翻译助手，请将英文准确翻译成中文。'
                    }, {
                        'role': 'user',
                        'content': f'请翻译以下英文：\n{para}'
                    }]
                    
                    # 调用 API
                    response = Generation.call(
                        model='qwen-max',  # 或 'qwen-plus', 'qwen-turbo'
                        messages=messages,
                        result_format='message',  # 返���格式
                        temperature=0.3,  # 降低随机性
                        top_p=0.8,
                        max_tokens=1500,
                        stream=False
                    )
                    
                    if response.status_code == 200:
                        translated = response.output.choices[0]['message']['content']
                        if self.keep_format:
                            translated_parts.append(f"{para}\n{translated}")
                        else:
                            translated_parts.append(translated)
                    else:
                        raise Exception(f"API调用失败: {response.code} - {response.message}")
                        
                return '\n\n'.join(translated_parts)
            else:
                messages = [{
                    'role': 'system',
                    'content': '你是一个专业的翻译助手，请将英文准确翻译成中文。'
                }, {
                    'role': 'user',
                    'content': f'请翻译以下英文：\n{text}'
                }]
                
                response = Generation.call(
                    model='qwen-max',
                    messages=messages,
                    result_format='message',
                    temperature=0.3,
                    top_p=0.8,
                    max_tokens=1500,
                    stream=False
                )
                
                if response.status_code == 200:
                    return response.output.choices[0]['message']['content']
                else:
                    raise Exception(f"API调用失败: {response.code} - {response.message}")
                
        except Exception as e:
            self.logger.error(f"翻译失败: {str(e)}", exc_info=True)
            raise Exception(f"翻译失败: {str(e)}")
    
    def translate_pdf(self, pdf_path: str, output_path: str):
        """翻译PDF文件并保存结果"""
        try:
            self.logger.info(f"开始处理PDF文件：{pdf_path}")
            
            # 提取文本
            text = self.extract_text_from_pdf(pdf_path)
            
            # 翻译文本
            self.logger.info("开始翻译提取的文本")
            translated_text = self.translate_text(text)
            
            # 生成HTML输出
            self.logger.info("生成HTML输出")
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {{ 
                        font-family: Arial, sans-serif; 
                        line-height: 1.6; 
                        margin: 40px; 
                        max-width: 1200px;
                        margin: 0 auto;
                        padding: 20px;
                        background-color: #f5f5f5;
                    }}
                    .paragraph-block {{ 
                        background-color: white;
                        margin-bottom: 20px;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }}
                    .original {{ 
                        color: #2c3e50;
                        margin-bottom: 15px;
                        padding-bottom: 15px;
                        border-bottom: 1px solid #eee;
                    }}
                    .translated {{ 
                        color: #34495e;
                    }}
                    .title {{
                        font-weight: bold;
                        color: #7f8c8d;
                        margin-bottom: 5px;
                        font-size: 0.9em;
                    }}
                    .copy-btn {{
                        float: right;
                        padding: 5px 10px;
                        background-color: #3498db;
                        color: white;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                    }}
                    .copy-btn:hover {{
                        background-color: #2980b9;
                    }}
                </style>
                <script>
                    function copyText(type, blockId) {{
                        const block = document.getElementById(blockId);
                        const text = block.querySelector(type === 'original' ? '.original' : '.translated').textContent;
                        navigator.clipboard.writeText(text).then(() => {{
                            alert('已复制到剪贴板');
                        }});
                    }}
                </script>
            </head>
            <body>
            """
            
            # 分段处理文本
            original_paragraphs = text.split('\n\n')
            translated_paragraphs = translated_text.split('\n\n')
            
            # 确保两个列表长度相同
            min_len = min(len(original_paragraphs), len(translated_paragraphs))
            
            # 逐段生成对照显示的HTML
            for i in range(min_len):
                if original_paragraphs[i].strip() and translated_paragraphs[i].strip():
                    html_content += f"""
                    <div class="paragraph-block" id="block-{i}">
                        <div class="original">
                            <div class="title">
                                原文
                                <button class="copy-btn" onclick="copyText('original', 'block-{i}')">复制原文</button>
                            </div>
                            {html.escape(original_paragraphs[i])}
                        </div>
                        <div class="translated">
                            <div class="title">
                                译文
                                <button class="copy-btn" onclick="copyText('translated', 'block-{i}')">复制译文</button>
                            </div>
                            {html.escape(translated_paragraphs[i])}
                        </div>
                    </div>
                    """
            
            html_content += """
            </body>
            </html>
            """
            
            # 保存结果
            self.logger.info(f"保存翻译结果到：{output_path}")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
                
            self.logger.info("PDF翻译完成")
                
        except Exception as e:
            self.logger.error(f"PDF翻译失败: {str(e)}", exc_info=True)
            raise Exception(f"PDF翻译失败: {str(e)}") 