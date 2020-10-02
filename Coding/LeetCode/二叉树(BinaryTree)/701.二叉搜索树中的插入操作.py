#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#
# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(node:TreeNode,val):
            if node.val < val:
                if node.right:
                    helper(node.right,val)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    helper(node.left,val)
                else:
                    node.left = TreeNode(val)

        if not root:return TreeNode(val)
        helper(root,val)
        return root
# @lc code=end

