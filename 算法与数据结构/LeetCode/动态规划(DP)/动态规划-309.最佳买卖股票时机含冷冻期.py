from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if not length:
            return 0

        '''
        dp_0 表示第i天持有股票
        dp_1 表示第i天不持有股票 处于冷冻期
        dp_2 表示第i天不持有股票 不处于冷冻期
        '''
        dp_0 = -prices[0]
        dp_1 = 0
        dp_2 = 0

        for i in range(1,length):
            #第i天持有股票 
            #1.可能是i-1天持有股票 i天不进行操作
            #2.可能是i-1天不持有股票，不处于冷冻期，i天买入
            new_dp_0 = max(dp_0,dp_2-prices[i])
            #第i天不持有股票 处于冷冻期 表明第i天卖出股票
            new_dp_1 = dp_0 + prices[i]
            #第i天不持有股票 不处于冷冻期 表明i-1没有买入 没有卖出
            new_dp_2 = max(dp_1,dp_2)
            dp_0 = new_dp_0
            dp_1 = new_dp_1
            dp_2 = new_dp_2

        return max(dp_1,dp_2)