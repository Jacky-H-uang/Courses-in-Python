# Created By Jacky on 2021/4/28


import numpy as np
from NumericalAnalysis_Courses.Gauss_Seidel.gauss_seidel import gauss_seidel


A = np.mat([[3,1,-1],[2,4,1],[-1,2,5]])
b = np.mat([4,1,1]).T

gauss_seidel(A,b,24)


