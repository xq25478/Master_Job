#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        n = len(candidates)
        candidates.sort()
        visited = [False]*n

        def backTrack(candidates,target,index):
            if target == 0: #结束条件刚好为0
                res.append(ans[:]) 
                return

            for i in range(index,n):
                if  target-candidates[i] < 0 :#剪枝加速
                    return  
                if i > index and candidates[i] == candidates[i-1] and visited[i-1]==False:
                    continue
                ans.append(candidates[i])
                visited[i] = True
                backTrack(candidates,target-candidates[i],i+1)
                ans.pop()
                visited[i] = False
        backTrack(candidates,target,0)
        return res
# @lc code=end
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))
