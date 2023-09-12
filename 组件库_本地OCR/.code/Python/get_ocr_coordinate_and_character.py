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
for textBlock in json.loads(r.text)[0]:
    print(textBlock)
    strText=textBlock[1][0]
    arrayTopLeft = [int(textBlock[0][0][0]),int(textBlock[0][0][1])]
    arrayBottomRight = [int(textBlock[0][2][0]),int(textBlock[0][2][1])]
    # print(arrayTopLeft)
    # print(arrayBottomRight)
    """ determine text alignment direction"""
    width = arrayBottomRight[0]-arrayTopLeft[0]
    height = arrayBottomRight[1]-arrayTopLeft[1]
    # print(width,height)
    if width>=height:
        print("text alignment direction: horizontal")
        for index, char in enumerate(strText):
            print(f"index:{index}, character:'{char}'")
            arrarCharTopLeft=[int(textBlock[0][0][0])+int(width/ len(strText) *index),int(textBlock[0][0][1])]
            print(arrarCharTopLeft)
            tempArray.append({"coordinate":arrarCharTopLeft,"text":[char]})
    else :
        print("text alignment direction: vertical")
        for index, char in enumerate(strText):
            print(f"index:{index}, character:'{char}'")
            arrarCharTopLeft=[int(textBlock[0][0][0]),int(textBlock[0][0][1]+int(height/ len(strText) *index))]
            print(arrarCharTopLeft)
            tempArray.append({"coordinate":arrarCharTopLeft,"text":[char]})
print("----Recognized result array----")
print(tempArray)
outStrOCRResultJSON=json.dumps(tempArray,ensure_ascii=True)