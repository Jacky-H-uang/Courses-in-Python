# Created By Jacky on 2020/12/24



"""
复习快速排序
分三步
    1. partition
    2. 快排分治
    3. 排序
"""

import random

# pivot 来利用 Lumuto 做划分
def partition(Arr , p , r):
    x = Arr[r]
    i = p - 1
    for j in range(p,r):
        if Arr[j] <= x:
            i = i + 1
            Arr[i] , Arr[j] = Arr[j] , Arr[i]
    Arr[i+1] , Arr[r] = Arr[r] , Arr[i+1]

    return i + 1


# 快排归并
def sort(Arr , L , R):
    if L < R:
        q = partition(Arr , L , R)
        sort(Arr , L , q - 1)
        sort(Arr , q + 1 , R)


# 快速排序
def quick_sorting(Arr):
    sort(Arr , 0 , len(Arr) - 1)



# Test
if __name__ == '__main__':
    Arr = list()
    for i in range(20):
        Arr.append(random.randint(-100,100))
    print(Arr)
    quick_sorting(Arr)
    print(Arr)