#-*- coding:utf-8 -*-

import cv2
import numpy as np
import sys

if __name__ == "__main__":
    背景文件路径=sys.argv[1]
    滑块文件路径=sys.argv[2]

block = cv2.imread(滑块文件路径, 0)
template = cv2.imread(背景文件路径, 0)
# print(block)
# print(template)

# 二值化后的图片名称
blockName = "block.png"
templateName = "template.jpeg"
# 裁剪掉滑块的多余边缘将二值化后的图片进行保存
# cv2.imwrite(blockName, block[5:63,5:63])
cv2.imwrite(blockName, block)
cv2.imwrite(templateName, template)
block = cv2.imread(blockName)
block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
block = abs(255 - block)
""" 将小图反色，大图不变 """
cv2.imwrite(blockName, block)
block = cv2.imread(blockName)
template = cv2.imread(templateName)
# 获取偏移量
result = cv2.matchTemplate(block, template,cv2.TM_CCOEFF_NORMED)  # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
# print(result)
# numpy.unravel_index()函数的作用是获取一个/组int类型的索引值在一个多维数组中的位置。

y, x = np.unravel_index(result.argmax(), result.shape)
滑块偏移值 = int(x*(342/552))
print("x方向的偏移折算后=",滑块偏移值 , "x=", x, "y=", y)
