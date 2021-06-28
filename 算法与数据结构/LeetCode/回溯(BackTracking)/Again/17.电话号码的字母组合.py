#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        alpha = [['a','b','c'],
                 ['d','e','f'],
                 ['g','h','i'],
                 ['j','k','l'],
                 ['m','n','o'],
                 ['p','q','r','s'],
                 ['t','u','v'],
                 ['w','x','y','z']
                ]
        res = []
        ans = []
        def backTrack(ans,digits,i):
            #第一步 写回溯结束条件
            if i == len(digits):
                res.append(''.join(ans))
                return 
            index = int(digits[i])-2
            for j in range(len(alpha[index])):
                ans.append(alpha[index][j])#每一步都由N种选择 故需要通过for循环来完成每次选择
                backTrack(ans,digits,i+1)
                ans.pop()
        backTrack(ans,digits,0)
        return res
s = Solution()
print(s.letterCombinations('23')) 
# @lc code=end

