# Created By Jacky on 2020/11/10
# -*- coding:utf-8  -*-

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

"""
反应 2007 ~ 2011 美国电影类型的情况
"""


# 加载文件
def loadData(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        story = []
        for row in reader:
            if row[5] == '':  continue
            story.append(row[5])

    return story


# 数据分析，返回分析结果
def paserData(A):
    count = { }
    for X in A:
        for a in X:
            a = a.upper()
            if a == '' : continue

            if a not in count : count[a] = 1
            count[a] = count[a] + 1

    count = sorted(count.items() , key = lambda x : x[1])

    return count



# 柱状图添加标签的颜色
def add_labels(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width + 3 , rect.get_y() + rect.get_height()/10, str(width) + "部", ha = 'center', va ='bottom')
        rect.set_edgecolor('blue')



# 绘制柱状图
def plotter(dic):

    x = []
    y = []

    for i , j in dic:
        x.append(i)
        y.append(j)

    # 为柱状图设置 label
    text = plt.barh(y =  x, height = 0.6 , color = (0.5,0.4,0.3) , width = y)
    plt.tick_params(axis='y', rotation = 15, color='red')
    plt.title("反应 2007 ~ 2010 美国电影类型的情况",fontsize = 23,color = (0.1,0.5,0.6))
    add_labels(text)
    plt.xlabel("电影部数",color = (0.8,0.4,0.2),fontsize = 14)
    plt.ylabel("电影类型" , color = (0.8,0.4,0.2),fontsize = 14)


    plt.show()



# Test
if __name__ == '__main__':
    # 初始化列表
    films = [
            'Most Profitable Hollywood Stories - US 2007.csv' ,
            'Most Profitable Hollywood Stories - US 2008.csv',
            'Most Profitable Hollywood Stories - US 2009.csv' ,
            'Most Profitable Hollywood Stories - US 2010.csv',
            'Most Profitable Hollywood Stories - US 2011.csv'
          ]

    # 存储数据集合
    dataSet = []
    for data in films:
        dataSet.append(loadData(data))

    # 解析数据
    dic = paserData(dataSet)

    # Visualization
    plotter(dic)