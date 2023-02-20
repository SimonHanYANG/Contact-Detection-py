'''
Author: Simon Yang SimonYang223@163.com
Date: 2023-02-20 14:27:31
LastEditors: Simon Yang SimonYang223@163.com
LastEditTime: 2023-02-20 19:02:09
FilePath: \Contact-Detection-py\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2 as cv
import methods

def contactDetection(img):
    m_pipette_ROI = methods.findPipetteROI(img)


def main():
    img = cv.imread('crop.jpg', 0)
    contactDetection(img)

if __name__ == "__main__":
    main()
