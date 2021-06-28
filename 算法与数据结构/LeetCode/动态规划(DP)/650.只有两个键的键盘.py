#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        
        dp = [float('inf')]*(n+1)

        dp[0] = float('inf')
        dp[1] = 0
        
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                if i%j == 0:
                    dp[i] = min(dp[i],dp[j] + i//j)
        return dp[-1]
# @lc code=end
s = Solution()
print(s.minSteps(3))

