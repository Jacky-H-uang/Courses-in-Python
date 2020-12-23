# Created By Jacky on 2020/12/23


"""
选择排序的代码
"""

def select_sorting(Arr):
    N = len(Arr)
    for i in range(N):
        min_index = i
        for j in range(i+1,N):
            if Arr[min_index] > Arr[j]:
                min_index = j

        Arr[i] , Arr[min_index] = Arr[min_index] , Arr[i]


if __name__ == '__main__':
    Arr = [1,111,12,0,-9,0,-13,94]
    select_sorting(Arr)
    print(Arr)