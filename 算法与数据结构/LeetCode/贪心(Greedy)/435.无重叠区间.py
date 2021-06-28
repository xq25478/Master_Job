#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
from typing import List
# @lc code=start
class Solution:
    '''
    采用贪心算法求解 将每个区间按照end升序排列 去掉区间当中start>end 重复即可
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
            
        intervals.sort(key=lambda x:x[1])
        cur = intervals[0][1]
        cnt = 1
 
        for interval in intervals:
            if interval[0] >= cur:
                cur = interval[1]
                cnt += 1

        return n- cnt
# @lc code=end

