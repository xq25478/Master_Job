'''
请实现两个函数，分别用来序列化和反序列化二叉树。
'''
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        from collections import deque
        if not root:return '[]'
        queue = deque()
        queue.append(root)
        arr = []
        while queue:
            node = queue.popleft()
            if node:
                arr.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                arr.append('null')

        #删除最后面的叶子节点的None
        while arr[-1] == None:
            arr.pop()

        return '[' + ','.join(arr) + ']'        

    def deserialize(self, data):
        from collections import deque
        if data == '[]':return
        vals, i = data[1:-1].split(','), 1

        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))