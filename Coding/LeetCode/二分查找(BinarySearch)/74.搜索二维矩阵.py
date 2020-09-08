#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #思路1 二分查找
        if len(matrix) == 0: return False 
        if not matrix[0]:return False

        rows = len(matrix)
        cols = len(matrix[0])
     
        left = 0
        right = rows*cols

        while left < right:
            mid = left + (right-left)//2
            row = mid // cols
            col = mid %  cols
            
            if matrix[row][col] == target: return True
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                right = mid           

        return False
# @lc code=end
s = Solution()
print(s.searchMatrix(
[
    [1, 3, 5, 7],
    [10,11,16,20],
    [23,30,34,50]
]    
,50))

