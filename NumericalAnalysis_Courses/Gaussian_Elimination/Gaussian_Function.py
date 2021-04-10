# Created By Jacky on 2021/4/7

# 高斯消元法算法
# Input : 系数矩阵 A 和 b 矩阵
# Output: 结果矩阵 x


import numpy as np


def gauss(A,b):
    n = len(b)
    x = np.zeros((n,1))

    # 消元
    for i in range(n):
        for k in range(i + 1 , n):
            for j in range(i + 1 , n):
                A[k,j] = A[k,j] + A[i,j] * (-A[k,i] / A[i , i])
            b[k] = b[k] + b[i] * (-A[k,i] / A[i , i])
            A[k,i] = 0

    # 回代计算
    x[n-1] = b[n-1] / A[n-1 , n-1]
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1 , n):
            sum = sum + A[i , j] * x[j]
        x[i] = (b[i] - sum) / A[i , i]

    print("消元后的矩阵 A : \n" , A)
    print("\n消元后的矩阵 b : \n" , b)
    print("\n解得 X ：")
    print(x)

    return x