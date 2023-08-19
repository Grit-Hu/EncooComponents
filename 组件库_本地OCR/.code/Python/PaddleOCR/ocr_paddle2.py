from paddleocr import PaddleOCR
import json

def recognize(img_path,language):
    result = PaddleOCR(use_angle_cls=True, lang=language,
                       show_log=False,drop_score=0.2).ocr(img_path, cls=True)
    tempArray = []
    # print("----列表识别结果----")
    for line in result:
        # print(line)
        tempArray.append(line[1][0])
    print("----识别结果数组----")
    print(tempArray)

    return json.dumps(tempArray,ensure_ascii=True)
