#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List
from copy import deepcopy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        ans = []
        def backTrack(nums,i):
            if i == len(nums):
                res.append(ans[:]) #deepcopy
                return 
            for j in range(len(nums)):
                if nums[j] in ans:
                    continue
                ans.append(nums[j])
                backTrack(nums,i+1)
                ans.pop()
        backTrack(nums,0)
        return res
s = Solution()
print(s.permute([1,2,3]))
# @lc code=end

