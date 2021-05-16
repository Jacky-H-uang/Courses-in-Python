# Created By Jacky on 2021/4/28


import numpy as np

def gauss_seidel(A,b,k,error):
    n = len(A)
    Aux = A             # 辅助矩阵
    x = np.zeros(n)
    cnt = 0
    for time in range(k):
        compare_x = x.copy()        # 记录上一次迭代的结果来更好比较误差
        for i in range(n):
            cur = 0.0
            for j in range(n):
                if i == j:  continue
                cur += (-Aux[i,j]) * x[j]
            x[i] = (cur + b[i,0]) / Aux[i,i]
        # print("迭代第 " + str(time+1) + " 次得到 x: ")
        cnt += 1
        # print(x)

        # 判断误差 小于error的时候为收敛
        error_x = 0
        for p in range(n):
            error_x = max(abs(compare_x[p] - x[p]),error_x)
        if error_x < error:
            break
    # print("\n最终收敛的结果 : ")
    # print(x)

    return cnt , x

if __name__ == '__main__':
    A = np.mat([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
    b = np.mat([6,25,-11,15]).T
    gauss_seidel(A,b,100,0.0000001)
