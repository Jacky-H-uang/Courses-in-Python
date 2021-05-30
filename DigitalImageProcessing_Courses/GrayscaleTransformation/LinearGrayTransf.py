# Created By Jacky on 2021/5/27


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import copy

# 线性灰度变换
def linear(img,a,b,c,d):
    alpha = (d - c) / (b-a)
    beta = c - alpha*(-1 * a)
    rows , cols = img.shape[0] , img.shape[1]
    for i in range(rows):
        for j in range(cols):
            p = alpha * img[i,j] + beta

            # 判断这点的像素灰度是否符合标准
            if p[0] > 255 : p[0] = 255
            elif p[0] < 0 : p[0] = 0
            if p[1] > 255 : p[1] = 255
            elif p[1] < 0 : p[1] = 0
            if p[2] > 255 : p[2] = 255
            elif p[2] < 0 : p[2] = 0
            img[i,j] = p

    return img



if __name__ == '__main__':
    img = cv.imread("../Images/test3.jpg")
    X = input("输入初始的灰度范围 ： ").split(' ')
    Y = input("输入变换的灰度范围 ： ").split(' ')

    a = int(X[0])
    b = int(X[1])
    c = int(Y[0])
    d = int(Y[1])

    cv.imshow("Original: ",img)
    out_img = linear(img,a , b , c , d)

    cv.imshow("After GrayTransformation : ",out_img)
    cv.waitKey(0)
    cv.destroyAllWindows()