from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#题解来自liweiwei19 树形DP入门
class Solution:
    #dp[0]表示不选取当前节点 dp[1]表示选取当前节点
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs (node:TreeNode)->List[int]:
            if node is None:
                return [0,0]
            left  = dfs(node.left)
            right = dfs(node.right)
            return [max(left[0],left[1]) + max(right[0],right[1]),node.val + left[0] + right[0]]
        res = dfs(root)
        return max(res[0],res[1])
            


        