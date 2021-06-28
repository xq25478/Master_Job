#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 5
        res = 0

        while i <= n:
            res+= n//i
            i*=5
        return res
# @lc code=end

