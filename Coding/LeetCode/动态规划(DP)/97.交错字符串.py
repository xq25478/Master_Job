#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 动态规划解决
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [ [False]*(len(s2)+1) for _ in range(len(s1)+1)] #未采用滚动数组优化
        dp[0][0] = True
        #dp[i][j]表示s1前i个元素s2前j个元素能否构成s3前i+j个元素
        #若s1[i] = s3[i+j]
        #若s2[j] = s3[i+j]
        len1 = len(s1)
        len2 = len(s2)
        fn = [False]*(len2+1) #采用滚动数组优化
        fn[0] = True
        for i in range(len1+1):
            for j in range(len2+1):
                if i > 0:
                    fn[j] = fn[j]  and s1[i-1] == s3[i+j-1]
                    #dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[i+j-1]) #未采用滚动数组优化
                if j > 0:
                    fn[j] = fn[j] or (fn[j-1]  and s2[j-1] == s3[i+j-1])
                    #dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[i+j-1]) #未采用滚动数组优化
                
        return fn[len2]
        #return dp[len1][len2]

# @lc code=end
s = Solution()
print(s.isInterleave('aabcc','dbbca','aadbbcbcac'))

