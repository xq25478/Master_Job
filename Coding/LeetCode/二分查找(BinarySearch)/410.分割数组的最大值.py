#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
from typing import List
# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
#         二分查找 属实经典嗷
#         left,right=max(nums),sum(nums)
#         while left < right:
#             mid = left + (right-left)//2
#             s,cnt = 0,1
#             for i in nums:
#                 if s + i > mid:
#                     cnt += 1
#                     s = i
#                 else:
#                     s += i
#             if cnt <= m:
#                 right = mid 
#             else:
#                 left = mid + 1
#         return left
#         动态规划
        n = len(nums)
        #dp(i,j)表示前i个数分成j段的和的最大值的最小值
        dp = [ [float('inf')]*(m+1) for _ in range(n+1) ] 
        dp[0][0] = 0

        sub = [0]*(n+1)
        for i in range(n):
            sub[i+1] = sub[i] + nums[i]

        for i in range(m+1):dp[0][i] = 0

        for i in range(n+1):
            for j in range(1,min(i,m)+1):
                for k in range(i+1):
                    dp[i][j] = min(dp[i][j],max(dp[k-1][j-1],sub[i]-sub[k-1]))
        return dp[n][m]

# @lc code=end
s = Solution()
print(s.splitArray([1,2,11,8,15,7,1,6],3))

