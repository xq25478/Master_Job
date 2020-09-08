#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       
        N = len(gas)
        i = 0
        cur_tank = 0
        tol_tank = 0
        start_station = 0
        
        for i in range(N):
            tol_tank += gas[i]-cost[i]
            cur_tank += gas[i]-cost[i]
            if cur_tank < 0:
                cur_tank = 0
                start_station = i + 1
            
        return start_station if tol_tank >= 0 else -1 
# @lc code=end
s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
