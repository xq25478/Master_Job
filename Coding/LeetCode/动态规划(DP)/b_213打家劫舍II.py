from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        #分为小偷不偷窃第一间房屋和小偷偷窃第一间房屋
        res = 0

        dp_0 = 0
        dp_1 = 0 #不偷窃第一号房间 所以最后一号房可偷可不偷
        for i in range(1,len(nums)):
            new_dp = max(dp_1,nums[i]+dp_0)
            dp_0 = dp_1
            dp_1= new_dp
        res = max(res,dp_1)

        dp_0 = 0
        dp_1 = nums[0] #偷窃了第一号房 最后一号房必须不能偷
        for i in range(1,len(nums)-1):
            new_dp = max(dp_1,nums[i]+dp_0)
            dp_0 = dp_1
            dp_1= new_dp
        res = max(res,dp_1)

        return res