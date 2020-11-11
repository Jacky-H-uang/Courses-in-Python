# Created By Jacky on 2020/11/7

"""
散点图
"""


import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x, y)
plt.show()