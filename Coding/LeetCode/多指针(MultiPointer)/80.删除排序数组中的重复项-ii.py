#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        cnt = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                cnt += 1
            else:
                cnt =  1
            if cnt < 3:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left+1
# @lc code=end
s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))

