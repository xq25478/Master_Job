class Solution:
    def cuttingRope(self, n: int) -> int:

        dp = [1]*(n+1)
        dp[2] = 1
        dp[1] = 1

        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j*dp[i-j],j*(i-j))

        return dp[-1]