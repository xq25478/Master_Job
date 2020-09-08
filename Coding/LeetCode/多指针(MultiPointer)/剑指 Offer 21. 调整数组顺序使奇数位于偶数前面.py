'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # way 1 双指针
        # left = 0
        # right = n-1

        # while left < right:
        #     if nums[left] % 2 == 1:#奇数
        #         left += 1
        #     else:#偶数
        #         if nums[right]%2 == 1: #奇数
        #             nums[left],nums[right]=nums[right],nums[left]
        #             left += 1
        #         right -= 1
        i = 0
        for j in range(n):
            if nums[j]%2 ==1:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        # way 2 单指针
        return nums