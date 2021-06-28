##############LeetCode之双指针法##################
from typing import List

#075 颜色分类(https://leetcode-cn.com/problems/sort-colors/)
class Solution075:
    def sortColors(self, nums: List[int]) -> None:
        left_ptr = 0
        right_ptr = len(nums)-1
        curr_ptr = 0
        while curr_ptr <= right_ptr:
            if nums[curr_ptr] == 0:
                nums[left_ptr],nums[curr_ptr] = nums[curr_ptr],nums[left_ptr]
                curr_ptr += 1
                left_ptr += 1
            elif nums[curr_ptr] == 2:
                nums[curr_ptr],nums[right_ptr] = nums[right_ptr],nums[curr_ptr]
                right_ptr -=1
            else:
                curr_ptr+= 1