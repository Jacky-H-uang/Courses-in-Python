# Created By Jacky on 2020/12/11

import datetime

"""
�����Ȳ��루Collatz conjecture������ѧ��������עĿ������֮һ
�ò��������ɵ¹���ѧ��Lothar Collatz��1937�������
����ѡ��ʲô��������Ϊ��ʼ��ͨ��Ӧ�������Ĺ��򣬸��㷨���ջ������޲����ڽ�����
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