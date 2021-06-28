#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        ptr = 0
        last = 0

        while ptr < n:
            cnt = 0
            c = s[ptr]
            i = ptr
            while i < n and c == s[i]:
                i += 1
                cnt += 1
            ptr = i 
            res += min(cnt,last)
            last = cnt
            
        return res    
# @lc code=end

