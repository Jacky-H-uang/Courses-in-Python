# Created By Jacky on 2021/4/28


import numpy as np
from NumericalAnalysis_Courses.Gauss_Seidel.gauss_seidel import gauss_seidel
from NumericalAnalysis_Courses.Gauss_Seidel.jacobi import jacobi_iteration
from NumericalAnalysis_Courses.Gauss_Seidel.SOR import sor_function


def compareThree(A,b,k,w,error):
    print("比较三种方法的收敛速度")
    print("======================\n")

    print("一 : Jacobi Method")
    c1 , xc = jacobi_iteration(A,b,k,error)
    print("迭代次数 : ",c1)
    print("最终收敛 : " , xc)

    print("\n二 : Gauss Seidel")
    c2 , xc = gauss_seidel(A,b,k,error)
    print("迭代次数 : ",c2)
    print("最终收敛 : " , xc)

    print("\n三 : SOR ")
    c3 , xc = sor_function(A,b,w,k,error)
    print("迭代次数 : ",c3)
    print("最终收敛 : " , xc)


if __name__ == '__main__':
    k = 100                 # 迭代 100 次
    w = 1.1                 # 松弛参数 1.1
    error = 0.000001        # 误差 0.000001

    A = np.mat([[3,-1,0,0,0,0.5],[-1,3,-1,0,0.5,0],[0,-1,3,-1,0,0],[0,0,-1,3,-1,0],[0,0.5,0,-1,3,-1],[0.5,0,0,0,-1,3]])
    b = np.mat([2.5,1.5,1,1,1.5,2.5]).T

    compareThree(A,b,k,w,error)