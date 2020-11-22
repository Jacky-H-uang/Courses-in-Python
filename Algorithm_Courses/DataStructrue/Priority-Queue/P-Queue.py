# Created By Jacky on 2020/11/22

"""
                    Introduction
This it the datastructrue of priority-queue's implemention
It includes four functions

--- 基于大根堆的实现
"""

"""
            API 的主要方法
1. init(MAXN)                   # 初始化优先队列的大小
2. isEmpty()                    # 判断优先队列是否为空
3. deleteMAXVal()               # 删除最大的元素
4. insert(val)                  # 向堆中插入元素
5. size()                       # 判断当前堆的大小
"""


import random


class pQ:
    def __init__(self):
        self.__pqueue = list()
        self.__N = 0


    # 初始化优先队列
    def init(self,MAXN):
        self.__pqueue = [0] * (MAXN + 1)


    # 堆的比较方法
    def __less(self, i, j):
        if int(self.__pqueue[i] - self.__pqueue[j]) < 0:
            return True
        return False


    # 堆的交换
    def __exch(self, i, j):
        t = self.__pqueue[i]
        self.__pqueue[i] = self.__pqueue[j]
        self.__pqueue[j] = t


    # 堆化
    def __heapifySwim(self,k):
        # 上浮类型的堆化
        # 将这个结点和他的父亲结点相比较
        while k > 1 and self.__less(k // 2, k):
            self.__exch(k // 2, k)
            k = k//2
    def __heapifySink(self,k):
        # 下沉类型的堆化
        # 将根结点和字结点比较
        while 2 * k <= self.__N:
            j = 2 * k
            if j < self.__N and self.__less(j, j + 1):  j += 1
            if not self.__less(k, j):      break;
            self.__exch(k, j)
            k = j


    # 向优先队列中插入元素
    def insert(self,val):
        # 尾端添加元素然后在调用swim
        self.__pqueue[self.__N + 1] = val
        self.__N += 1
        self.__heapifySwim(self.__N)


    # 删除最大的元素
    def delMAXVal(self):
        maxVal = self.__pqueue[1]
        self.__exch(1, self.__N)
        self.__N -= 1
        self.__pqueue[self.__N + 1] = None
        self.__heapifySink(1)

        return maxVal


    # 优先队列的大小
    def size(self):
        return self.__N


    # 判断优先队列是否为空
    def isEmpty(self):
        return self.__N == 0




if __name__ == '__main__':
    p = pQ()
    MAXN = 100
    # 优先队列容量 100
    p.init(MAXN)

    # 随机插入 0~500 的数字 100 个
    for i in range(MAXN):
        p.insert(random.randint(0,500))

    # 打印出最后排序堆排序结果
    for i in range(MAXN):
        print("No{} : {}".format(i+1,p.delMAXVal()))