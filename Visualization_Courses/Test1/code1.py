# Created By Jacky on 2020/11/7

"""
numpy 产生随机数的几种方法
"""

import numpy as np


#范围内的整数
a = np.random.randint(0,10,100)
print(a)

# 0 到 1 的均匀分布
b = np.random.rand(40)
print(b)

# 标准正态分布
c = np.random.randn(10)
print(c)

# 生成指定正态分布
d = np.random.normal(0,1,100)
print(d)

# 0 到 1 的均匀分布
e = np.random.random(20)
print(e)

# 0 到 1 的均匀分布
f = np.random.ranf(20)
print(f)

# 指定均匀分布
g = np.random.uniform(-1,1,100)
print(g)