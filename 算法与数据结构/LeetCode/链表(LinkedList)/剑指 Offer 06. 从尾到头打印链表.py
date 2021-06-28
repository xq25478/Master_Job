'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
 
限制：
0 <= 链表长度 <= 10000
'''
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
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
