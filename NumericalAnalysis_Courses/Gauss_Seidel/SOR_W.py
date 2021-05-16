# Created By Jacky on 2021/5/16

from NumericalAnalysis_Courses.Gauss_Seidel.SOR import sor_function
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def plotter(cnt,w):
    plt.figure()
    plt.xlabel('X : 松弛参数0.5~1.5')
    plt.ylabel('Y : 迭代次数')

    plt.scatter(w ,cnt , edgecolors = 'red',c='red',marker='x')

    plt.grid()
    plt.show()


if __name__ == '__main__':
    k = 1000                 # 迭代 1000 次
    error = 0.000001        # 误差 0.000001

    A = np.mat([[3,-1,0,0,0,0.5],[-1,3,-1,0,0.5,0],[0,-1,3,-1,0,0],[0,0,-1,3,-1,0],[0,0.5,0,-1,3,-1],[0.5,0,0,0,-1,3]])
    b = np.mat([2.5,1.5,1,1,1.5,2.5]).T


    w = []
    wc = 0.5
    cnt = []
    for i in range(20):
        w.append(wc)
        c , xc = sor_function(A,b,wc,k,error)
        wc += 0.05
        cnt.append(c)

    plotter(cnt,w)