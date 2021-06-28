#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0
        def dfs(node:TreeNode,flag):
            nonlocal ret
            if flag == 0 :#左节点
                if not node.left and not node.right:
                    ret  += node.val
            if node.left:
                dfs(node.left,0)
            if node.right:
                dfs(node.right,1)
        ret = 0
        dfs(root,None)
        return ret
# @lc code=end

