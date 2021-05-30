# Created By Jacky on 2021/5/26


import numpy as np
import matplotlib.pyplot as plt
from NumericalAnalysis_Courses.Gaussian_Elimination.Gaussian_Function import gauss

# 解方程组来求插值多项式
def interpolation(x,y):
    l = len(x)
    A = np.zeros((l,l))
    # 生成矩阵
    for i in range(l):
        aux = np.power(x,i)
        A[:,i] = aux

    ans = gauss(A,y)
    x = [0] * len(ans)

    for i in range(len(ans)):
        x[i] = ans[len(ans)-i-1,0]

    f = np.poly1d(x)

    return f



def plotter(x,y,f,a,b,k):
    plt.figure()
    plt.xlabel("X-")
    plt.ylabel("Y-")
    plt.scatter(x,y,marker='x',c='red')

    x_ = np.linspace(a,b,k)
    y_ = [f(_) for _ in x_]
    plt.plot(x_,y_ ,c='g')

    plt.grid()
    plt.show()


if __name__ == '__main__':
    x1 = np.array([-1,1,2,5])
    y1 = np.array([-7,7,-4,35])
    f = interpolation(x1,y1)
    plotter(x1,y1,f,a = -10,b = 10,k = 100)
    print("[x,y] = [{} , {}]".format(-1,-7))
    print("f(-1) = " , f(-1))

    x2 = np.array([0,np.pi/6,np.pi/4,np.pi/3,np.pi/2])
    y2 = np.array([np.sin(_) for _ in x2])
    f = interpolation(x2,y2)
    print("sin(π/12) = ",np.sin(np.pi/12))
    print("f(π/12) = " , f(np.pi/12))
    plotter(x2,y2,f,a = -10,b = 10,k = 100)