from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp_0 = 0
        dp_1 = nums[0]
        
        #dp[i]表示偷窃房屋最大号码为i的最大收益
        for i in range(1,len(nums)):
            new_dp = max(dp_1,nums[i]+dp_0)
            dp_0 = dp_1
            dp_1= new_dp
        return dp_1