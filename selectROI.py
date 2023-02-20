# -*- coding: utf-8 -*-
# @Author  : Simon
# @Time    : 2023/2/21 19:00
# @Function: 从图片中选出某一区域，Enter保存

import cv2

# 读取图片
img = 'test.jpg'
img = cv2.imread(img)
cv2.imshow('original', img)

# 选择ROI
roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
print(roi)

# 显示ROI并保存图片
if roi != (0, 0, 0, 0):
    crop = img[y:y+h, x:x+w]
    cv2.imshow('crop', crop)
    cv2.imwrite('crop.jpg', crop)
    print('Saved!')

# 退出
cv2.waitKey(0)
cv2.destroyAllWindows()
