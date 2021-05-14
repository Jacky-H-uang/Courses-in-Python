# Created By Jacky on 2021/5/12

import numpy as np
import matplotlib.pyplot as plt
import math

# 精度函数
def accurency(a,b,k):
    n = round(k / math.log(2,10))
    error = (b-a)/(2**(n+1))
    return error


# 二分法
def binary(f,a,b,error):
    fa = f(a)
    fb = f(b)
    cnt = 1
    xc = []
    yc = []
    while (b-a) / 2 > error:
        c = (a + b) / 2
        print("第",cnt,"次迭代的估计点 : " ,c)
        cnt += 1
        fc = f(c)
        xc.append(c)
        yc.append(fc)
        if fc == 0:
            break
        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    x = (a+b)/2

    print("最优估计的点 : " , x)

    return xc ,yc , x , f(x)


# 求解的函数
def f(x):
    return np.cos(x) - x


# 绘制图像
def plotter(fuc,a,b,k,xc,yc,_x,_y):
    plt.figure()
    plt.xlabel('X')
    plt.ylabel('Y')

    x = np.linspace(a, b, k)         # 从 0 到 1 ，等分50分
    y = [fuc(t) for t in x]

    plt.plot(x, y,c='g')
    plt.plot(x,[0] * k,c = 'gold')
    plt.scatter(xc , yc , edgecolors = 'red',c='red',marker='x')
    plt.scatter(_x,_y,c = 'blue',marker='s')

    plt.grid()
    plt.show()

if __name__ == '__main__':
    a = 0
    b = 1
    acc = accurency(a,b,6)
    xc , yc , x , y = binary(f,a,b,error = acc)
    plotter(f,a,b,50,xc,yc,x,y)