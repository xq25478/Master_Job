#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
from typing import List
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =[0]*(amount+1) #dp[i]表示凑合成金额为i的硬币组合数
        dp[0] = 1

        #正确写法 将coin放在外面
        for coin in coins: #状态1 
            for i in range(1,amount+1):#状态2 
                if i < coin:
                    continue
                dp[i] += dp[i-coin]

        return dp[amount]
# @lc code=end
s = Solution()
print(s.change(5,[1,2,5]))

