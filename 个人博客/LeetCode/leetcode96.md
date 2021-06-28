---
title: LeetCode96-不同的二叉搜索树
categories:
- LeetCode
tags:
- 动态规划
- LeetCode
---
本题是一道非常经典的DP问题,首先对二叉搜索树进行一个简单说明，所谓二叉搜索树，也就是对于树的任意一个节点来说，其根节点的值要不小于左节点的值且不大于右节点的值。
<!-- more -->
## 算法讲解
 对于以1 ... n 为节点组成的二叉搜索树，我们可以遍历每个数字i,G(n)表示长度为n的序列的不同二叉树数目，F(i,n)(0<=i<=n)表示以i为根的二叉树数目，于是就有以下公式:
 G(n) = F(1,n) + F(2,n) + ... + F(n,n)
### 初始状态
当n=0(空树)时或n=1(只有一个根时)，数目均为1，于是G(0) = 1,G(1)=1.
### 状态转移方程
容易得到，以i为根的二叉搜索树，其数目等于左子树个数*右子树个数，于是可知F(i,n) = G(i-1)G(n-i),从而可得状态转移方程:
G(n) = G(0)G(n-1) + G(1)G(n-2)...+G(n-1)G(0)
### 输出结果
显然算法输出的结果即为dp[n]
## 代码实现
以下是代码Python代码实现
```bash
from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
s = Solution()
print(s.numTrees(3))
```