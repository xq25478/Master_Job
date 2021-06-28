'''
小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。
小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。
注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
'''
from typing import List
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        def ds(target,left,right)->int:
            while left < right:
                mid =  left + (right-left)//2
                if drinks[mid] <=  target:
                    left = mid + 1
                else:
                    right = mid

            return left

        if not staple or not drinks:return 0
        staple.sort()
        drinks.sort()
        #[1,5,8,9] 2

        ret = 0
        left = 0
        right = len(drinks)
        for i in range(len(staple)):
            if staple[i] < x:
                tmp = ds(x-staple[i],left,right)
                ret += tmp
                if not tmp:
                    break
                    
        return ret%(1000000007)