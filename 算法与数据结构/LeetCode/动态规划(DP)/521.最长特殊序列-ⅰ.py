#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        '''
        思路 简单的动态规划
        '''
        len_a = len(a)
        len_b = len(b)
        if len_a != len_b:
            return max(len_a,len_b)
        
        n = len_a
        dp = 0
            
        for i in range(1,n+1):
            if a[i-1] == b[i-1]:
                dp = 0 if dp == 0 else dp+1

            else:
                dp += 1

        return -1 if dp == 0 else dp    
# @lc code=end
s = Solution()
print(s.findLUSlength('aaa','bbb'))