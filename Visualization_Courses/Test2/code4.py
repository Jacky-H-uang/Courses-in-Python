# Created By Jacky on 2020/11/16


"""
统计2007-2011年票房收入走势
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
from pyecharts.charts import *
import pyecharts.options as opts

plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号


# 加载文件
# 统计每一年的总票房然后返回
def loadData(filenames):
    allBoxOffice = []
    for filename in filenames:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            cnt = 0.0
            for row in reader:
                num = ''.join([x for x in row[10] if x.isdigit() or x == '.'])
                if num == '': continue
                cnt += float(num)
            cnt = round(cnt,5)
            allBoxOffice.append(cnt)
            f.close()

    return allBoxOffice




# 分析数据
def analysisData(filenames):
    year = [str(x) + "年" for x in range(2007,2012)]
    ret = []
    val = loadData(filenames)
    return year , val




# Visualization
def plotter(filenames):
    year , data = analysisData(filenames)
    fig = (
        Line(init_opts = opts.InitOpts(width = "1600px",height = "800px"))
        .add_xaxis(xaxis_data = year)
        .add_yaxis(
            series_name = "年票房收入($m)",
            y_axis = data,
            markpoint_opts = opts.MarkPointOpts (
                data = [
                    opts.MarkPointItem(type_ = "max", name="最高票房"),
                    opts.MarkPointItem(type_ = "min", name="最低票房"),
                ]
            ),
            markline_opts=opts.MarkLineOpts (
                data=[opts.MarkLineItem(type_="average", name="平均票房")]
            ),
        )
        .set_global_opts(
            title_opts = opts.TitleOpts(title = "2007~2011好莱坞票房趋势"),
            tooltip_opts=opts.TooltipOpts(trigger = "axis"),
            toolbox_opts=opts.ToolboxOpts(is_show = True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
        .render("code4.html")
    )




if __name__ == '__main__':
    # 初始化列表
    films = [
            'Most Profitable Hollywood Stories - US 2007.csv' ,
            'Most Profitable Hollywood Stories - US 2008.csv',
            'Most Profitable Hollywood Stories - US 2009.csv' ,
            'Most Profitable Hollywood Stories - US 2010.csv',
            'Most Profitable Hollywood Stories - US 2011.csv'
            ]

    print(plotter(films))