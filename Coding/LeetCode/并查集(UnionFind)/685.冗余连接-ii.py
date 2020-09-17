#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
"""
在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。
每一个节点只有一个父节点，除了根节点没有父节点。
输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 
和顶点 v 的边，其中 u 是 v 的一个父节点。
返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
"""
from typing import List
# @lc code=start
class UnionFind:
    def __init__(self,n):
        self.count = n  #记录连通分量
        self.fa = [i for i in range(n)]  #fa[i]表示i的父节点
        self.size = [1 for _ in range(n)]

    def find(self,x)->int:
        while x != self.fa[x]:
            self.fa[x] = self.fa[self.fa[x]]  #路径压缩
            x = self.fa[x]
        return x

    def union(self,i,j): #连通任意两个节点
        x = self.find(i)
        y = self.find(j)

        if x == y:return

        ## 路径优化
        if self.size[x] > self.size[y]: 
            self.fa[y] = x
            self.size[x] += self.size[y]
        else:
            self.fa[x] = y
            self.size[y] += self.size[x]  
        self.count -= 1

    def getCount(self):
        return self.count

    def connected(self,i,j)->bool:
        return self.find(i) == self.find(j)

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        parent = list(range(n+1))
        conflict = -1
        cycle = -1

        for i,(node1,node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) ==  uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1,node2)
                
        if conflict < 0:  #不存在双父节点 则一定存在环
            return [edges[cycle][0], edges[cycle][1]]
        else: #存在双父节点
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]
# @lc code=end

