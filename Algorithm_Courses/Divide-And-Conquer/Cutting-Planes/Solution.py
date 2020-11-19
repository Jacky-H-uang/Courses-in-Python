# Created By Jacky on 2020/11/19

"""
Backgroud:
    平面上有很多形如 y = kx + b 的直线，他们相交很把平面切割成很多小的平面。
    现在有两个边界 y = A ， y = B (A < B) , 求若干条直线在边界中能切割成多少个平面

Input  : 若干个形如 (k , b) 的数组，每个元素代表一条直线 y = kx + b
Output : 能切割出的平面的数目
"""


import random


# 随机产生若干的(k,b)组成的列表
def creatData():
    ret = []
    for i in range(100):
        ret.append((random.randint(0,100),random.randint(0,100)))

    return ret



# 利用归并求逆序对
def CountSpliteInv(left, right, count):
    i = j = 0
    ret = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1
            # 当分解到左边和右边只有1个元素时，并且左边元素大于右边，很明显此时只有1个逆序对
            if len(left) == 1 and len(right) == 1:
                count = 1
            else:
                count += len(left) - i

    # 将数组中的剩余部分添加
    ret += left[i:]
    ret += right[j:]

    return ret, count

def CountInv(list):
    count = 0
    mid = int(len(list)/2)
    if mid == 0:
        return list, 0
    # divide
    left, leftInv = CountInv(list[:mid])
    right, rightInv = CountInv(list[mid:])

    # merge
    list, spliteInv = CountSpliteInv(left, right, count)
    count = leftInv + rightInv + spliteInv

    return list, count





# 分割平面的个数
def cuttingPlane(left , right , A):
    B = []
    for i in range(len(A)):
        # 求出左右的交点
        X = left * A[i][0] + A[i][1]
        Y = right * A[i][0] + A[i][1]
        B.append((X,Y))

    # 与边界的交点的坐标按照与 left 的交点坐标排序
    B = sorted(B,key = lambda x:x[0])

    # 将排完序的坐标重新装入数组 C 中
    C = []
    for i,j in B:
        C.append(j)

    print(A)        # 原始数组                      (k , b)
    print(B)        # 求出与左右交点，排序后的数组     (x , y)
    print(C)        # 与有边界的交点                 (y)
    reList , reCount = CountInv(C)
    return reCount + len(A) + 1



if __name__ == '__main__':
    # 生成 100 条 斜率和截距在 0 ~ 100 的直线
    ret = creatData()

    LeftB = int(input("左边界 ： "))
    RightB = int(input("右边界 ： "))

    print("{} 条直线最终在边界 {} ~ {} 切割平面数 {}: ".format(len(ret),LeftB,RightB,cuttingPlane(LeftB,RightB,ret)))