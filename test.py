'''
Author: Simon Yang SimonYang223@163.com
Date: 2023-02-20 17:11:27
LastEditors: Simon Yang SimonYang223@163.com
LastEditTime: 2023-02-20 17:13:38
FilePath: \Contact-Detection-py\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2

bgr_img = cv2.imread("test.jpg")
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
th, binary = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(bgr_img, contours, -1, (0, 0, 255), 3)
 
bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]
 
for bbox in bounding_boxes:
     [x , y, w, h] = bbox
     cv2.rectangle(bgr_img, (x, y), (x + w, y + h), (255, 255, 0), 2)
 
cv2.imshow("name", bgr_img)
cv2.waitKey(0)