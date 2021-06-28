#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(s1:TreeNode,s2:TreeNode):
            if not s1 and not s2:
                return None

            v1 = 0 if not s1 else s1.val
            v2 = 0 if not s2 else s2.val
            s1 = TreeNode(0) if not s1 else s1
            s2 = TreeNode(0) if not s2 else s2
            node = TreeNode(v1 + v2)
            
            node.left  = dfs(s1.left,s2.left)
            node.right = dfs(s1.right,s2.right)
            return node

        if not t1 and not t2:
            return None

        root = dfs(t1,t2)
        return  root

# @lc code=end

