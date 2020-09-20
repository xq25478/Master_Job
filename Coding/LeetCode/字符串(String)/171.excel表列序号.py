#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            r += ord(s[i]) - 64
            r *= 26

        return r//26
# @lc code=end

