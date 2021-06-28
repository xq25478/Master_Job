---
title: LeetCode-DP-树形DP
categories:
- 数据结构与算法
- LeetCode
tags:
- 树形DP
- DP
---

## 337 打家劫舍 III
* 题目描述
<!--more-->
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
```
class Solution:
    #dp[0]表示不选取当前节点 dp[1]表示选取当前节点
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs (node:TreeNode)->List[int]:
            if node is None:
                return [0,0]
            left  = dfs(node.left)
            right = dfs(node.right)

            #要么选取左右两边各自最大之和 要么只选择根节点
            return [max(left[0],left[1]) + max(right[0],right[1]),node.val + left[0] + right[0]]
        res = dfs(root)
        return max(res[0],res[1])
```

## 96 不同的二叉搜索树
```
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0

        #dp[i]表示以i为根节点的二叉搜索树种类
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] += dp[j]*dp[i-j-1] #左边由dp[j]个节点  右边有dp[i-j-1]个节点
        return dp[n]

s = Solution()
print(s.numTrees(3))
```
