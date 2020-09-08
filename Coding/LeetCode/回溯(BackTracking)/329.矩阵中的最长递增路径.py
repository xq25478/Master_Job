#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
from typing import List
import functools
# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 回溯法 无法通过 实质是枚举 太过耗时
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        def getNeightbour(m,n):
            res = []
            if m > 0:
                res.append((m-1,n))
            if n > 0:
                res.append((m,n-1))
            if m < rows-1:
                res.append((m+1,n))
            if n < cols-1:
                res.append((m,n+1))

            return res

        @functools.lru_cache(maxsize=None)
        def backTrack(i,j):
            v = matrix[i][j]
            ls = [backTrack(r,c) for r,c in getNeightbour(i,j) if matrix[r][c] > v ]
            return 1 + (max(ls) if ls else 0)
            
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans,backTrack(i,j))
        return ans
        
# @lc code=end
s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))

