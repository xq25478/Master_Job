from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
        
s = Solution()
print(s.numTrees(3))