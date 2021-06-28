#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#
from typing import List
# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res = [1]
        l = len(primes)
        nums = [0]*l

        for _ in range (1,n):
            ugly = [res[nums[i]]*primes[i] for i in range(l)]
            min_ugly = min(ugly)
            res.append(min_ugly)
            for i in range(l):
                if min_ugly == res[nums[i]]*primes[i]:
                    nums[i] += 1
        return res[n-1]
# @lc code=end

