#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        n = len(candidates)
        candidates.sort()
        min_value = candidates[0]

        def backTrack(candidates,target,index):
            if target == 0: #结束条件刚好为0
                res.append(ans[:]) #在这里去重
                return

            for i in range(index,n):
                if target < min_value or target-candidates[i] < 0 :#剪枝加速
                    return  
                if i > index and candidates[i] == candidates[i-1]:#加入循环游标去重
                    continue
                ans.append(candidates[i])
                backTrack(candidates,target-candidates[i],i)
                ans.pop()
                
        backTrack(candidates,target,0)
        return res
s = Solution()
print(s.combinationSum([2,3,5],8))
# @lc code=end