#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = [str(x) for x in digits]
        c = list(str(int(''.join(b))+1))
        return [int(x) for x in c]
# # @lc code=end
# s = Solution()
# print(s.plusOne([9,9,9]))
