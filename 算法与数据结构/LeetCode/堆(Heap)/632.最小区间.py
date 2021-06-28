#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        #方法1 堆
        left,right = -10**9,10**9

        max_value = max(vec[0] for vec in nums)#堆中最大值
        priority_queue = [(vec[0],i,0) for i, vec in enumerate(nums)]
        heapq.heapify(priority_queue)

        while True:
            min_value,row,idx = heapq.heappop(priority_queue)#堆中最小值
            if max_value-min_value < right-left:
                left,right = min_value,max_value
            if idx == len(nums[row]) -1:
                break
            max_value = max(max_value,nums[row][idx+1])
            heapq.heappush(priority_queue,(nums[row][idx+1],row,idx+1))#重新放入row行的一个元素

        return [left,right]
# @lc code=end
s = Solution()
print(s.smallestRange([
[4,10,15,24,26],
[0,9,12,20],
[5,18,22,30]]))
