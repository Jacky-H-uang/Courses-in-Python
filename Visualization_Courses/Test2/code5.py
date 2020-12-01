# Created By Jacky on 2020/11/16


"""
选出最后大众喜欢的电影（只列前5名，按美国和其他国家排名）
"""

import numpy as np
from pyecharts.charts import *
import pyecharts.options as opts
import csv
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号

# 加载数据
# 返回美国和其他国家的排行榜
def loadData(filenames):
    USA = []
    OTHER = []
    for filename in filenames:
        usa = {}
        other = {}
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                # 按照美国
                usa[row[0]] = row[8]
                # 按照其他国家
                other[row[0]] = row[9]
            f.close()
        USA.append(usa)
        OTHER.append(other)

    # 返回字典列表
    return USA , OTHER





# 解析数据
# 返回一个拥有每年观众得分的元组列表
def parserData(filenames):
    usa, other = loadData(filenames)
    retUSA = []
    retOTHER = []


    # 遍历每一年美国的数据
    for i in range(len(usa)):
        temp = {}
        for x, y in usa[i].items():
            if x == '' or y == '':  continue
            y = ''.join([t for t in y if t.isdigit() or t == '.'])
            if y == '': continue
            temp[x] = float(y)
        ret = sorted(temp.items() , key = lambda x : x[1],reverse=True)[:5]
        retUSA.append(ret)


    # 遍历每一年的其他国家的数据
    for i in range(len(other)):
        temp = {}
        for x, y in other[i].items():
            if x == '' or y == '':  continue
            y = ''.join([t for t in y if t.isdigit() or t == '.'])
            if y == '': continue
            temp[x] = float(y)
        ret = sorted(temp.items() , key = lambda x : x[1],reverse=True)[:5]
        retOTHER.append(ret)

    return retUSA , retOTHER




# 聚集数据
# def clusterData(filenames):
#         usa, other = parserData(filenames)
#         UsaDic = {}
#         OtherDic = {}
#         for i in range(len(usa)):
#                 L = usa[i]
#                 # 每一年的数据
#                 for x, y in L:
#                         UsaDic[x] = y
#         retUsa = sorted(UsaDic.items() , key = lambda x : x[1] , reverse = True)
#         retUsa = retUsa[:5]
#
#         for i in range(len(other)):
#                 L = other[i]
#                 # 每一年的数据
#                 for x, y in L:
#                         OtherDic[x] = y
#         retOther = sorted(UsaDic.items() , key = lambda x : x[1] , reverse = True)
#         retOther = retOther[:5]
#
#         return retUsa , retOther



# Viusalization
def plotter(filenames):
    index = 2007
    USA, Other = parserData(filenames)

    # Problem
    # 没有参考系

    timeLine1 = Timeline()
    timeLine2 = Timeline()
    g = Grid(init_opts = opts.InitOpts(width = "1600px",height = "1000px"))
    for i in range(len(USA)):
        L = USA[i]
        temp1 = [x[0] for x in L]
        temp2 = [x[1] for x in L]
        barX = (
            Bar()
                .add_xaxis(temp1)
                .add_yaxis("票房$m", temp2, is_show_background=True, category_gap="80%")
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts(title = str(index) + "年美国受欢迎电影 ：Top5"),
                    xaxis_opts = opts.AxisOpts(name="电影名称", axislabel_opts={"rotate":15,"color": "blue"}),
                    toolbox_opts=opts.ToolboxOpts(is_show = True),
                    yaxis_opts = opts.AxisOpts(name="票房", axislabel_opts={"rotate": 30}),
                    legend_opts = opts.LegendOpts(is_show = True),

                )
            )
        timeLine1.add(barX , str(index) + "年")
        index += 1
    timeLine1.render("code5.html")
    index = 2007

    for i in range(len(Other)):
        L = Other[i]
        temp1 = [x[0] for x in L]
        temp2 = [x[1] for x in L]
        barX = (
            Bar()
                .add_xaxis(temp1)
                .add_yaxis("票房$m", temp2, is_show_background=True, category_gap="80%")
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts(title = str(index) + "年其他国家受欢迎电影 ：Top5"),
                    xaxis_opts = opts.AxisOpts(name="电影名称", axislabel_opts={"rotate":15,"color": "blue"}),
                    toolbox_opts=opts.ToolboxOpts(is_show = True),
                    yaxis_opts = opts.AxisOpts(name="票房", axislabel_opts={"rotate": 30}),
                    legend_opts = opts.LegendOpts(is_show = True),
                )
            )
        timeLine2.add(barX , str(index) + "年")
        index += 1

    timeLine2.render("code5_.html")





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