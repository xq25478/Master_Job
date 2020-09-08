'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，
A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 
示例 2:

输入: [0,0,1,2,5]
输出: True

'''
from typing import List
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        
        l = 0
        r = 3
        val = nums[-1]

        while r >= l:
            if nums[r]!=val-1:
                if nums[l]!=0:
                    return False
                else:
                    l += 1
                    val -= 1
            else:
                r -= 1
                val -= 1
        return True
                