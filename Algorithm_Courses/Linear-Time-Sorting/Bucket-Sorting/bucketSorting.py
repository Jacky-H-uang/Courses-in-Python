# Created By Jacky on 2020/11/23


"""
关于桶排序：
    桶排序将 [0,1) 区间划分为 n 个相同大小的子区间 , 或称为桶。然后 , 将 n 个输入数分别放到各个桶里。
    因为输入数据是均匀 , 独立分布在 [0,1) 区间上 , 所以一般不会出现很多数落在同一个桶的情况下
"""

import datetime
import random
import sys





# 创建数据集合
def createData(n,k):
    retArr = []
    for i in range(n):
        retArr.append(random.randint(0,k))

    return retArr

# 获取桶的数量 , 即应该分出多少个桶
def getNum(arr):
    minVal = sys.maxsize
    maxVal = - sys.maxsize - 1
    for i in range(len(arr)):
        if arr[i] > maxVal:
            maxVal = arr[i]
        if arr[i] < minVal:
            minVal = arr[i]

    bucketNum = (maxVal - minVal) // len(arr) + 1

    return minVal , maxVal , bucketNum


# 桶排序
def bucketSorting(arr):
    minVal , maxVal , bucketNum = getNum(arr)

    # 初始化桶
    bucket = []
    for i in range(bucketNum):
        temp = list()
        bucket.append(temp)


    for i in range(len(arr)):
        temp = (arr[i] - minVal) // len(arr)

        bucket[temp].append(arr[i])

    for i in range(len(bucket)):
        bucket[i].sort()

    index = 0
    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            arr[index] = bucket[i][j]
            index += 1



if __name__ == '__main__':
    n = int(input("要排序多少个数字 : "))
    k = int(input("要排序数组的范围0 ~ : "))

    arr = createData(n,k)
    print("排序前 : {}".format(arr))
    start = datetime.datetime.now()
    bucketSorting(arr)
    end = datetime.datetime.now()
    print("排序后 : {}".format(arr))
    print("\n排序时间 : {} (s)".format((end - start).seconds))