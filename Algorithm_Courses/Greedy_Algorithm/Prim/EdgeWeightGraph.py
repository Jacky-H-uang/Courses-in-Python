# Created By Jacky on 2020/12/3

from Algorithm_Courses.Greedy_Algorithm.Prim.Edge import *


# ��Ȩ����ͼ
class EdgeWeightedGraph:
    def __init__(self,V,E,adj):
        self.V = int(V)             # ��������
        self.E = int(E)             # �ߵ�����
        self.adj = dict(adj)        # �ڽӱ�

        for v in range(self.V):
            adj[v] = list()

    def V(self):
        return self.V

    def E(self):
        return self.E

    def addEdge(self,e):
        v = e.either()
        w = e.other(v)
        adj[v].append(e)
        adj[w].append(e)


    def adj(self,v):
        return adj[v]


    def edges(self):
        b = list()
        for v in range(self.V):
            for e in self.adj[v]:
                if e.other(v) > v:      b.append(e)

        return b
