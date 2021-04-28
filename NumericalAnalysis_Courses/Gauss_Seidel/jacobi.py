# Created By Jacky on 2021/4/28

import numpy as np

def jacobi_iteration(A,b,k,error):
    n = len(A)
    Aux = A
    x = np.zeros(n)
    for time in range(k):               # 迭代 k 次
        # 保存单次迭代后的值
        x_single = np.zeros(n)
        for i in range(n):
            cur = 0.0
            for j in range(n):
                if i == j:  continue
                cur += (-Aux[i,j]) * x[j]
            x_single[i] = (cur + b[i,0]) / Aux[i,i]
        print("迭代第 " + str(time+1) + " 次得到 x: ")
        print(x_single)

        error_x = 0.0           # 保存迭代的最大的误差
        for p in range(n):
            error_x = max(abs(x[p]-x_single[p]),error_x)
        x = x_single
        if error_x < error:
            break

    print("\n最终收敛的结果 : ")
    print(x)


if __name__ == '__main__':
    A = np.mat([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
    b = np.mat([6,25,-11,15]).T

    # 误差选其 10^-7 小于这个 error 或者迭代一百次时跳出循环
    jacobi_iteration(A,b,100,0.00000001)
