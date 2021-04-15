# Created By Jacky on 2021/4/14

# LU分解算法 (将系数矩阵A分解为上三角矩阵 L 和下三角矩阵 U 其中 A = LU)
# Input: 系数矩阵 A 和 b 矩阵
# Output: 结果矩阵 x


import numpy as np

def LU_D(A):
    n = len(A)
    L = np.eye(n)
    U = A
    for i in range(n):
        for k in range(i+1,n):
            for j in range(i+1,n):
                fac = -U[k,i] / U[i,i]
                U[k,j] = U[k,j] + U[i,j] * fac
            aux = np.eye(n)
            aux[k,i] = aux[k,i] - aux[i,i] * fac
            L = np.dot(L,aux)
            U[k,i] = 0

    return L ,U         # 返回 矩阵 L 和 U

def LU(A,b):
    n = len(b)
    L , U = LU_D(A)

    print("L矩阵 : \n" , L  , "\n")
    print("U矩阵 : \n" , U , "\n")

    # 求解 Lc = b
    c = np.zeros((n,1))
    c[0] = b[0]
    for i in range(1,n):
        sum = 0
        for j in range(0,n-1):
            sum += L[i,j] * c[j]
        c[i] = (b[i]-sum)

    # 求解 Ux = c
    x = np.zeros((n,1))
    x[n-1] = c[n-1] / U[n-1,n-1]
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += U[i,j] * x[j]
        x[i] = (c[i]-sum) / U[i,i]

    return x