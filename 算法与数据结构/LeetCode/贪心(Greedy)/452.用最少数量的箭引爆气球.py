#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
            
        points.sort(key=lambda x:x[1])
        cur = points[0][1]
        cnt = 1
 
        for point in points:
            if point[0] > cur:
                cur = point[1]
                cnt += 1

        return cnt
# @lc code=end

