#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
from typing import List
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def checkSpeed(speed:int,H:int)->int:
            cnt = 0
            for pile in piles:
               a = pile // speed
               b = 1 if pile % speed else 0
               cnt += (a + b)
            return cnt <= H

        piles.sort()
        right = piles[-1]+1
        left = 1
        while left < right:
            mid = left + (right-left)//2
            val = checkSpeed(mid,H)
            if val:
                right = mid
            else:
                left = mid + 1

        return left
# @lc code=end
s = Solution()
print(s.minEatingSpeed([30,11,23,4,20],5))