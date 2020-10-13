#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return None

        p1,cur,p2 = 0,0,n-1

        while cur <= p2:
            if nums[cur] == 0:
                nums[p1],nums[cur] = nums[cur],nums[p1]
                cur += 1
                p1 += 1
            elif nums[cur] == 2:
                nums[p2],nums[cur] = nums[cur],nums[p2]
                p2  -= 1
            else:
                cur += 1
# @lc code=end

