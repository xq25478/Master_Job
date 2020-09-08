#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums: return False
        def helper(nums):
            if len(nums) == 1: return abs(nums[0]-24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        newnums = [nums[k] for k in range(len(nums)) if i != k != j]
                        if helper(newnums + [nums[i]+nums[j]]): return True
                        if helper(newnums + [nums[i]-nums[j]]): return True
                        if helper(newnums + [nums[i]*nums[j]]): return True
                        if nums[j] != 0 and helper(newnums + [nums[i]/nums[j]]): return True 
            return False
        return helper(nums)   
# @lc code=end

