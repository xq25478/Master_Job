#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        from collections import deque
        if not root:return 0
        stack = deque()
        stack.append(root)
        depth = 1

        while stack:
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node.left and not node.right:
                    return depth
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            depth+=1
        return depth

# @lc code=end

