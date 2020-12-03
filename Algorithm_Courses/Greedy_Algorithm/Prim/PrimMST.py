# Created By Jacky on 2020/12/3


from Algorithm_Courses.Greedy_Algorithm.Prim.Edge import *
from Algorithm_Courses.Greedy_Algorithm.Prim.EdgeWeightGraph import *
import heapq
from queue import PriorityQueue as PQ
import sys


# Prim �㷨�� MST
class PrimMST:
    def __init__(self,G):
        self.G = G
        self.edgeTo = [Edge] * G.V()         # Edge[] ����������ı�
        self.distTo = [0.0] * G.V()          # distTo[w] = edgeTo[w].weight()
        self.marked = [False] * G.V()        # bool[] ��� v ��������Ϊ True
        self.pq = PQ(G.V())                  # ���ȶ������洢����

        for v in range(G.V()):
            self.distTo[v] = sys.maxsize

        self.distTo[0] = 0.0
        self.pq.put((0,0.0))

        while not pq.isEmpty():
            self.visit(G,self.pq.get()[1])
            pq.delMAXVal()

    # ���ʽ��
    def visit(self,G,v):
        self.marked[v] = True
        for e in G.adj(v):
            w = e.other()
            if self.marked[w] == True:  continue
            if e.weight() < self.distTo[w]:
                self.edgeTo[w] = e                  # ��¼�����ĵ�
                self.distTo[w] = e.weight()         # ��¼�����ıߵ�Ȩֵ

                # ����������Ѿ����ڣ��͸���������̵ľ���
                pass
