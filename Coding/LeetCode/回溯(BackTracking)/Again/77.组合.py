#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k :
            return[] 
        res = []
        ans = []
        def Recursive(ans,i:int):
            if k == len(ans):
                res.append(ans[:])
                return
            if i > n:
                return 
            #选择当前数字
            ans.append(i)
            Recursive(ans,i+1)
            ans.pop()
            #不选当前数字
            Recursive(ans,i+1) 

        Recursive(ans,1)
        return res
# @lc code=end
s =Solution()
print(s.combine(4,2))

