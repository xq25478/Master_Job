#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #dp[i][j]表示word1的前i个字母和word2的前j个字符所需要的最少操作数
        word1_len = len(word1)
        word2_len = len(word2)

        #状态定义
        dp = [[0]*(word2_len+1) for _ in range(word1_len+1)]

        #初始值
        for i in range(1,word1_len+1):
            dp[i][0] = i

        for i in range(1,word2_len+1):
            dp[0][i] = i
        

        for i in range(1,word1_len+1):
            for j in range(1,word2_len+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] =  min(
                                min(
                                dp[i - 1][j] + 1,
                                dp[i][j - 1] + 1),
                                dp[i-1][j-1] + 1)
                                
        return dp[word1_len][word2_len]

# @lc code=end
s = Solution()
print(s.minDistance('a','abc'))

