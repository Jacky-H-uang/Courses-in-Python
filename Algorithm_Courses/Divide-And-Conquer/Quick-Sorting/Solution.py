# Created By Jacky on 2020/11/11


"""
问题描述：
    给定一个整数数组，要求排序将其排成单调数组
Input  : An Array of Integer shuffled.
Output : The monotonous Array.
"""

import random


# 创建一个 100 个数字的打乱的数组
def createDataSet():
    ret = []
    for i in range(100):
        ret.append(random.randint(0,10000))

    random.shuffle(ret)

    return ret


# 交换函数
def exchange(Array,i,j):
    temp = Array[i]
    Array[i] = Array[j]
    Array[j] = temp

# 利用 pivot 来分区
def partition(Array,p,r):
    x = Array[r]
    i = p - 1
    for j in range(p,r):
        if Array[j] <= x:
            i = i + 1
            exchange(Array , i , j)
    exchange(Array,i+1,r)

    return i + 1


# 快速排序分治  (ps : 这里是朴素版本的快排,当然也可以采用随机化版本的快速排序来随机化 q)
def quickSort(Array,L,R):
    if L  <  R :
        q = partition(Array,L,R)
        quickSort(Array,L,q-1)          # 分治排左边比 Array[q] 小的
        quickSort(Array,q+1,R)          # 分治排右边比 Array[q] 大的




def qS(Array):
    quickSort(Array,0,len(Array)-1)
    return Array


if __name__ == '__main__':
    Arr = createDataSet()
    print("排序前 : " + str(Arr))
    print("排序后 : " + str(qS(Arr)))