#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    # 记忆化搜索 官解
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        #左右两端添加一个数 防止越界
        length = len(nums)
        val = [1] + nums + [1]
        @lru_cache(None)
        def solve(left:int,right:int)->int:
            if left >= right-1:
                return 0
            best = 0
            for i in range(left+1,right):
                best = max(val[left]*val[right]*val[i]+solve(left,i)+solve(i,right),best)
            return best
        return solve(0,length+1)
    #DP 官解
    def maxCoins1(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)
        return rec[0][n + 1]
    
# @lc code=end
s = Solution()
print(s.maxCoins([3,1,5,8]))