# Created By Jacky on 2020/12/3

from Algorithm_Courses.Greedy_Algorithm.Prim.Edge import *


# 加权无向图
class EdgeWeightedGraph:
    def __init__(self,V,E,adj):
        self.V = int(V)             # 顶点总数
        self.E = int(E)             # 边的总数
        self.adj = dict(adj)        # 邻接表

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
