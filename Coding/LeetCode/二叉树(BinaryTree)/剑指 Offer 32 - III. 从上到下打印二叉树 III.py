'''
请实现一个函数按照之字形顺序打印二叉树，
即第一行按照从左到右的顺序打印，第二层
按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #思路一 倒序输入
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root:return []

        queue = deque()
        queue.append(root)
        ret = []
        odd = False
        while queue:
            new_queue = deque()
            res = []
            while queue:
                node = queue.popleft()
                res.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            if odd:
                res = res[::-1]
            ret.append(res)
            queue = new_queue
            odd = ~odd
        return ret
        #思路2 两边输入
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res