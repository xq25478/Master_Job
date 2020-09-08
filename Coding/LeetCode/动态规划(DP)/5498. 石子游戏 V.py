'''
题目描述:
几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。

游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；
Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，
Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让
 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。

只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。

返回 Alice 能够获得的最大分数 。

'''
from typing import List
class Solution:
    #前缀和+记忆化DFS(或者区间DP)
    def stoneGameV(self, stoneValue: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(maxsize = None)
        def dfs(i,j):
            if i == j - 1:
                return 0
            
            res = 0
            for k in range(i+1,j):
                left = pre[k]-pre[i]
                right = pre[j]-pre[k]

                if left > right:
                    res = max(res,dfs(k,j)+right)
                elif left < right:
                    res = max(res,dfs(i,k)+left)
                else:
                    res =  max(res,max(dfs(i,k),dfs(k,j))+left )
            return res

        n = len(stoneValue)
        pre = [0]*(n+1)
        for i in range(1,n+1):
            pre[i] = pre[i-1] + stoneValue[i-1]

        return dfs(0,n)
        