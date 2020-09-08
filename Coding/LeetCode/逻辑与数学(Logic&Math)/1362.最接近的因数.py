#
# @lc app=leetcode.cn id=1362 lang=python3
#
# [1362] 最接近的因数
#
import math
from typing import List
# @lc code=start
class Solution:
    def divide(self, n):
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % i == 0:
                return [i, n // i]

    def closestDivisors(self, num: int) -> List[int]:
        ans = [0, int(1e9)]
        for i in range(num + 1, num + 3):
            cur = self.divide(i)
            if abs(cur[0] - cur[1]) < abs(ans[0] - ans[1]):
                ans = cur
        return ans
# @lc code=end

