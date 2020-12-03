# Created By Jacky on 2020/12/3


from Algorithm_Courses.Greedy_Algorithm.Prim.Edge import *
from Algorithm_Courses.Greedy_Algorithm.Prim.EdgeWeightGraph import *
import heapq
from queue import PriorityQueue as PQ
import sys


# Prim 算法的 MST
class PrimMST:
    def __init__(self,G):
        self.G = G
        self.edgeTo = [Edge] * G.V()         # Edge[] 距离树最近的边
        self.distTo = [0.0] * G.V()          # distTo[w] = edgeTo[w].weight()
        self.marked = [False] * G.V()        # bool[] 如果 v 在树中则为 True
        self.pq = PQ(G.V())                  # 优先队列来存储距离

        for v in range(G.V()):
            self.distTo[v] = sys.maxsize

        self.distTo[0] = 0.0
        self.pq.put((0,0.0))

        while not pq.isEmpty():
            self.visit(G,self.pq.get()[1])
            pq.delMAXVal()

    # 访问结点
    def visit(self,G,v):
        self.marked[v] = True
        for e in G.adj(v):
            w = e.other()
            if self.marked[w] == True:  continue
            if e.weight() < self.distTo[w]:
                self.edgeTo[w] = e                  # 记录更近的点
                self.distTo[w] = e.weight()         # 记录更近的边的权值

                # 如果这条边已经存在，就更新它的最短的距离
                pass
