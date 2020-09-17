#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(ans,sum)
        return ans
# @lc code=end
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
