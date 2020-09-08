'''

给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。
'''

from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        #动态规划
        pos_mul = 0
        neg_mul = 0
        ret = 0

        for num in nums:
            if num == 0:
                pos_mul = neg_mul = 0
            elif num > 0:
                pos_mul += 1
                if neg_mul > 0:
                    neg_mul += 1
            else:
                temp = neg_mul
                neg_mul = pos_mul + 1
                pos_mul = 0 if temp == 0 else temp + 1 
            
            ret = max(ret,pos_mul)
            
        return ret