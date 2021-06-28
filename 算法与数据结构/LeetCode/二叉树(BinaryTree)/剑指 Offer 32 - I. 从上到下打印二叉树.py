'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        from collections import deque
        if not root:return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            node = queue.popleft()
            res.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        return res
