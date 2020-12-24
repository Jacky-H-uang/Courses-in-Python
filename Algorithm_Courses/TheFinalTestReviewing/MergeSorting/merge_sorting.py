# Created By Jacky on 2020/12/23


"""
归并排序复习
"""


def sort(Arr , lo , hi):
    if hi <= lo:
        return
    mid = (hi+lo)//2

    sort(Arr , lo , mid)            # 左排序
    sort(Arr , mid+1 , hi)          # 右排序

    merge(Arr , lo , mid , hi)      # 归并



# 侧重点在于解决归并的部分
def merge(Arr , lo , mid , hi):
    i = lo
    j = mid + 1

    # 辅助数组
    aux = [0] * len(Arr)
    for k in range(lo,hi+1):
        aux[k] = Arr[k]

    for k in range(lo,hi+1):
        if i > mid :
            Arr[k] = aux[j]
            j += 1
        elif j > hi:
            Arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            Arr[k] = aux[j]
            j += 1
        else :
            Arr[k] = aux[i]
            i += 1



def merge_sorting(Arr):
    sort(Arr , 0 , len(Arr)-1)



# Test
if __name__ == '__main__':
    Arr = [0,1,8,-1,99,0,21,6,100,-9,43,13]
    merge_sorting(Arr)
    print(Arr)