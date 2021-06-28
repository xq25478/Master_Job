---
title: LeetCode-队列
categories:
- 数据结构与算法
- LeetCode
tags:
- 队列
---

## 239 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
<!--more-->
```
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
```
