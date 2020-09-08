# Definition for a binary tree node.
'''
解题思路:
对于任意一个节点a,如下所示:
    d
    a
b       c
可能的路径 b->a->c   b->a->d  c->a->d
计算三条路径的最大值即可
'''

import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_value = float('-inf')
        '''
            1
        2       3
        '''
        def dfs(root):
            if root is None:
                return 0
            left = max(0,dfs(root.left)) #计算左边最大值 9
            right = max(0,dfs(root.right)) #计算右边最大值
            self.max_value = max (self.max_value,root.val+left+right) #更新路径 选择b->a->c 
            return max(left,right)+root.val #b->a->d  c->a->d
        dfs(root)
        return self.max_value
s = Solution()