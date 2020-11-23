# Created By Jacky on 2020/11/23


"""
关于基数排序：
    基数排序假设 n 个 d 位元素存放在数组 A 中 , 其中第一位为最低位 , 第 d 位为最高位。
    算法运行时间为 O(d(n+k)), d 代表 d 位数 , k 代表每一个数位有 n 个可能的取值。
    当 d 为常数 , 且 k = O(n) 的时候基数排序有线性的时间代价。
思想：
    将整数按位切分成不同的数字 , 然后按每个位数分别比较。
"""

import random


def createArray(Num,X):
    retA = []
    for i in range(Num):
        retA.append(random.randint(0,X))

    return retA



# 取出数组中的最大的元素
def getMax(Array,N):
    maxVal = Array[0]
    for i in range(N):
        if Array[i] > maxVal:
            maxVal = Array[i]

    return maxVal


# 将每个数字计算出来其 exp 位的数字然后排序
def radixHelper(Array,N,exp):
    AUX = [0] * (N+1)
    Bucket = [0] * 10           # 10 个桶来存放在位为 0~9 的数字

    # 这里采用计数排序的思路
    for i in range(N):
        Bucket[(Array[i]//exp)%10] += 1

    for i in range(1,N):
        Bucket[i] += Bucket[i-1]

    for i in range(N-1,-1,-1):
        AUX[Bucket[(Array[i]//exp)%10]-1] = Array[i]
        Bucket[(Array[i]//exp)%10] -= 1

    for i in range(N):
        Array[i] = AUX[i]




# 基数排序
def radixSorting(Array):
    N = len(Array)
    maxVal = getMax(Array,N)
    exp = 1
    while maxVal / exp > 0:
        radixHelper(Array,N,exp)
        exp *= 10




# Test
if __name__ == '__main__':
    num = input("输入要排序数字的个数：")
    num = int(num)
    k = input("要排序的范围：0 ~ ")
    k = int(k)

    A = createArray(num,k)
    # A = [53,542,3,63,14,213,154,748,616]
    print("排序前：\n{}".format(A))
    radixSorting(A)
    print("排序后：\n{}".format(A))