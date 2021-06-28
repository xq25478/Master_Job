#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)

        p1 = 0
        p2 = 0
        cnt = 0

        while p1 < l1 and p2 < l2:
            if s[p1] == t[p2]:
                cnt+=1
                p1 += 1
            p2 += 1

        return cnt == l1
# @lc code=end
s = Solution()
print(s.isSubsequence('abc','ahbgdc'))

