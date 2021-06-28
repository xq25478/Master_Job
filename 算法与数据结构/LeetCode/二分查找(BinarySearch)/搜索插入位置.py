from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n-1 
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return l if l == n or nums[l] > target else l+1
s = Solution()
print(s.searchInsert([1,3,5,6],7))
print(s.searchInsert([1],1))
print(s.searchInsert([1,3,5,6],0))
print(s.searchInsert([1,3,5,6],4))
print(s.searchInsert([1,3,5,6],2))