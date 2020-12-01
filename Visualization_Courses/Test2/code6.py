# Created By Jacky on 2020/11/16


"""
选出最赚钱的电影  (只排前20)
"""



import csv
import matplotlib.pyplot as plt
import numpy as np
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType


plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号



# 加载数据
def loadData(filenames):
    f_w = {}
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
                if row[0] == '': continue
                if row[0] not in f_w:  f_w[row[0]] = round(float(X) - float(Y))       # 保留小数点后 5 位
                f_w[row[0]] += round(float(X) - float(Y))
            f.close()

    return f_w



# 分析数据
def parserData(filenames):
    fw = loadData(filenames)
    # 取排名前 20 的公司：
    ret = sorted(fw.items() , key = lambda x : x[1] , reverse = True)
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

    P = (
        Pie()
            .add(
            "电影利润",
            AUX,
            center=["40%", "50%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2007~2010最赚钱电影 Top20"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient = "vertical"),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(formatter="{c} ($m)")
        )
        .render("code6.html")
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
