#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:return True
        n = len(s)
        if n & 1 == 1:return False

        s1 = []
        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                s1.append(s[i])
            else:
                if s1 and ( ( s1[-1] == '(' and s[i] == ')' ) \
                       or   ( s1[-1] == '[' and s[i] == ']' )  \
                       or   ( s1[-1] == '{' and s[i] == '}' ) ):
                    s1.pop()
                else:
                    return False

        return True if not s1 else False

# @lc code=end