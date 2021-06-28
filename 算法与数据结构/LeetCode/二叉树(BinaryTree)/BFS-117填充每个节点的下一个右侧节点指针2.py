class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        # BFS 按照层序遍历的思想 逐层遍历 同时每一层
        # 也按照一个小三角形逐步向右遍历
        # 传递的变量 三角形顶点指针 起始节点
        def next(head:'Node'):
            if head == None: #递归结束条件
                return None
            # 寻找起始节点
            while head is not None and head.left is None and head.right is None:
                head = head.next
            if head is None: #找不到 表明该层为空 直接return
                return
            # 下一层的起始节点
            next_head = head.left if head.left is not None else head.right

            while head is not None:
                temp = head.next
                avail_node = None
                while temp is not None:
                    if temp.left is None and temp.right is None:
                        temp = temp.next
                    elif temp.left is not None:
                        avail_node = temp.left
                        break
                    else:
                        avail_node = temp.right
                        break
                if head.left is not None and head.right is not None:
                    #左右均在
                    head.left.next = head.right
                    head.right.next = avail_node
                elif head.left is not None:
                    head.left.next = avail_node
                else:
                    #左在右不在
                    head.right.next = avail_node
                head = temp
            next(next_head)

        #right boundry
        temp = root
        while temp!=None:
            temp.next = None
            temp = temp.right
        # 初始化变量
        head = root
        next(head)
        return root




        