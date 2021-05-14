# Created By Jacky on 2021/4/28


import numpy as np
from NumericalAnalysis_Courses.Gauss_Seidel.gauss_seidel import gauss_seidel
from NumericalAnalysis_Courses.Gauss_Seidel.jacobi import jacobi_iteration
from NumericalAnalysis_Courses.Gauss_Seidel.SOR import sor_function


def compareThree(A,b,k,w,error):
    print("比较三种方法的收敛速度")
    print("======================\n")

    print("一 : Jacobi Method")
    jacobi_iteration(A,b,100,error=0.00001)

    print("\n二 : Gauss Seidel")
    gauss_seidel(A,b,100,error=0.00001)

    print("\n三 : SOR ")
    sor_function(A,b,1.25,100,error=0.00001)



if __name__ == '__main__':
    k = 100                 # 迭代 100 次
    w = 1.25                # 松弛参数 1.25
    error = 0.00001         # 误差 0.00001

    A1 = np.mat([[-4,1,1,1],[1,-4,1,1],[1,1,-4,1],[1,1,1,-4]])
    b1 = np.mat([1,1,1,1]).T

    #compareThree(A1,b1,k,w,error)

    A2 = np.mat([[4,3,0],[3,4,-1],[0,-1,4]])
    b2 = np.mat([24,30,-24]).T
    compareThree(A2,b2,k,w,error = 0.0000001)