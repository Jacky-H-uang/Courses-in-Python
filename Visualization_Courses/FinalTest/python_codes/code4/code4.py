# Created By Jacky on 2020/12/27


"""
展示 十大 热门以及 冷门专业
"""

import pandas as pd
from pyecharts.charts import *
import pyecharts.options as opts
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号


# 加载数据
def load_data():
    data = pd.read_csv('2020年湖北省各专业录取数量.csv')
    x_data = data.专业名称
    y_data = data.录取数

    data_p = [list(z) for z in zip(x_data,y_data)]

    data_p.sort(key = lambda x : x[1],reverse=True)
    data_hot = data_p[:10]
    data_cold = data_p[-10::]
    return data_hot, data_cold

# 可视化
def plotter():
    data_hot , data_cold = load_data()
    c1 = (
        Bar()
        .add_xaxis([_[0] for _ in data_hot])
        .add_yaxis("热门专业Top10", [_[1] for _ in data_hot])
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(name="专业录取数",axislabel_opts={"rotate":30,"color":"blue"}),
            xaxis_opts=opts.AxisOpts(name="专业",axislabel_opts = {"rotate":30}),
        )
        .render("code4-1.html")
    )
    c1 = (
        Bar()
        .add_xaxis([_[0] for _ in data_cold])
        .add_yaxis("冷门专业Top10", [_[1] for _ in data_cold])
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(name="专业录取数",axislabel_opts={"rotate":30,"color":"blue"}),
            xaxis_opts=opts.AxisOpts(name="专业",axislabel_opts = {"rotate":30}),
        )
        .render("code4-2.html")
    )

if __name__ == '__main__':
    plotter()