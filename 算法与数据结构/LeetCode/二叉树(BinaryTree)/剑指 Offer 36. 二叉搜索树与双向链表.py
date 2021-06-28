'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        #left-pre right-next 非就地
        # inOrder = []

        # def dfs(node:Node):
        #     if not node:
        #         return 
        #     dfs(node.left)
        #     inOrder.append(node)
        #     dfs(node.right)

        # dfs(root)
        # if not inOrder:
        #     return None

        # for i in range(len(inOrder)-1):
        #     inOrder[i].right = inOrder[i+1]
        #     inOrder[i+1].left = inOrder[i]

        # inOrder[-1].right = inOrder[0]
        # inOrder[0].left = inOrder[-1]

        # return inOrder[0]

        #就地
        self.pre = None
        self.head = None

        def dfs(cur:Node)->Node:
            if not cur:return
            dfs(cur.left)

            if self.pre:
                self.pre.right,cur.left= cur,self.pre
            else:
                self.head = cur
            
            self.pre = cur
            dfs(cur.right)

            return 

        if not root:return None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

  