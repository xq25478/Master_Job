#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
# @lc code=end

