# Created By Jacky on 2021/4/7


# ����Ԫ��ȥ��
# ÿ�ζ���������Ԫ���ڵ�һ��



import numpy as np
from NumericalAnalysis_Courses.Gaussian_Elimination import Gaussian_Function

def Eliminate_Pivot(A,b):
    n = len(b)
    aux = np.zeros((1,n))               # ��������

    for i in range(1,n):
        max = abs(A[i,i])
        m = i                           # ��¼������
        for j in range(i+1,n):
            if max < np.abs(A[j , i]):
                max = np.abs(A[j , i])
                m = j
        if(m != i):                     # �������ȵ�ʱ��Ҫ�����е�ʱ��
            for k in range(i , n):
                aux[k] = A[i , k]
                A[i , k] = A[m , k]
                A[m , k] = aux[k]
            temp = b[i]
            b[i] = b[m]
            b[m] = temp

def Gauss_Lie(A , b):
    Eliminate_Pivot(A , b)                # ��������Ԫ
    Gaussian_Function.gauss(A , b)        # Ȼ���ٸ�˹��Ԫ