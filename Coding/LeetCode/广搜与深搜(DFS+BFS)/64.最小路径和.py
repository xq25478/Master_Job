#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [float('inf')]*cols
        dp[0] = grid[0][0]
        for i in range(0,rows):
            for j in range(0,cols):
                if j > 0 and i > 0:
                    dp[j] = min(dp[j],dp[j-1]) + grid[i][j]
                elif i == 0 and j > 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[j] += grid[i][j]
        return dp[-1]
# @lc code=end
s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
