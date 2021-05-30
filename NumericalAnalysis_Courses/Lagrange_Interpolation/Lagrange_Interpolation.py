# Created By Jacky on 2021/5/26

import numpy as np
import matplotlib.pyplot as plt
from sympy import expand
from sympy.abc import x


def lagrange_inter(Xa:list,y):
    L = len(y)
    langrange_ploy = 0
    for k in range(L):
        langrange_ploy += y[k] * lagrange_func(k,Xa.copy())

    return expand(langrange_ploy)


def lagrange_func(k,Xa:list):
    # 删除第 k 个数字
    x_del = Xa[k]
    Xa.pop(k)

    Xa = np.array(Xa)
    return np.prod((x - Xa) / (x_del - Xa))


if __name__ == '__main__':
    xa = [0,np.pi/6,np.pi/4,np.pi/3,np.pi/2]
    x_array = np.array(xa)
    ya = np.array([np.sin(a) for a in x_array])
    lagrange_2 = lagrange_inter(xa, ya)
    real = np.sin(np.pi/12)
    estimate = lagrange_2.subs(x,np.pi/12)
    error = real - estimate
    print("真实值 sin(π/12) = " , np.sin(np.pi/12))
    print("拉格朗日插值多项式为:{}".format(lagrange_2))
    print("拉格朗日插值多项式在x = π/12处的值 : " , estimate)
    print("实际绝对误差 = " , real - estimate)