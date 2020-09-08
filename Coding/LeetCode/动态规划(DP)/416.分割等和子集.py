#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from typing import List
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s%2 == 1:
            return False

        #转换为背包问题
        amonut = s // 2

        dp = [False]*(amonut+1)
        dp[0] = True
    
        #coin 在前 否则出现重复情况
        for coin in nums:
            for i in range(amonut,-1,-1):#由于每个数字只能使用一次 反向
                if i < coin:
                    continue
                dp[i] = dp[i] or dp[i-coin] #dp[]

        return dp[amonut]
    
# @lc code=end
s = Solution()
print(s.canPartition([1,2,5]))

