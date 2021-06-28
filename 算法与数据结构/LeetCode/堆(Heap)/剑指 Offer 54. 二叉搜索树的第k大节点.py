# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
# 思路1 最小堆(size = k)
    def kthLargest(self, root: TreeNode, k: int) -> int:
        import heapq
        if not root:return

        stack = [root]
        heap = []
        n = 0

        while stack:
            node = stack.pop()
            if n < k:
                heapq.heappush(heap,node.val)
                n += 1
            else:
                if node.val > heap[0]:
                    heapq.heapreplace(heap,node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return heap[0]
# 思路2 中序遍历为递增数组

