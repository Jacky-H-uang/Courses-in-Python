# Created By Jacky on 2020/11/10

"""
统计2007-2011年电影票房排行榜（只排前20）
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号




# 加载数据
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

    ret = { }

    # str 转为 float 类型
    for X in A:
        for i , j in X.items():
            s = ''.join([x for x in j if x.isdigit() or x == '.'])
            if s == '':continue
            ret[i] = float(s)

    ret = sorted(ret.items(),key = lambda x:x[1],reverse = True)[:20]

    return ret



# Visualization
def plotter(filenames):
    A = parserData(filenames)
    X = [x[0] for x in A]
    Y = [y[1] for y in A]

    print(X)
    print(Y)




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
