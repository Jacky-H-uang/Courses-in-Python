# Created By Jacky on 2020/12/11

import datetime

"""
考拉兹猜想（Collatz conjecture）是数学中最引人注目的难题之一
该猜想首先由德国数学家Lothar Collatz在1937年提出：
无论选择什么正整数作为开始，通过应用上述的规则，该算法最终会在有限步骤内结束。
"""
def Collatz(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2           # op 1
        else:
            n = n * 3 + 1       # op 2

    print("Function Done!!!")

if __name__ == '__main__':
    start = datetime.datetime.now()
    Collatz(1010101010101000909023102930452345719543691657326756134751132838134971407134758235512435414)
    end = datetime.datetime.now()

    print("{} s".format((end-start).seconds))