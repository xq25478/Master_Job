#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        ans = []

        def backTrack(num_1,num_2):
            if len(ans) == 2*n:
                res.append(''.join(ans[:]))
                return 

            if num_1 > num_2:
                return

            if num_1 >= 1:
                ans.append('(')
                backTrack(num_1-1,num_2)
                ans.pop()

            if num_2 >= 1:
                ans.append(')')
                backTrack(num_1,num_2-1)
                ans.pop()

        backTrack(n,n)
        return res
# @lc code=end
s = Solution()
print(s.generateParenthesis(5))