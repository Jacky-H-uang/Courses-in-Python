# Created By Jacky on 2021/4/28


import numpy as np

def gauss_seidel(A,b):
    n = len(A)
    Aux = A             # 辅助矩阵
    x = np.zeros(n)
    for k in range(10):
        for i in range(n):
            cur = 0.0
            for j in range(n):
                if i == j:  continue
                cur += (-Aux[i,j]) * x[j]
            x[i] = (cur + b[i,0]) / Aux[i,i]
        print("迭代第 " + str(k+1) + " 次得到 x: ")
        print(x)

    print("\n最终收敛的结果 : ")
    print(x)


if __name__ == '__main__':
    A = np.mat([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
    b = np.mat([6,25,-11,15]).T
    gauss_seidel(A,b)
