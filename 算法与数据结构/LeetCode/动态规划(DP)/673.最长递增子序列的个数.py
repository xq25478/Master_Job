#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
from typing import List
# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*(n)#num[i]结尾的最长序列
        cnt = [1]*n#num[i]结尾的最长序列个数

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j]+1:
                        cnt[i] += cnt[j]
                    else:
                         #cnt[i] = cnt[j]
                         cnt[i] = cnt[j] if dp[i] < dp[j]+1 else cnt[i]
                    dp[i] = max(dp[i],dp[j]+1)

        max_seq = max(dp)
        res = 0
        for i in range(0,n):
            if dp[i] == max_seq:
                res += cnt[i]
        return res
# @lc code=end
s = Solution()
#print(s.findNumberOfLIS([2,2,2,2,2]))
#print(s.findNumberOfLIS([1,3,5,4,7]))
print(s.findNumberOfLIS([1,2,3,1,2,3,1,2,3]))
