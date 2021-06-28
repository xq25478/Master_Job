class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return

        def next(left_node:'Node',right_node:'Node',flag):
            if left_node is  None or right_node is None:
                return
            left_node.next = right_node
            if flag: #相同父节点
                next(left_node.left,left_node.right,True)
                next(right_node.left,right_node.right,True)  
            next(left_node.right,right_node.left,False)

        next(root.left,root.right,True)
        #right boundry
        temp = root
        while temp!=None:
            temp.next = None
            temp = temp.right
        return root


        