#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
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
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)

        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if M[i][j]==1:
                    uf.union(i,j)
                    
        return uf.getCount()
# @lc code=end

