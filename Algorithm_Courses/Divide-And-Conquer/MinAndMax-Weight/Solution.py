# Created By Jacky on 2020/11/11


"""
问题描述：
    给定一个数量为 N 的物品重量的列表找出其中最大重量的物品和最小重量的物品

Input  : An array of the integer
Output : Return the max and min weight
"""

import math
import random

def createData():
    A = []
    for i in range(100):
        A.append(random.randint(1,1000))

    return A


def findMaxMinWeight(Array,L,R):
    if L == R:          return Array[L] , Array[R]
    if L + 1 == R :     return max(Array[L],Array[R]) , min(Array[L],Array[R])
    mid = (L+R) >> 1

    W1max , W1min = findMaxMinWeight(Array , L , mid)
    W2max , W2min = findMaxMinWeight(Array , mid+1,R)


    return max(W1max,W2max) , min(W1min,W2min)


def findMMW():
    A = createData()
    return findMaxMinWeight(A,0,len(A)-1)


if __name__ == '__main__':
    maxV,minV = findMMW()
    print("Max-Weight : " + str(maxV))
    print("Min-Weight : " + str(minV))