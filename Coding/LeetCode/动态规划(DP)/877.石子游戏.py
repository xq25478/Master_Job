#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#
from typing import List
# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[0,0] for i in range(n)] for j in range(n)]
        #dp[i][j]表示从i...j之间胜负结果dp[i][j][0]表示先手
        #dp[i][j][1]表示后手    
    
        #base case
        for i in range(n):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0
        
        #
        for l in range(2,n+1):
            for i in range(n-l+1):
                j = l + i -1
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]

                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]

        return bool(dp[0][n-1][0]-dp[0][n-1][1])
# @lc code=end
s = Solution()
print(s.stoneGame([3,7,2,3]))

