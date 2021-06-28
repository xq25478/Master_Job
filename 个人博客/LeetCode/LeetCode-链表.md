---
title: LeetCode-链表
categories:
- 数据结构与算法
- LeetCode
tags:
- 链表
---

## 剑指06 从尾到头打印链表
<!--more-->
```
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 思路一 反转
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next

        # return res[::-1]
        res =  []
        #思路2 递归
        res = []
        def dfs(root:ListNode,res):
            if not root:
                return 
            dfs(root.next,res)
            res.append(root.val)
        dfs(head,res)
        return res
```

## 剑指18 删除链表的节点

```
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        pre = None
        cur = head

        while cur and cur.val != val:
            pre = cur
            cur = cur.next

        if not cur:
            return head

        if cur == head:
            return cur.next
        else:
            pre.next = cur.next
                 
        return  head
```

## 剑指24 反转链表

```
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        if not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
```

## 138 复杂链表的复制
采用hash表的思想
```
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
```
