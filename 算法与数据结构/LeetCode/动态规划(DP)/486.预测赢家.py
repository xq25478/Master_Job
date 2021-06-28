#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#
from typing import List
# @lc code=start
class Solution:
    #斜着DP
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        #dp[i][j]表示 dp[i][j][0]表示先手 dp[i][j][1]表示后手
        dp = [[[0,0] for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i][0] = nums[i]
            dp[i][i][1] = 0

        for l in range(1,n): #每一轮遍历x轴的起点 
            for k in range(l,n):
                j = k 
                i = k - l
                left  = nums[i] + dp[i+1][j][1]
                right = nums[j] + dp[i][j-1][1]
                if left >= right:
                    dp[i][j][0] = left
                    dp[i][j][1] =  dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] =  dp[i][j-1][0]

        return dp[0][n-1][0] >= dp[0][n-1][1]
# @lc code=end
s = Solution()
print(s.PredictTheWinner([1,5,2]))

