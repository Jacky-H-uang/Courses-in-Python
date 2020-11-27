# Created By Jacky on 2020/11/27

"""
                                        双蛋问题
Background: 现在城市中有一幢高楼 , 楼高为 n 层。一天一个工程队来测试楼层的安全性 , 采用了一种扔鸡蛋的方法。
            已知这个楼层的安全指标是找到楼层的临界楼层 , 在临界楼层以下的扔鸡蛋都不会碎掉 , 而在临界楼层以上的
            楼层扔鸡蛋都会碎掉。现在工程队想找出这个临界楼层时需要扔鸡蛋的最小次数。

Input : n 楼层高度 , m 个鸡蛋。
Output : 找到临界楼层且扔鸡蛋的最小次数。

-- 我将结果也写到文件(result.txt)里面备份
"""


import sys

# 利用动态规划
class TwoEggsProblem(object):
    # 初始化 楼层 n 和鸡蛋数 m
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.dp = [[0] * (self.m + 1) for _ in range(self.n+1)]

        # Boundary 处理 ：
        for i in range(1,self.n+1):
            self.dp[i][1] = i
        for i in range(1,self.m+1):
            self.dp[1][i] = 1


    # Dynamic Programming 解决
    def Solution(self):
        # 状态转移方程 : dp(i,j) = min{dp(i,j) , max{dp(k-1,j-1) , dp(i-k,j)} }
        for i in range(2,self.n+1):
            for j in range(2,self.m+1):
                temp = sys.maxsize

                # 枚举 1 ~ i 层从每一层开始测试的最小抛的次数
                for k in range(1,i):
                    temp = min(temp,max(self.dp[k-1][j-1] , self.dp[i-k][j]) + 1)
                self.dp[i][j] = temp

        return self.dp[self.n][self.m]


    # 返回结果
    def retAns(self):
        return self.Solution()




# 测试
if __name__ == '__main__':
    n = int(input("楼层的高度 : "))
    m = int(input("鸡蛋的数量 : "))

    # 写入文件存储
    file = open('result.txt', 'w')

    file.write(" 规划表如下")
    file.write("\n\t\t\t\t\t         鸡蛋数量")
    file.write("\n\t\t\t")

    print(" 规划表如下：")
    print("\n\t\t\t\t\t         鸡蛋数量")
    print("\t\t\t",end=" ")
    for i in range(1,m+1):
        file.write("  {}  ".format(i))
        print("{}".format(i) ,end="    ")

    file.write("\n")
    print("\n")



    for i in range(1,n+1):
        file.write("{} floor :     ".format(i))
        print("{} floor : ".format(i), end="   ")
        for j in range(1,m+1):
            t = TwoEggsProblem(i,j)
            file.write("{}    ".format(t.retAns()))
            print(t.retAns(),end="    ")
        file.write("\n")
        print("\n")