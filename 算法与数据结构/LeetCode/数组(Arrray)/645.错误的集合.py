#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
from typing import List
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)  
        dup = 0
        miss = 0
        for i in range(n):
            if nums[abs(nums[i])-1] < 0:
                dup = abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= -1

        for i in range(n):
            if nums[i] > 0:
                miss = i + 1
        return [dup,miss]
# @lc code=end

