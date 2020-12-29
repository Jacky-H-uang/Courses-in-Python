# Created By Jacky on 2020/12/27

"""
部分省份录取人数 2016~2020 比例
"""

import pandas as pd
from pyecharts.charts import *
import pyecharts.options as opts
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号


# 加载数据
def load_data(filename):
    data = pd.read_csv(filename)
    x_d = data.省份
    y_d = data.录取数
    data_p = list()
    for i , j in zip(x_d,y_d):
        data_p.append([i,j])
    data_p.sort(key = lambda x:x[1],reverse = True)
    return data_p[1:9]


# 可视化
def plotter():
    tl = Timeline()
    for i in range(2016, 2021):
        data = load_data(str(i) + '年.csv')
        pie = (
            Pie()
            .add(
                "城市",
                data,
                rosetype="radius",
                radius=["30%", "55%"],
            )

        )
        tl.add(pie, "{}年".format(i))
    tl.render("code3.html")

if __name__ == '__main__':
    plotter()