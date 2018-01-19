# -*- coding:utf-8 -*-

#引入机器学习模块
import pytesseract
#引入图形处理模块
from PIL import Image

#引入一张图片
img = Image.open('dd.png')

#识别图片
# text = pytesseract.image_to_string(img)
# tessdata_dir_config = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
text = pytesseract.image_to_string(img, config=tessdata_dir_config)

print text