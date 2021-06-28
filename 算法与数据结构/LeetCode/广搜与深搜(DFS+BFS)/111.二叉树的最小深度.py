#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
import queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        depth = 1
        q = queue.Queue(-1)
        q.put(root)
        while q.qsize() > 0:
            n = q.qsize()
            for _ in range(n):
                node = q.get()
                if (not node.left) and (not node.right):
                    return depth
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            depth += 1
        return depth
# @lc code=end
