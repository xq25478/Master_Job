'''
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
'''

## 做题之间先问面试官有无空间/时间复杂度限制 考察程序员和面试官之间的沟通
# time o(n) space o(n)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        ht = {}
        for num in nums:
            if num in ht:
                return num 
            else:
                ht[num] = 1
        
# time o(n)  space o(1)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            k = nums[i]
            if nums[nums[i]] < 0:
                return -1
            


