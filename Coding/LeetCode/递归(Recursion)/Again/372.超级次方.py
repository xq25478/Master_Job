#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#
from typing import List
# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def myPow(a:int,k:int)->int:
            res = 1
            for _ in range(k):
                res *= a
                res %= base
            
            return res

        base = 1337
        if len(b) == 0:
            return 1
        a%=base
        k = b.pop()
        last1 = myPow(a,k)
        last2 = myPow(self.superPow(a,b),10)
        return last1 * last2 % base
# @lc code=end

