# Created By Jacky on 2021/4/7


import numpy as np
from NumericalAnalysis_Courses.Gaussian_Elimination import Gaussian_Function
from NumericalAnalysis_Courses.Gaussian_Elimination.Elimination_with_Maximal_Column_Pivoting import Eliminate_Pivot


# Test 1
print("高斯消元法:\n")
A = np.mat([[1,2,1],[3,8,1],[0,4,1]])
b = np.mat([2,12,2]).T
x = Gaussian_Function.gauss(A,b)



# Test 2
print("\n列主消元法:\n")
A = np.mat([[0.001 , 2.000 , 3.000],[-1.000,3.712,4.623],[-2.000,1.072,5.643]])
b = np.mat([1.000,2.000,3.000]).T
Eliminate_Pivot(A,b)