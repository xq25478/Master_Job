#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

# 自底向上
# @lc code=end

