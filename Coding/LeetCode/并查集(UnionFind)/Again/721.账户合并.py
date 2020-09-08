#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        import collections
        uf = UnionFind(10001)
        em_to_name = {}
        em_to_id = {}
        i = 0 

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                uf.union(em_to_id[acc[1]],em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[uf.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]
# @lc code=end