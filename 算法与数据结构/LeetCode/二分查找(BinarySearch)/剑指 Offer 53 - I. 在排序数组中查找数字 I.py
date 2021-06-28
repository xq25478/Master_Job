'''
统计一个数字在排序数组中出现的次数。
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        if not nums or target < nums[0] or target > nums[-1]:
            return 0

        res = 0
        while left < right:
            mid = left + (right-left)//2

            if nums[mid] > target:
                right = mid
            
            if nums[mid] < target:
                left = mid + 1
            
            if nums[mid] == target:
                for i in range(mid,len(nums)):
                    if nums[i] == target:
                        res += 1
                for i in range(mid-1,-1,-1):
                    if nums[i] == target:
                        res += 1
                break
        return res