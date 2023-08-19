#-*- coding:utf-8 -*-
import sys
import PaddleOCR.ocr_paddle


if __name__ == "__main__":
    imagePath=sys.argv[1]
    language=sys.argv[2]
    resultText=""

resultText=PaddleOCR.ocr_paddle.recognize(imagePath,language)
