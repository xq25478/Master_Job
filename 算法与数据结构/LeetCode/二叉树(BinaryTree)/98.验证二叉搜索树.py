#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #二叉搜索树的中序遍历必然是递增的

        self.stack_value = float('-inf')
        self.res = True

        def dfs(node:TreeNode)->bool:
            if not node: return 

            dfs(node.left)
            if node.val > self.stack_value:
                self.stack_value = node.val
            else:
                self.res = False
                return 
            dfs(node.right)

        dfs(root)
        return self.res
# @lc code=end

