# Created By Jacky on 2020/12/3



# ������Ȩ�ߵ����ݽṹ
class Edge:
    def __init__(self,v,w,weight):
        self.v = int(v)                     # ����֮һ
        self.w = int(w)                     # ��һ������
        self.weight = float(weight)         # �ߵ�Ȩ��

    def weight(self):
        return self.weight

    def either(self):
        return self.v

    def other(self,vertex):
        if vertex == self.v:        return self.w
        elif vertex == self.w:      return self.v
        else:                       print("Inconsistent Edge")


    def compareTo(self,that):
        if self.weight() < that.weight():       return -1
        elif self.weight() > that.weight():     return 1
        else:                                   return 0

    def printEdge(self):
        print("{}-{} {}".format(self.v,self.w,self.weight))