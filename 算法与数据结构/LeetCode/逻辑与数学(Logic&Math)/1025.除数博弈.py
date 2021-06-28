#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

# @lc code=start
class Solution:
    def divisorGame(self, N: int) -> bool:
        return True if N%2 == 0 else False  
# @lc code=end
s = Solution()
print(s.divisorGame(2))

