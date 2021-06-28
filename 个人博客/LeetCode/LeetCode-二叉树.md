---
title: LeetCode-二叉树
categories:
- 数据结构与算法
- LeetCode
tags:
- 二叉树
---

## 144 二叉树的前序遍历
<!--more-->
```
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
#递归
        return [root.val] + self.preorderTraversal(root.left) + \
            self.preorderTraversal(root.right)

#非递归
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right: stack.append(node.right) #先添加right
            if node.left: stack.append(node.left)
        return res
```

## 145 二叉树的后序遍历
```
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
#递归
        return  self.postorderTraversal(root.left) + \
            self.postorderTraversal(root.right) + [root.val] 

#非递归
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            res.append(node.val)
        return res[::-1]
```
## 94 二叉树的中序遍历
```
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
# 递归
        ans = []
        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)

# 非递归
        stack = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
```
## 102 二叉树的层序遍历
```
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur,res = [root],[]

        while cur:
            lay,layer = [],[]
            for node in cur:
                layer.append(node.val)
                if node.left:lay.append(node.left)
                if node.right:lay.append(node.right)
            cur = lay
            res.append(layer)
        return res
```

## 111 二叉树的最小深度
```
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        from collections import deque
        if not root:return 0
        stack = deque()
        stack.append(root)
        depth = 1

        while stack:
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node.left and not node.right:
                    return depth
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            depth+=1
        return depth
```

## 104二叉树的最大深度
* 相似题目:剑指55
```
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #递归
        if not root:
            return 0
        if root.left!=None:
            l_value = self.maxDepth(root.left)
        if root.right!=None:
            r_value = self.maxDepth(root.right)
        return max(r_value,l_value)+1
```

## 429 N叉树的层序遍历
```
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        res = []
        queue = [root]
        def bfs(queue):
            if len(queue) == 0 :
                return 
            res.append([ i.val for i in queue])
            queue = [childen for node in queue for childen in node.children]
            bfs(queue)
        bfs(queue)
        return res
```

## 100 相同的树
```
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p!=None and q!=None:
            return (p.val == q.val) and self.isSameTree(p.left,q.left)  and self.isSameTree(p.right,q.right)    
         elif p==None and q == None:
            return True
         else :
            return False
```

## 101 平衡二叉树
验证一颗二叉树是否为平衡二叉树

```
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        from functools import lru_cache
        from collections import deque
# 自顶向下
## 非记忆化 O(nlogn) - O(N)
        # if not root:return True
        
        # @lru_cache
        # def maxDepth(node:TreeNode)->bool:
        #     if not node:return 0
        #     return max(maxDepth(node.left),maxDepth(node.right)) + 1

        # queue = deque()
        # queue.append(root)

        # while queue:
        #     temp = queue.popleft()
        #     left  = 0 if not temp.left  else maxDepth(temp.left)
        #     right = 0 if not temp.right else maxDepth(temp.right)
        #     if abs(right-left) > 1:
        #         return False
        #     if temp.left:
        #         queue.append(temp.left)
        #     if temp.right:
        #         queue.append(temp.right)

        # return True  
        #  
# 自顶向下      
## 记忆化储存 节约递归时间 O(N)-O(N)
        if not root:return True
    
        ht = {} 

        def maxDepth(node:TreeNode)->bool:
            if not node:return 0
            ht[node] =  max(maxDepth(node.left),maxDepth(node.right)) + 1
            return ht[node]

        queue = deque()
        queue.append(root)
        maxDepth(root)

        while queue:
            temp = queue.popleft()
            left  = 0 if not temp.left  else ht[temp.left]
            right = 0 if not temp.right else ht[temp.right]
            if abs(right-left) > 1:
                return False
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return True   
```

## 剑指offer07 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
```
class Solution:
    '''
    思路 分治法
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def conquer(pre_start,pre_end,in_start,in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            pre_order_root = pre_start
            in_order_root = map[preorder[pre_order_root]]

            root = TreeNode(preorder[pre_order_root])
            size_left = in_order_root-in_start

            root.left = conquer(pre_start+1,pre_start+size_left,in_start,in_order_root-1)
            root.right = conquer(pre_start+size_left+1,pre_end,in_order_root+1,in_end)

            return root

        pre_len = len(preorder)
        in_len = len(inorder)

        if pre_len != in_len:
            return None
    
        map = {inorder[i]:i for i in range(in_len)}

        return conquer(0,pre_len-1,0,in_len-1)
```