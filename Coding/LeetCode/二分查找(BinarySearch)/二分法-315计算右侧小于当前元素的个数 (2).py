from typing import List

class Solution:
    #遍历
    def findMin(self, nums: List[int]) -> int:

        arr_len = len(nums)
        for i in range(arr_len-1):
            if nums[i+1]<nums[i]:
                return nums[i+1]
        return nums[0]
        
    #二分法
    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            pivot = left + (right-left)//2
            if nums[pivot] < nums[right]:
                right = pivot
            elif nums[pivot] > nums[right]:
                left = pivot+1
            else:
                right -= 1
        return nums[left]

a = Solution()
print(a.findMin2([1,3,5,0]))
