#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        def dfs(stk:deque):
            if not stk:return
            n = len(stk)
            lay = []
            for _ in range(n):
                node = stk.popleft()
                lay.append(node.val)
                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
            dfs(stk)
            ret.append(lay)

        if not root:
            return []
        stack = deque()
        stack.append(root)
        ret = []
        dfs(stack)
        return ret

# @lc code=end

