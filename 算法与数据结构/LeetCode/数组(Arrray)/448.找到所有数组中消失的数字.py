#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
from typing import List
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # hash O(n)-O(n)
        # hash = {}
        # for num in nums:
        #     hash[num] = True

        # n = len(nums)
        # res = [i for i in range(1,n+1) if i not in hash]
        # return res   

        n = len(nums)  
        for i in range(n):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1

        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
# @lc code=end
s =Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

