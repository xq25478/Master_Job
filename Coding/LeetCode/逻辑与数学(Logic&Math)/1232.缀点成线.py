#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
from typing import List
# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        if n < 3:
            return True

        for i in range(1,n-1):
            x1 = coordinates[i-1][0]
            y1 = coordinates[i-1][1]
            x2 = coordinates[i][0]
            y2 = coordinates[i][1]
            x3 = coordinates[i+1][0]
            y3 = coordinates[i+1][1]

            if (y2-y1)*(x3-x2)!=(y3-y2)*(x2-x1):
                return False
                
        return True
# @lc code=end

