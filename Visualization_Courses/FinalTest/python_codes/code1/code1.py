# Created By Jacky on 2020/12/27


"""
各个省录取分数线情况
"""
import pandas as pd
from pyecharts.charts import *
import pyecharts.options as opts
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号

# 取5个城市
city = ['湖北','上海','北京','广东','上东']

# 加载数据
def load_data(filename):
    data = pd.read_csv(filename)

    x_data = data.省份
    y_data = data.分数线
    data_pair = dict()
    for i,j in zip(x_data,y_data):
        if i in data_pair.keys():
            continue
        data_pair[i] = j

    return data_pair


# 可视化部分
def plotter(filenames):
    city1 = '湖北'
    city2 = '北京'
    city3 = '四川'
    city4 = '广东'
    city5 = '山东'
    year = ['2016年','2017年','2018年','2019年','2020年']
    scores_city1 = []
    scores_city2 = []
    scores_city3 = []
    scores_city4 = []
    scores_city5 = []
    for f in filenames:
        data_dict = load_data(f)
        for x , y in data_dict.items():
            if x == city1:
                scores_city1.append(y)
            elif x == city2:
                scores_city2.append(y)
            elif x == city3:
                scores_city3.append(y)
            elif x == city4:
                scores_city4.append(y)
            elif x == city5:
                scores_city5.append(y)
    (
        Line()
        .add_xaxis(xaxis_data = year)
        .add_yaxis(
            series_name="湖北省",
            stack = "总量",
            y_axis = scores_city1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="北京市",
            stack="总量",
            y_axis = scores_city2,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="四川省",
            stack="总量",
            y_axis=scores_city3,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="广东省",
            stack="总量",
            y_axis=scores_city4,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="山东省",
            stack="总量",
            y_axis=scores_city5,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(trigger = "axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show = True),
                splitline_opts=opts.SplitLineOpts(is_show = True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap = False),
        )
        .render("code1.html")
    )


# 测试
if __name__ == '__main__':
    f = [
        '2016年各省份录取分数线.csv',
        '2017年各省份录取分数线.csv',
        '2018年各省份录取分数线.csv',
        '2019年各省份录取分数线.csv',
        '2020年各省份录取分数线.csv'
    ]
    plotter(f)