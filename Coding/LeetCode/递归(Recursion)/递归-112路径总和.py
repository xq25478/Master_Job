from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #递归
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.right == None and root.left == None :
            return (root.val == sum)
        return self.hasPathSum(root.right,sum-root.val) | self.hasPathSum(root.left,sum-root.val)

s = Solution()
print(s.hasPathSum([5,4,8,11,None,13,4,7,2,None,None,None,1],22))