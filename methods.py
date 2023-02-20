'''
Author: Simon Yang SimonYang223@163.com
Date: 2023-02-20 14:24:40
LastEditors: Simon Yang SimonYang223@163.com
LastEditTime: 2023-02-20 18:33:31
FilePath: \Contact-Detection-py\methods.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import numpy as np

def findPipetteROI(img):
    m_img_size = img.shape
    img_binarized = np.zeros(m_img_size, np.uint8)
    g_gray = np.zeros(m_img_size, np.uint8)

    m_threshold = (int)(img.mean())

    ret, img_binarized = cv2.threshold(img, m_threshold * 0.75, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("img_binarized", img_binarized)

    contours, hierarchy = cv2.findContours(img_binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    # cv2.imshow("img", img)
    
    bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]

    for bbox in bounding_boxes:
        [x , y, w, h] = bbox
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 8)
        print("x: {}".format(x))
        
    cv2.imshow("Micropipette Contours", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return bounding_boxes