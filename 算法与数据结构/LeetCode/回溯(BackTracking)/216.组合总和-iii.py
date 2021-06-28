#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backTrack(target,cnt,cur,pre):
            if target == 0 and cnt == k:
                ret.append(ans[:])
                return
            if target > 0 and cnt == k:
                return
        
            if pre < cur and (k-cnt)*cur <= target and 1 <= cur <= 9:
                ans.append(cur)
                backTrack(target-cur,cnt+1,cur+1,cur)
                ans.pop()

            if cur < n :
                backTrack(target,cnt,cur+1,pre)
            
        ret = []
        ans = []
        backTrack(n,0,1,0)
        return ret
# @lc code=end
s = Solution()
print(s.combinationSum3(2,18))
