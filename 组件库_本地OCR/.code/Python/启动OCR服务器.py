#-*- coding:utf-8 -*-
from flask import Flask,request
from paddleocr import PaddleOCR
import json
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ocr", methods=["POST"])
def ocr():
    # print("Start OCR.")
    imgPath=json.loads(request.get_data())["imgPath"]
    print("imgPath="+imgPath)
    result = PPobject.ocr(imgPath)
    return json.dumps(result, ensure_ascii=False)

if __name__ == "__main__":
    language=sys.argv[1]
    print("====Creat model start.====")
    PPobject = PaddleOCR(use_angle_cls=True, lang=language,
                         show_log=False, enable_mkldnn=True)
    print("====Creat model done.====")
    # print(PPobject)
    app.run(debug=False)
    print("====app run====")
    print("====END====")
