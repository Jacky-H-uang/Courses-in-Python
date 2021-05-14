# Created By Jacky on 2021/5/14

import numpy as np
import math
import matplotlib.pyplot as plt

# 简单迭代法
def simple_iter(g,x0,k):
    x = np.zeros(k+1)
    x[0] = x0
    print("不动点迭代开始 : ")
    for i in range(k):
        print("x",i," = " , x[i])
        x[i+1] = g(x[i])
    x_c = x[k]
    print(x_c)
    return x


def g(x):
    f = np.poly1d([-2,1,3])
    return f(x)**(1/4)


def plotter(fuc,x,y,a,b,k):
    plt.figure()
    plt.xlabel('X')
    plt.ylabel('Y')

    x_ = np.linspace(a, b, k)         # 从 0 到 1 ，等分50分
    y_ = [fuc(t) for t in x_]

    plt.plot(x_, y_,c='g')
    plt.plot(x_,x_,c = 'gold')
    plt.scatter(x , y , edgecolors = 'red',c='red',marker='x')
    plt.scatter(x[-1],y[-1],c = 'blue',marker='s')

    plt.grid()
    plt.show()

if __name__ == '__main__':
    x = simple_iter(g,1,27)
    y = [g(_x) for _x in x]
    plotter(g,x,y,a = 0,b = 1.5, k = 50)
