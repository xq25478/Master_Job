#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        p = 1
        n = len(nums)

        while p < n:
            if nums[left] != nums[p]:
                nums[left+1] = nums[p]
                left += 1
            p += 1
        return left + 1
# @lc code=end


