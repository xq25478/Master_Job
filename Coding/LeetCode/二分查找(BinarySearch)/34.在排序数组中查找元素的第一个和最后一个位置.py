#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)

        if not nums or target < nums[0] or target > nums[-1]:
            return [-1,-1]

        while left < right:
            mid = left + (right-left)//2

            if nums[mid] > target:
                right = mid
            
            if nums[mid] < target:
                left = mid + 1
            
            if nums[mid] == target:
                left = mid
                right = mid 
                for i in range(mid,len(nums)):
                    if nums[i] == target:
                        right = i
                    
                for i in range(mid-1,-1,-1):
                    if nums[i] == target:
                        left = i 
                        
                return [left,right]
        return [-1,-1]
# @lc code=end

