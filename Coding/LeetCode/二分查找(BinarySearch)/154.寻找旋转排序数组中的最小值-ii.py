#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            pivot = left + (right-left)//2
            if nums[right] > nums[pivot]:
                right = pivot
            elif nums[right] < nums[pivot]:
                left = pivot + 1
            else:
                right -= 1
        return nums[left]
# @lc code=end
s = Solution()
print(s.findMin([1,3,5]))

