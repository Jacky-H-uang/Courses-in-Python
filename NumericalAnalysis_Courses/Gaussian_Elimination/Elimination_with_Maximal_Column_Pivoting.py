# Created By Jacky on 2021/4/7


# 列主消元法算法 (每一个把最大的主元放在前面)
# Input: 系数矩阵 A 和 b 矩阵
# Output: 结果矩阵 x



import numpy as np
from NumericalAnalysis_Courses.Gaussian_Elimination import Gaussian_Function

def Eliminate_Pivot(A,b):
    n = len(b)
    aux = np.zeros((1,n))               # 辅助向量
    x = np.zeros((n,1))

    for i in range(n):
        max = np.abs(A[i,i])
        m = i                           # 记录最大的行
        for j in range(i+1,n):
            if max < np.abs(A[j , i]):
                max = np.abs(A[j , i])
                m = j
        if(m != i):                     # 遇到不等的时候即要交换行的时候
            for k in range(i , n):
                aux[i,k] = A[i , k]
                A[i , k] = A[m , k]
                A[m , k] = aux[i,k]
            temp = b[i,0]
            b[i,0] = b[m,0]
            b[m,0] = temp
        for k in range(i+1,n):
            for j in range(i+1,n):
                A[k,j] = A[k,j] + A[i,j] * (-A[k,i]/A[i,i])
            b[k] = b[k] + b[i] * (-A[k,i] / A[i,i])
            A[k,i] = 0

    print("消元后的A：\n")
    print(A)
    print("消元后的b：\n")
    print(b)

    x[n-1] = b[n-1] / A[n-1,n-1]
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += A[i,j]*x[j]
        x[i] = (b[i]-sum) / A[i,i]

    print("解得 X : \n")
    print(x)

    return x