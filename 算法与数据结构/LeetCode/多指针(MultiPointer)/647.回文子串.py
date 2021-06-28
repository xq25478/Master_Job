#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        #双指针算法
        def center_1(idx1)->int:
            cnt = 1
            i = idx1 - 1
            j = idx1 + 1
            while i >= 0 and j < n and s[i]==s[j]:
                cnt += 1
                i -= 1
                j += 1
            return cnt

        def center_2(idx1,idx2):
            cnt = 0
            i = idx1 
            j = idx2 
            while i >= 0 and j < n and s[i]==s[j]:
                cnt += 1
                i -= 1
                j += 1

            return cnt
            
        n = len(s)
        if n == 0:return 0
        if n == 1:return 1

        res = 0
        for i in range(n):
            res += center_1(i)
            if i < n-1:
                res += center_2(i,i+1)
        return res
        
# @lc code=end

