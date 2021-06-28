#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <=1:
            return 0

        dp_0 = 0
        dp_1 = float('-inf')
        
        #3. state change
        for i in range(0,n):
            new_dp_0 = max(dp_0,dp_1+prices[i])
            new_dp_1 = max(dp_1,dp_0-prices[i]-fee)
            dp_0,dp_1 = new_dp_0,new_dp_1
        #  output
        #return max(dp[n-1][0],dp[n-1][1])
        return max(dp_0,dp_1)
# @lc code=end

