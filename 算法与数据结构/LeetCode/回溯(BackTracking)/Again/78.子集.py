#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        ans = []
        def Recursive(ans,i:int):
            if i >=  len(nums):
                res.append(ans[:])
                return
            #选择当前数字
            ans.append(nums[i])
            Recursive(ans,i+1)
            ans.pop()
            #不选当前数字
            Recursive(ans,i+1) 
        Recursive(ans,0)
        return res
s =Solution()
print(s.subsets([1,2,3]))
# @lc code=end

