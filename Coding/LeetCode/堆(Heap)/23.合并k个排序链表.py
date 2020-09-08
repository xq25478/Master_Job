#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# @lc code=start
# Definition for singly-linked list.
import heapq
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = None
        cur = root

        lists = [i for i in lists if i]
        min_heap = [(i.val,idx) for idx,i in enumerate(lists) if i]
        p_node = [i for i in lists]
        heapq.heapify(min_heap)

        while min_heap:
            _,idx = heapq.heappop(min_heap)
            node = p_node[idx]

            if p_node[idx].next != None:
                p_node[idx] = p_node[idx].next
                heapq.heappush(min_heap,(p_node[idx].val,idx))

            if root == None:
                root = node
                cur = root
            else:
                cur.next = node
                cur = node

        if cur :
            cur.next = None
            
        return root
# @lc code=end