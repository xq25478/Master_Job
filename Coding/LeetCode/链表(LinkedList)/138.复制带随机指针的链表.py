#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        from collections import deque
        if not head:return None

        ht = {}
        root = Node(head.val)
        ht[head] = root

        queue = deque()
        queue.append(head)

        while queue:
            temp = queue.popleft()

            if temp.next:
                if temp.next not in ht:
                    ht[temp.next] = Node(temp.next.val)
                queue.append(temp.next)
                ht[temp].next = ht[temp.next]

            if temp.random :
                if temp.random not in ht:
                    ht[temp.random] = Node(temp.random.val)
                ht[temp].random = ht[temp.random]  

        return root
# @lc code=end

