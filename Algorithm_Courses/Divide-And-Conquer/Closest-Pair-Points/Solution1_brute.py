# Created By Jacky on 2020/11/7


"""
This is Closest Pair Points Problem BruteForce Solution:
Input : point pairs
ouput : min distance
"""

from math import *
import sys
import random


# 随机生成 1000 个坐标在 -10000~10000 的点
def shuffData():
    with open("digits.txt", "w") as f:
        for i in range(1000):
            x = random.uniform(-10000, 10000)
            y = random.uniform(-10000, 10000)
            line = str(x) + " " + str(y)
            f.write(line + '\n')
        f.close()

# 初始化点对
def init():
    with open("digits.txt") as f:
        ret = []
        for line in f:
            line = line.split(' ')
            x = float(line[0])
            y = float(line[1])
            ret.append((x, y))
        f.close()
        return ret


# 计算两点的欧几里德距离
def calcDist(i,j,points):
    return sqrt(pow(points[i][0] - points[j][0],2) + pow(points[i][1] - points[j][1],2))


# 暴力法找出最短点距
def bruteforce():
    # 初始化点对和最大距离
    points = init()
    dist = sys.float_info.max

    # 暴力搜索每个点到所有点的距离并记录最短的距离
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            dist = min(dist,calcDist(i,j,points))

    return dist


if __name__ == '__main__':
    # 生成随机数组
    shuffData()
    print(bruteforce())