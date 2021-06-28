#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List
from collections import deque
import heapq
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        思路1:双端单调递减队列 23% 33.91%
        '''
        deq = deque()
        ans = []

        def deq_push(deq:deque,num):
            while deq:
                val = deq.pop()
                if val >= num:
                    deq.append(val)
                    break
            deq.append(num)

        def deq_max(deq:deque):
            val = deq.popleft()
            deq.appendleft(val)
            return val

        def deq_pop(deq,num):
            if deq:
                val = deq.popleft()
                if val != num:
                    deq.appendleft(val)

        for i in range(len(nums)):
            if i < k-1:
                deq_push(deq,nums[i])
            else:
                deq_push(deq,nums[i])
                ans.append(deq_max(deq))
                deq_pop(deq,nums[i-k+1])
                
        return ans
   
# @lc code=end
# s = Solution()
# print(s.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6],5))
data = [1,None,2]
res = '['
for i in range(len(data)):
    res += str(data[i])
    if i != len(data)-1:
        res += ','
res += ']'

data = res.split('[')[1].split(']')[0].split(',')
print(data)
