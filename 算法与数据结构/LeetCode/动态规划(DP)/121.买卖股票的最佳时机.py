#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1:
            return 0

        #1. DP Table define dp[i][k] 
        #表示第i天在持有股票(k=1)或者不持有股票(k=0)下的获得的利润
        #dp = [[0]*n for _ in range(n)]

        #2. base case
        #dp[0][0] = 0
        #dp[0][1] = -prices[0]
        dp_0 = 0
        dp_1 = -prices[0]

        #3. state change
        for i in range(1,n):
            #dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            #dp[i][1] = max(dp[i-1][1],-prices[i]) # 正确
            new_dp_0 = max(dp_0,dp_1+prices[i])
            new_dp_1 = max(dp_1,-prices[i])
            # dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i]) 错误 
            #因为本题目当中只支持1次交易 所以利润一定是-price[i]
            dp_0,dp_1 = new_dp_0,new_dp_1
        #  output
        #return max(dp[n-1][0],dp[n-1][1])
        return max(dp_0,dp_1)

# @lc code=end

