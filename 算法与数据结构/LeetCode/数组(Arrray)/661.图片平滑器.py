#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
from typing import List
# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows = len(M)
        cols = len(M[0])
        ret = [[0]* cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sum = M[i][j]
                cnt = 1
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]:
                    if 0 <= dx + i < rows and 0 <= dy + j < cols:
                        sum += M[dx+i][dy+j]
                        cnt += 1
                ret[i][j] = sum // cnt

        return ret  
# @lc code=end

