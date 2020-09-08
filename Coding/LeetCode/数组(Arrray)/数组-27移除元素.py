from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        l = 0
        r = length-1
        res = 0
        while l <= r:
            if nums[l] == val:
                res += 1
                while nums[r] == val and l!=r:
                    res += 1
                    r -= 1
                nums[l],nums[r] = nums[r],nums[l]
                r-= 1
            l += 1
        return length-res

class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        count = 0
        for i in range(0,length):
            if nums[i]!=val:
                nums[count] = nums[i]
                count+=1
        return count

s = Solution()
print(s.removeElement([1],1))