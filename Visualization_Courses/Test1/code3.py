# Created By Jacky on 2020/11/7


"""
折线图
"""

import numpy as np
import matplotlib.pyplot as plt


# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 普通折线图
fruits = ['苹果','香蕉','凤梨','桔子','橙','桃子']
shop1_sales = [8888,3323,6989,8873,3876,15409]
shop2_sales = [4888,7023,3989,5873,8876,6409]

plt.plot(fruits,shop1_sales)
plt.plot(fruits,shop2_sales)
plt.legend(["商家A","商家B"])

plt.show()