from typing import List
import copy

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0:
            return []

        sorted = []
        count = [0]*length

        def findIndex(arr,target)->int:
            if len(arr) == 0:
                return 0
            l,r = 0,len(arr)-1
            while l < r:
                mid = l + (r-l)//2
                if target > arr[mid]:
                    l = mid + 1
                else:
                    r = mid
            return l+1 if arr[l] < target else l

        i = length - 1
        while i >= 0:
            index = findIndex(sorted,nums[i])
            sorted.insert(index,nums[i])
            count[i] = index
            i -= 1
        return count

a = Solution()
print(a.countSmaller([5,2,6,1]))