# Created By Jacky on 2020/11/10

"""
统计2007-2011年电影票房排行榜（只排前20）
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pygal
import squarify

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
    ret = sorted(ret,key = lambda x:x[1],reverse=True)

    return ret




# Visualization
# 方形图来显示 Top 20 的票房情况
def plotter(filenames):
    A = parserData(filenames)
    print(A)
    X = []
    Y = []
    values = []

    index = 1
    for i in range(len(A)):
        values.append(str(A[i][1]) + "$m")
        X.append(A[i][0] + "\n(rank" + str(index) + ")")
        Y.append(A[i][1])
        index += 1
    my_dpi = 96
    plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
    colors = ['steelblue', '#9999ff', 'red', 'indianred', 'deepskyblue', 'lime', 'magenta', 'violet', 'peru', 'green',
              'yellow', 'orange', 'tomato', 'lawngreen', 'cyan', 'darkcyan', 'dodgerblue', 'teal', 'tan', 'royalblue']
    plot = squarify.plot(
        sizes=Y,            # 指定绘图数据
        label=X,            # 指定标签
        value=values,       # 添加数值标签
        edgecolor='white',  # 设置边界框为白色
        linewidth=3,        # 设置边框宽度为3
        alpha=.6,           # 设置透明度
        color=colors
    )
    plot.set_title('2007-2011年电影票房排行榜 Top20', fontdict={'fontsize': 24, 'color': (0.5,0.6,0.2)})
    plt.rc('font', size=20)

    plt.show()





if __name__ == '__main__':
    # 初始化列表
    films = [
            'Most Profitable Hollywood Stories - US 2007.csv' ,
            'Most Profitable Hollywood Stories - US 2008.csv',
            'Most Profitable Hollywood Stories - US 2009.csv' ,
            'Most Profitable Hollywood Stories - US 2010.csv',
            'Most Profitable Hollywood Stories - US 2011.csv'
            ]

    plotter(films)