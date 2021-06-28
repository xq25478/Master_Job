'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。
'''
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0 
        for i in range(len(nums)):
            res ^= nums[i]

        div = 1
        while div & res == 0:
            div <<= 1
        
        a = 0
        b = 0
        for i in range(len(nums)):
            if nums[i] & div:
                a ^= nums[i]
            else:
                b ^= nums[i]

        return [a,b]