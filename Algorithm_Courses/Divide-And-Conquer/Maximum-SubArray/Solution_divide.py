# Created By Jacky on 2020/11/8

"""
BackGround :
    你现在投资一家公司的股票,你可以在一个时间买入股票，在未来的某个时刻卖出股票，其中的利润为两只股票的差值
    然后现在给出了该公司股票未来的多天的股票市值情况，
    请你计算出在什么时候买入股票，并在什么时候卖出的时候使得利润最大。

This is a Solution for Maximum-SubArray Problem Using Divide-And-Conquer.
Input  :  An Array of Integer
Output :  Return the Maximum difference of two elements (return max(a[j] - a[i])   j > i)

"""

import sys
import random


# 生成数据 以 100 只股票为数据集生成价值 100 ~ 1000 的股票
def creatData():
    data = []
    for i in range(100):
        data.append(random.randint(100,1001))
    for x in data:
        print(x)
    return data

# 计算变化的差值的数组
def pretreatment(A):
    ret = []
    for i in range(1,len(A)):
        ret.append(A[i] - A[i-1])

    return ret


# 处理分治的合并项
# 返回合并的最左边界，合并的最右边界，合并区间得到的最大子数组的和
def findMaxCrossingSubarray(A,low,mid,high):
    leftsum = - 1000000
    sum = 0
    maxleft = 0
    for i in range(low,mid+1)[::-1]:
        sum = sum + A[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i

    rightsum = -1000000
    sum = 0
    maxright = 0
    for i in range(mid + 1 , high):
        sum = sum + A[i]
        if sum > rightsum:
            rightsum = sum
            maxright = i

    return (maxleft,maxright,leftsum + rightsum)



def findMaxmumSubarray(A,low,high):
    # 只含一种元素的时候的情况
    if low == high:     return  (low , high , A[low])

    else :
        mid = (low + high) >> 1
        (leftlow , lefthigh , leftsum) = findMaxmumSubarray(A,low,mid)
        (rightlow , righthigh , rightsum) = findMaxmumSubarray(A,mid+1,high)
        (crosslow , crosshigh , crosssum) = findMaxCrossingSubarray(A,low,mid,high)

        if leftsum >= rightsum and leftsum >= crosssum:     return (leftlow,lefthigh,leftsum)
        elif rightsum >= leftsum and rightsum >= crosssum:  return (rightlow,righthigh,rightsum)
        else:                                               return (crosslow,crosshigh,crosssum)

def MaxSubArray(A):
    retL , retR ,retSum = findMaxmumSubarray(A,0,len(A)-1)
    return retSum


if __name__ == '__main__':
    A = creatData()
    arr = pretreatment(A)
    print("最大的利润 : " + str(MaxSubArray(arr)))