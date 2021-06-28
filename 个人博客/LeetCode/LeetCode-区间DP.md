---
title: LeetCode-DP-区间DP
categories:
- 数据结构与算法
- LeetCode
tags:
- 区间DP
- DP
---

## 486 预测赢家 
* 类似题目 877-石子游戏
* 题目描述

给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。
<!--more-->
```
class Solution:
    #斜向DP
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        #dp[i][j]表示 dp[i][j][0]表示先手 dp[i][j][1]表示后手
        dp = [[[0,0] for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i][0] = nums[i]
            dp[i][i][1] = 0

        for l in range(1,n): #每一轮遍历x轴的起点 
            for k in range(l,n):
                j = k 
                i = k - l
                left  = nums[i] + dp[i+1][j][1]
                right = nums[j] + dp[i][j-1][1]
                if left >= right:
                    dp[i][j][0] = left
                    dp[i][j][1] =  dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] =  dp[i][j-1][0]

        return dp[0][n-1][0] >= dp[0][n-1][1]
        
s = Solution()
print(s.PredictTheWinner([1,5,2]))
```
