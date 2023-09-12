#-*- coding:utf-8 -*-
import sys
import json
import requests

if __name__ == "__main__":
    imagePath=sys.argv[1]
    language=sys.argv[2]
    resultText=""

r = requests.post("http://127.0.0.1:5000/ocr", headers={
    "Content-Type": "application/json"},data=json.dumps({"imgPath": imagePath,"language": language}))
tempArray = []
for line in json.loads(r.text)[0]:
    tempArray.append(line[1][0])
print("----Recognized result array----")
print(tempArray)
resultText=json.dumps(tempArray,ensure_ascii=True)