#
# @lc app=leetcode.cn id=1465 lang=python3
#
# [1465] 切割后面积最大的蛋糕
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h_pre = 0
        w_pre = 0
        max_h = 0
        max_w = 0
        mod = (10**9+7)
        #添加边界
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()

        for i in range(len(horizontalCuts)):
            max_h = max(horizontalCuts[i]-h_pre,max_h)
            h_pre = horizontalCuts[i]


        for j in range(len(verticalCuts)):
            max_w = max(verticalCuts[j]-w_pre,max_w)
            w_pre = verticalCuts[j]

        return (max_w%mod)*(max_h%mod)%mod
# @lc code=end

