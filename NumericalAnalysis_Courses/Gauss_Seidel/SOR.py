# Created By Jacky on 2021/5/10



import numpy as np

def sor_function(A,b,w,k ,error = 0.000001):
    n = len(A)
    Aux = A             # 辅助矩阵
    x = np.zeros(n)
    for time in range(k):
        compare_x = x.copy()        # 记录上一次迭代的结果来更好比较误差
        x_before = x.copy()
        for i in range(n):
            cur = 0.0
            for j in range(n):
                if i == j:  continue
                cur += (-Aux[i,j]) * x[j]
            x[i] = x_before[i] * (1-w)  + w * (cur + b[i,0]) / Aux[i,i]     # 松弛参数 w
        print("迭代第 " + str(time+1) + " 次得到 x: ")
        print(x)

        # 判断误差 小于error的时候为收敛
        error_x = 0
        for p in range(n):
            error_x = max(abs(compare_x[p] - x[p]),error_x)
        if error_x < error:
            break
    print("\n最终收敛的结果 : ")
    print(x)


if __name__ == '__main__':
    A = np.mat([[-4,1,1,1],[1,-4,1,1],[1,1,-4,1],[1,1,1,-4]])
    b = np.mat([1,1,1,1]).T
    sor_function(A,b,1.25,100)