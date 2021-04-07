# Created By Jacky on 2021/4/7


# 列主元消去法
# 每次都把最大的主元放在第一行



import numpy as np
from NumericalAnalysis_Courses.Gaussian_Elimination import Gaussian_Function

def Eliminate_Pivot(A,b):
    n = len(b)
    aux = np.zeros((1,n))               # 辅助向量

    for i in range(1,n):
        max = abs(A[i,i])
        m = i                           # 记录最大的行
        for j in range(i+1,n):
            if max < np.abs(A[j , i]):
                max = np.abs(A[j , i])
                m = j
        if(m != i):                     # 遇到不等的时候即要交换行的时候
            for k in range(i , n):
                aux[k] = A[i , k]
                A[i , k] = A[m , k]
                A[m , k] = aux[k]
            temp = b[i]
            b[i] = b[m]
            b[m] = temp

def Gauss_Lie(A , b):
    Eliminate_Pivot(A , b)                # 先排列主元
    Gaussian_Function.gauss(A , b)        # 然后再高斯消元