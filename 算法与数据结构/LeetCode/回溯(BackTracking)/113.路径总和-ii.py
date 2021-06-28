#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:return []

        ret = []
        ans = [root.val]
        def backTrack(node:TreeNode,target:int):
            if not node.left and not node.right:
                if not target:
                    ret.append(ans[:])
                return 

            if node.left:
                ans.append(node.left.val)
                backTrack(node.left,target-node.left.val)
                ans.pop()

            if node.right:
                ans.append(node.right.val)
                backTrack(node.right,target-node.right.val)
                ans.pop()
                
        backTrack(root,sum-root.val)

        return ret
# @lc code=end

