#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        hash_win= {}
        res = 0
        n = len(s)
        left = right = 0

        while right < n:
            hash_win[s[right]] = hash_win[s[right]] + 1 if \
                                 s[right] in hash_win else 1   
            #当前窗口含有重复字符串
            while hash_win[s[right]] > 1:
                hash_win[s[left]] -= 1
                left += 1
            right += 1
            res = max(res,right-left)
            
        return res
# @lc code=end
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

