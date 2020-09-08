from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        
        cnt_zero = 0
        for i in range(n):
            cnt_zero = cnt_zero + 1 if nums[i] != 0 else cnt_zero

        while cnt_zero:
            #奇数
            for i in range(n):
                if nums[i] & 1 == 1:
                    nums[i] -= 1
                    if not nums[i]:
                        cnt_zero -= 1
                    ret += 1
            #偶数   
            for i in range(n):
                nums[i] //= 2
            if cnt_zero:
                ret += 1
        return ret
            
s = Solution()
print(s.minOperations([1,5]))             