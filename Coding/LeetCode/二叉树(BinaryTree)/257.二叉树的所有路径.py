#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(s:str,node:TreeNode):
            if not node.left and not node.right:
                s += str(node.val)
                ret.append(s)
                return

            s += str(node.val) + '->'
            if node.left:
                dfs(s,node.left)
            if node.right:
                dfs(s,node.right)

        ret = []
        if not root:return []
        dfs('',root)
        return ret
# @lc code=end

