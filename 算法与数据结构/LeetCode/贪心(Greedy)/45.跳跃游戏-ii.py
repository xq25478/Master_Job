#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n,right_most = len(nums),0
        end = 0
        cnt = 0
        for i in range(0,n-1):
            right_most = max(nums[i]+i,right_most)
            if i ==  end:
                cnt+=1
                end = right_most
        return cnt
# @lc code=end

