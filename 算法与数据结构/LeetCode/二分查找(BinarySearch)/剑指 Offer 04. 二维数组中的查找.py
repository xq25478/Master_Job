'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的
一个二维数组和一个整数，判断数组中是否含有该整数。
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
'''
from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        #思路1 二分查找
        if len(matrix) == 0: return False 
        if not matrix[0]:return False

        rows = len(matrix)
        cols = len(matrix[0])

        while 0<= start[0] < rows and 0 <= start[1] < cols:
            if matrix[start[0]][start[1]] == target:
                return True
            elif matrix[start[0]][start[1]] > target:
                start[1] -=1
            else:
                start[0] +=1
        return False

s = Solution()
print(s.findNumberIn2DArray(
[
[1 ,2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]
]
,15))