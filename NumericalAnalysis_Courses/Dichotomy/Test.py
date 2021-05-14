# Created By Jacky on 2021/5/12


import numpy as np

from NumericalAnalysis_Courses.Dichotomy.binary_fuc import binary
from NumericalAnalysis_Courses.Dichotomy import binary_fuc
from NumericalAnalysis_Courses.Dichotomy.binary_fuc import accurency
from NumericalAnalysis_Courses.Dichotomy.Simple_Iteration import simple_iter
from NumericalAnalysis_Courses.Dichotomy import Simple_Iteration


def f1(x):
    return np.cos(x) - x
def f2(x):
    f = np.poly1d([1,0,0,-9])
    return f(x)
def g(x):
    f = np.poly1d([-2,1,3])
    return f(x)**(1/4)


if __name__ == '__main__':

    print("1 : 二分法求解 [0,1] 区间内 f(x) = cosx-x的零点 : ")
    a = 0
    b = 1
    acc = accurency(a,b,6)
    xc , yc , x , y = binary(f1,a,b,error = acc)
    # binary_fuc.plotter(f,a,b,50,xc,yc,x,y)

    print("2 : 二分法求解 [2,3] 区间内 f(x) = x^3 的零点 : ")
    a = 2
    b = 3
    acc = accurency(a,b,6)
    xc,yc,x,y = binary(f2,a,b,error=acc)
    binary_fuc.plotter(f2,a,b,50,xc,yc,x,y)

    print("\n3 : 简单迭代法")
    simple_iter(g,0,k = 10)
    x = simple_iter(g,0,27)
    y = [g(_x) for _x in x]
    Simple_Iteration.plotter(g,x,y,a = 0,b = 1.5, k = 50)