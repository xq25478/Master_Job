#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        visited = [False]*len(nums)
        for _ in range(0,3):
            max_value = float('-inf')
            max_value_index = len(nums)
            for index,value in enumerate(nums):
                if visited[index] == False and value > max_value:
                    max_value = value
                    max_value_index = index
            if max_value_index == len(nums):
                return max(nums)
            visited[max_value_index]  = True
            for index in range(len(nums)):
                if visited[index] == False and nums[index] == max_value:
                    visited[index] = True
        return max_value
# @lc code=end
s = Solution()
print(s.thirdMax([1,1,2]))
