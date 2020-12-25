# Created By Jacky on 2020/12/25

"""
复习插入排序
"""

import random

def insert_sorting(Arr):
    N = len(Arr)
    for i in range(1,N):
        for j in range(i,0,-1):
            if Arr[j] < Arr[j-1]:
                Arr[j] , Arr[j-1] = Arr[j-1] , Arr[j]


# Test
if __name__ == '__main__':
    Arr = list()
    for i in range(20):
        Arr.append(random.randint(-100,100))
    print(Arr)
    insert_sorting(Arr)
    print(Arr)