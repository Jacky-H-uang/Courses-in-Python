# Created By Jacky on 2020/11/7


"""
This is Closest Pair Points Problem Divide-And-Conquer Solution:
Input : point pairs
ouput : min distance
"""

from math import *
import sys
import random
import operator

# 随机生成 1000 个坐标在 -10000~10000 的点
def shuffData():
    with open("digits.txt", "w") as f:
        for i in range(1000):
            x = random.uniform(-10000, 10000)
            y = random.uniform(-10000, 10000)
            line = str(x) + " " + str(y)
            f.write(line + '\n')


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



# 排序函数
def cmpX(a):
    return a[0]
def cmpY(a,points):
    return points[a][1]



# 分治的方法找出最近点对的距离
def divideandconquer(L,R,points,aux):
    # 最优子结构的时候返回最短的距离
    if L + 1 == R:      return calcDist(L,R,points)
    if L + 2 == R:      return min(min(calcDist(L,L+1,points),calcDist(L+1,R,points)),calcDist(L,R,points))

    mid = (L+R)>>1
    dist = min(divideandconquer(L,mid,points,aux),divideandconquer(mid+1,R,points,aux))

    # 寻找范围内的所有点
    cnt = 0
    for i in range(L,R):
        X = points[i][0]
        Y = points[i][1]
        if X >= X-dist and X <= X+dist:
            aux[cnt] = i
            cnt += 1

    # 按 Y 来排序
    aux = sorted(aux[0:cnt+1],key = lambda a : cmpY(a,points))

    # 寻找区间内的最短距离
    for i in range(cnt):
        for j in range(i+1,cnt):
            if points[aux[j]][1] - points[aux[i]][1] >= dist:   break
            dist = min(dist,calcDist(aux[i] , aux[j] , points))

    return dist

def divide():
    # 初始化点对和最大距离
    points = init()
    # 先按照 x 排序
    points = sorted(points,key = cmpX)
    aux = [len(points)-1 for i in range(0,len(points))]
    return divideandconquer(0,len(points)-1,points,aux)



if __name__ == '__main__':
    # 生成随机数组
    shuffData()
    print(divide())