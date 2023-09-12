#-*- coding:utf-8 -*-
import sys
import json
import requests

if __name__ == "__main__":
    inStrImagePath=sys.argv[1]
    inStrlanguage=sys.argv[2]

r = requests.post("http://127.0.0.1:5000/ocr", headers={
    "Content-Type": "application/json"},data=json.dumps({"imgPath": inStrImagePath,"language": inStrlanguage}))
# print(r)
tempArray = []
for arrayElement in json.loads(r.text)[0]:
    print(arrayElement)
    arrayTopLeft=[str(int(arrayElement[0][0][0])),str(int(arrayElement[0][0][1]))]
    print("arrayTopLeft="+str(arrayTopLeft))
    strText=arrayElement[1][0]
    print("strText="+strText)
    tempArray.append({"coordinate":arrayTopLeft,"text":[strText]})
print("----Recognized result array----")
print(tempArray)
outStrOCRResultJSON=json.dumps(tempArray,ensure_ascii=True)