# Created By Jacky on 2020/11/10

"""
统计2007-2011年电影票房排行榜（只排前20）
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pygal

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号




# 加载数据,返回字典列表
def loadData(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        films = { }
        for row in reader:
            films[row[0]] = row[10]
        f.close()

        return films




# 返回一个元组的列表
def parserData(filenames):
    A = []
    for f in filenames:
        tmp = loadData(f)
        del tmp['']
        A.append(tmp)

    ret = []

    # str 转为 float 类型
    for X in A:
        for i , j in X.items():
            s = ''.join([x for x in j if x.isdigit() or x == '.'])
            if s == '':     continue
            ret.append((i,float(s)))

    ret = sorted(ret,key = lambda x:x[1],reverse = True)[:20]
    ret = sorted(ret,key = lambda x:x[1])

    return ret


# 柱状图添加标签的颜色
def add_labels(rects):
    for rect in rects:
        width = rect.get_width()
        plt.text(width + 100, rect.get_y() + rect.get_height()/10, str(width) + " $m", ha = 'center', va ='bottom')
        rect.set_edgecolor('blue')



# Visualization
def plotter(filenames):
    A = parserData(filenames)

    X = []
    Y = []
    for i in range(len(A)):
        X.append(A[i][0])
        Y.append(A[i][1])

    X = np.array(X)
    Y = np.array(Y)

    fig = plt.figure(dpi = 128 , figsize = (10,6))
    plt.title("统计2007-2011年电影票房排行榜  (只排前20)",color = (0.5,0.4,0.3),fontsize = 20)

    text = plt.barh(y = X , color = ['r', 'g', 'b', 'c', 'm', 'y',],height = 0.8,width = Y)
    add_labels(text)
    plt.tick_params(axis = 'y',rotation = 20,color = 'red')
    plt.xlabel("票房价值 ($m)" , color = (0.8,0.4,0.2))
    plt.ylabel("电影名" , color = (0.8,0.4,0.2))

    plt.show()


if __name__ == '__main__':
    # 初始化列表
    films = [
            'Most Profitable Hollywood Stories - US 2007.csv' ,
            'Most Profitable Hollywood Stories - US 2008.csv',
            'Most Profitable Hollywood Stories - US 2009.csv' ,
            'Most Profitable Hollywood Stories - US 2010.csv',
            'Most Profitable Hollywood Stories - US 2010.csv'
            ]

    plotter(films)