#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x = [points[0][0],points[1][0],points[2][0]]
        y = [points[0][1],points[1][1],points[2][1]]

        if points[0] == points[1] or points[1] == points[2] or points[2] == points[0]:
            return False

        if( x[0] == x[1] and x[1]== x[2] )or (y[1] == y[2] and y[2] == y[0]):
            return False
        
        if x[1] - x[0] == 0:
            x = x[::-1]
            y = y[::-1]
            
        a = (y[1]-y[0])/(x[1]-x[0])
        b = y[1] -a* x[1]
        if a*x[2]+ b == y[2]:
            return False
        else:
            return True

# @lc code=end
s = Solution()
print(s.isBoomerang([[31,86],[2,2],[3,3]]))



