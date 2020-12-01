# Created By Jacky on 2020/11/12


"""
任务3：统计2007-2011年最赚钱电影制片公司排行榜（只排前20）
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType


plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号



# 加载数据
def loadData(filenames):
    studio_w = {}
    for filename in filenames:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # 公司的利润等于 ： 收入 - 成本
            for row in reader :
                # 清洗数据
                X = ''.join([x for x in row[10] if x.isdigit() or x == '.'])
                Y = ''.join([x for x in row[11] if x.isdigit() or x == '.'])
                if X == '' : X = '0'
                if Y == '' : Y = '0'
                if row[1] == '': continue
                if row[1] not in studio_w:  studio_w[row[1]] = round(float(X) - float(Y))       # 保留小数点后 5 位
                studio_w[row[1]] += round(float(X) - float(Y))
            f.close()

    return studio_w



# 分析数据
def parserData(filenames):
    SW = loadData(filenames)
    # 取排名前 20 的公司：
    ret = sorted(SW.items() , key = lambda x : x[1] , reverse = True)
    ret = ret[:20]

    return ret



# Visualization
def plotter(filenames):
    AUX = parserData(filenames)
    X = []
    Y = []
    for i , j in AUX:
        X.append(i)
        Y.append(j)



    bar = (
        Bar(init_opts=opts.global_options.InitOpts(width="1600px",height = "800px"))
        .add_xaxis(X)
        .add_yaxis("公司利润($m)",Y,is_show_background = True,category_gap="60%")
        .set_series_opts(
            label_opts = opts.LabelOpts(position="top"),
        )
        .set_global_opts(
            title_opts = opts.TitleOpts(title = "2007-2010最赚钱电影公司 Top20 排行榜"),
            xaxis_opts = opts.AxisOpts(name = "公司名称",axislabel_opts = {"rotate":30,"color":"blue"}),
            yaxis_opts = opts.AxisOpts(name = "公司盈利" , axislabel_opts = {"rotate":30})
        )
        .render("code3.html")
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

    # Visualization
    plotter(films)