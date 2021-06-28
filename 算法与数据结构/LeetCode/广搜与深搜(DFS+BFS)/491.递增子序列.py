#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
from typing import List
# @lc code=start
class Solution:
    #方法1 回溯
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(ans,idx):
            if idx == n:
                if len(ans) > 1:
                    ret.append(ans[:])
                return 

            if not ans or nums[idx] >= ans[-1]:#合适且要
                ans.append(nums[idx])
                dfs(ans,idx+1)
                ans.pop()

            if not ans or nums[idx]!=ans[-1]:
                dfs(ans,idx+1)  #选择不要 无论是否合适

        ret = []
        n = len(nums)

        dfs([],0)
        return ret
# @lc code=end
s = Solution()
print(s.findSubsequences([1,1,1,1,1]))
