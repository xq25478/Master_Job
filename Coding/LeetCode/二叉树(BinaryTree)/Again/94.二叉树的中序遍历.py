#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        ans = []
        # 递归写法
        # def dfs(root:TreeNode):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     ans.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        
        #迭代的写法 借助栈来实现
        stack = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
# @lc code=end

