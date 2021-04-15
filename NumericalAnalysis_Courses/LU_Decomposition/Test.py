# Created By Jacky on 2021/4/14



import numpy as np
from NumericalAnalysis_Courses.LU_Decomposition import LU_Function

def Test(A,b):
    x = LU_Function.LU(A,b)
    print("解得 X : ")
    print(x)


if __name__ == '__main__':

    # Example1:
    A1 = np.mat([[1,2,-1],[2,1,-2],[-3,1,1]])
    b1 = np.mat([3,3,-6]).T
    Test(A1,b1)

    # Example2:
    A2 = np.mat([[1,2,3],[2,5,2],[3,1,5]])
    b2 = np.mat([14,18,20]).T
    Test(A2,b2)

    # Example3:
    A3 = np.mat([[3,7],[6,1]])
    b3 = np.mat([1,-11]).T
    Test(A3,b3)