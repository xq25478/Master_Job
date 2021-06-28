---
title: LeetCode-二叉搜索树
categories:
- 数据结构与算法
- LeetCode
tags:
- 二叉搜索树
---

## 98 验证二叉搜索树
<!--more-->
```
Code1
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(Node:TreeNode,min:TreeNode,max:TreeNode):
            if not Node:return True

            if min and Node.val <= min.val:
                return False
            if max and Node.val >= max.val:
                return False
            
            return helper(Node.left,min,Node) and helper(Node.right,Node,max)

        return helper(root,None,None)
Code2
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #二叉搜索树的中序遍历必然是递增的

        self.stack_value = float('-inf')
        self.res = True

        def dfs(node:TreeNode)->bool:
            if not node: return 

            dfs(node.left)
            if node.val > self.stack_value:
                self.stack_value = node.val
            else:
                self.res = False
                return 
            dfs(node.right)

        dfs(root)
        return self.res
```

## 235 二叉搜索树的最近公共祖先

