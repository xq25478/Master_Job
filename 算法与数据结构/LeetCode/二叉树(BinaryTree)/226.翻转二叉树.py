#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node:TreeNode):
            node.left,node.right = node.right,node.left
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        if not root:return None
        dfs(root)
        return root
# @lc code=end

