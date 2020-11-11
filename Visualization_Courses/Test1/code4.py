# Created By Jacky on 2020/11/9

"""
柱状图
"""

import numpy as np
import  matplotlib.pyplot as plt

N = 5
y = [20,10,30,25,15]
y1 = np.random.randint(10,50,N)

index = np.arange(N)

plt.bar(x = index , height = y , color = 'red' , width = 0.3)
plt.bar(x = index + 0.3 , height = y1 , color = 'black' , width = 0.3)

plt.show()