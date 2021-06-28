#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        
        '''
        显示中序遍历 o(n) o(n)
        '''
        in_arr = []
        sort_in_arr = []
        err = []

        def inOrder(root:TreeNode):
            if not root:return
            inOrder(root.left)
            in_arr.append(root.val)
            inOrder(root.right)

        def change(root:TreeNode):
            if not root: return 
            if root.val in err:
                root.val = err[0] if root.val == err[1] else err[1]
            change(root.left)
            change(root.right)

        inOrder(root)
        sort_in_arr = sorted(in_arr)

        for i in range(len(in_arr)):
            if in_arr[i]!=sort_in_arr[i]:
                err.append(in_arr[i])

        change(root)
# @lc code=end