---
title: LeetCode-蓄水池抽样
categories:
- 数据结构与算法
- LeetCode
tags:
- 蓄水池抽样
---

## 382 链表随机节点
给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
* 算法原理

<!--more-->
```
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        import random
        """
        Returns a random node's value.
        """
        count = 0
        reserve = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1,count)
            if rand == count:
                reserve = cur.val
            cur = cur.next
        return reserve
```
