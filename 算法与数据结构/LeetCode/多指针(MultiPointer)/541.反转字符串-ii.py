#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)

        def _reverse(left,right,s):
            while left < right:
                s[left],s[right] = s[right],s[left]
                left  += 1
                right -= 1
                
        for i in range(0,n,2*k):
            left,right = (i,n-1) if n-i < k else (i,i+k-1)
            _reverse(left,right,s)
        s = ''.join(s)
        return s
# @lc code=end

