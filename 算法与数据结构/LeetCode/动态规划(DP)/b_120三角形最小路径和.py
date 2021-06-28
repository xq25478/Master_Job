from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        length = len(triangle)
        dp = [0]*length
        dp[0] = triangle[0][0]

        for i in range(1,length):
            #j = i
            dp[i] = dp[i-1] + triangle[i][i]
            #j=1:i-1
            for j in range(i-1,0,-1):
                dp[j] = min(dp[j],dp[j-1]) + triangle[i][j]
            #j =0
            dp[0] += triangle[i][0]
        return min(dp)

s = Solution()
print(s.minimumTotal(
[[2],[3,4],[6,5,7],[4,1,8,3]]))