# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
