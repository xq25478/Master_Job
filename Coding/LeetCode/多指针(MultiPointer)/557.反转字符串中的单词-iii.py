#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        def _reverse(left,right,s):
            while left < right:
                s[left],s[right] = s[right],s[left]
                left  += 1
                right -= 1
        i = 0
        while i < n:
            if s[i] != ' ':
                left = i
                if i == n-1:
                    break
                for j in range(i+1,n):
                    if s[j] == ' ' or j == n-1:
                        right = j-1 if s[j] == ' ' else j
                        _reverse(left,right,s)
                        i = j + 1
                        break
            else:
                i += 1
        return ''.join(s)

# @lc code=end
s = Solution()
print(s.reverseWords('i love u'))

