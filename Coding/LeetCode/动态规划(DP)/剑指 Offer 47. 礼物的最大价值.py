from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        if not grid[0]:return 0

        rows = len(grid)
        cols = len(grid[0])
        dp = [0 for i in grid[0]] #初始化
        for i in range(cols):
            dp[i] = grid[0][0] if i == 0 else dp[i-1] + grid[0][i] 

        #辅助数组
        for i in range(1,rows):
            for j in range(cols):
               dp[j] = dp[j] + grid[i][j] if j == 0 else grid[i][j] + max(dp[j],dp[j-1])

        #反向遍历
        return dp[-1]
s = Solution()
print(s.maxValue([[1,3,1],[1,5,1],[4,2,1]]))