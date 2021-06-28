
---
title: LeetCode-BFS
categories:
- 数据结构与算法
- LeetCode
tags:
- BFS
---


## 剑指 Offer 13. 机器人的运动范围
* 题目描述

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
<!--more-->
```
class Solution:
    BFS 广度优先搜索 借助队列实现
    def check_cooridnate(number):
        hundreds = number // 100
        ten = (number-hundreds*100)//10
        last = number%10
        return hundreds + ten + last

    marked = set()  # 将访问过的点添加到集合marked中,从(0,0)开始
    queue = collections.deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        if (x,y) not in marked and self.check_cooridnate(x,y) <= k:
            marked.add((x,y)) 
            for dx, dy in [(1,0),(0,1)]:  # 仅考虑向右和向下即可
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    queue.append((x+dx,y+dy)) 
    return len(marked)   
```