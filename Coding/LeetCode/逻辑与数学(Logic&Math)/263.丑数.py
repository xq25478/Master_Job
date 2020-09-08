#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        
        if num < 1:
            return False

        if num == 1:
            return True
        
        while num%2 == 0:
            num = num // 2
        
        while num%3 == 0:
            num = num // 3

        while num % 5 == 0:
            num = num // 5
        
        return True if num == 1 else False
# @lc code=end

