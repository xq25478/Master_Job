'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，
每一层打印到一行。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []

        stack = [root]
        ans = []
        
        while stack:
            new_stack = []
            res = []
            for i in range(len(stack)):
                node = stack[i]
                res.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            ans.append(res)
            stack = new_stack
        return ans