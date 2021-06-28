#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#
from typing import List
# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        #自己的憨憨解法 高空间 高时间
        # n = len(A)
        # res = 0
        # if n < 2:
        #     return res

        # #dp init dp[i][j] 表示[A[i],A[j]]区间的A是否构成等差数列

        # dp = [[False]*n for _ in range(n)]

        # for i in range(1,n-1):
        #     if A[i-1] + A[i+1] == 2*A[i]:
        #         dp[i-1][i+1] = True
        #         res += 1

        # for i in range(n-3):
        #     for j in range(i+3,n):
        #         if dp[i][j-1] == False:
        #             dp[i][j] = False
        #         else:
        #             if A[j-2] + A[j]== 2*A[j-1]:
        #                 dp[i][j] = True   
        #                 res += 1     
        # return res
        # 官方
        #dp[i]表示a[i]之前的等差数组个数
        sum = 0
        dp = 0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1] -A[i-2]:
                dp += 1
                sum += dp
            else:
                dp = 0
        return sum
# @lc code=end
s = Solution()
print(s.numberOfArithmeticSlices([1,2,3,4,5,6]))

