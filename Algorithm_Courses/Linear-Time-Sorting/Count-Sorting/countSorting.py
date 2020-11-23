# Created By Jacky on 2020/11/19


"""
关于计数排序：
    计数排序假设 n 个输入元素中的每一个都是 0 到 k 区间内的一个整数,其中 k 为某个整数。
    当 k = O(n) 时，排序的运行时间为 O(n)

思想:
    对每一个输入元素 x ，确定小于 x 的元素个数。利用这一信息就可以直接把 x 放到它在输出数组位置上了。
缺点：
    计数排序只能对正整数排序，且无法对负数排序
"""


import random
import datetime
import time


# 产生数据集合
# 产生 0 ~ k 区间内的任意整数
def createDataSet(num , k):
    A = [0] * (1+num)
    for i in range(1,num+1):
        A[i] = random.randint(0,k)      # 产生 [0,k] 的随机数


    return A



# 计数排序
# A 为一个输入数组
# B 为一个输出数组
# k 表示整数的范围

def countSorting(A,k):
    # 初始化计数数组 C : 0 ~ k 输出数组 B
    C = [0] * (k+1)
    B = [0] * len(A)

    # 统计输入数组 A 中元素的个数
    for i in range(1,len(A)):
        C[A[i]] += 1

    # 统计 C 数组的前缀和
    for i in range(1,k+1):
        C[i] += C[i-1]

    # 计数排序
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1

    return B


# 测试
if __name__ == '__main__':
    num = input("输入要排序数字的个数：")
    num = int(num)
    k = input("要排序的范围：0 ~ ")
    k = int(k)

    A = createDataSet(num,k)

    print("排序前：")
    print(A)
    start = datetime.datetime.now()
    result = countSorting(A,k)
    end = datetime.datetime.now()
    print("排序后：")
    print(result)

    print("\n 算法运行时间 ： " + str((end - start).seconds) + " s")