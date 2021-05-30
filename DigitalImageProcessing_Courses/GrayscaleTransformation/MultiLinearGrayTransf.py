# Created By Jacky on 2021/5/28

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# 分段灰度线性变换

def multi_linear(img,a,b,c,d,L = 256):
    height , width = img.shape[0] , img.shape[1]

    out_img = np.zeros((height,width),np.uint8)
    # 一般来分三段处理
    for i in range(height):
        for j in range(width):
            # 第一段处理
            if img[i,j] > 0 and img[i,j] < a:
                out_img[i,j] = np.round((c/a) * img[i,j])

            # 第二段处理
            elif img[i,j] >= a and img[i,j] < b:
                out_img[i,j] = np.round((d-c)/(b-a) * (img[i,j] - a) + c)

                # 第三段处理
            elif img[i,j] >= b and img[i,j] < L:
                out_img[i,j] = np.round((L-1-d)/(L-1-b) * (img[i,j] - b) + d)


    return out_img



if __name__ == '__main__':
    img = cv.imread('../Images/test3.jpg')
    cv.imshow('Original-Img',img)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    out_img = multi_linear(img,a = 30,b = 100 , c = 30 , d = 200)
    cv.imshow('Result-Img',out_img)
    cv.waitKey(0)
    cv.destroyAllWindows()