##############LeetCode之动态规划##################

import numpy as np 
from typing import List

#1014 最佳观光组合(https://leetcode-cn.com/problems/best-sightseeing-pair/)
class Solution1014:
    #枚举方法
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        best = 0
        ans = 0
        for index in range(len(A)):
            ans = max (ans,A[index]-index + A[best]+best)
            if A[best] + best < A[index] + index:#动态维护best值
                best = index
        return ans

if __name__ == '__main__':
    s1014 = Solution1014()
    s1014.maxScoreSightseeingPair([1,2,3])
