#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])

        res = []
        w = col
        h = row
        index = 0
        while h > 0 and w > 0:
            start_x = start_y = index 
            for i in range(start_y,w+start_y):
                res.append(matrix[start_x][i])

            for i in range(start_x+1,start_x+h-1):
                #[1,3)
                res.append(matrix[i][w+start_y-1])
            if h > 1:
                for i in range(start_x+w-1,start_x-1,-1):
                    res.append(matrix[h+start_x-1][i])
            if w > 1:
                for i in range(start_x+h-2,start_x,-1):
                    res.append(matrix[i][start_y])
            h = h-2
            w = w-2
            index += 1
        return res
# @lc code=end
s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

