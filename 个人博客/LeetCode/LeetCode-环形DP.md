---
title: LeetCode-DP-环形DP
categories:
- 数据结构与算法
- LeetCode
tags:
- 环形DP
- DP
---

## 213打家劫舍II
* 题目描述:

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
<!--more-->
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        #分为小偷不偷窃第一间房屋和小偷偷窃第一间房屋
        res = 0
        dp_0 = 0
        dp_1 = 0 #不偷窃第一号房间 所以最后一号房可偷可不偷
        for i in range(1,len(nums)):
            new_dp = max(dp_1,nums[i]+dp_0)
            dp_0 = dp_1
            dp_1= new_dp
            
        res = max(res,dp_1)

        dp_0 = 0
        dp_1 = nums[0] #偷窃了第一号房 最后一号房必须不能偷
        for i in range(1,len(nums)-1):
            new_dp = max(dp_1,nums[i]+dp_0)
            dp_0 = dp_1
            dp_1 = new_dp

        return max(res,dp_1)
```
