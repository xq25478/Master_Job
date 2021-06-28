from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = nums[0]
        res = dp
        for i in range(1,len(nums)):
            if dp < 0:
                dp = nums[i]
            else:
                dp = dp + nums[i]
            res = max(res,dp)
        return res
