'''
https://leetcode-cn.com/problems/wildcard-matching/
'''
from typing import List

class Solution:
    #动态规划
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False]*(n+1) for _ in range(1+m)]

        for j in range(n+1):
            if j == 0 or p[j-1] == '*':
                dp[0][j] = True
            else:
                break
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] in {s[i-1],'?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] | dp[i][j-1]
        return dp[-1][-1]