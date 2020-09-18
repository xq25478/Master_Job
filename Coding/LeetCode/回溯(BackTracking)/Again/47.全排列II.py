#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums.sort()
        res = []
        ans = []
        check = [False]* len(nums)
        def backTrack(nums,i):
            if i == len(nums):
                res.append(ans[:]) #deepcopy
                return 
            for j in range(len(nums)):
                if check[j] == True:
                    continue
                if j>0 and nums[j] == nums[j-1] and check[j-1] == False:
                    continue
                check[j]=True
                ans.append(nums[j])
                backTrack(nums,i+1)
                check[j]=False
                ans.pop()
        backTrack(nums,0)
        return res
# @lc code=end
s = Solution()
print(s.permuteUnique([1,2,2]))

