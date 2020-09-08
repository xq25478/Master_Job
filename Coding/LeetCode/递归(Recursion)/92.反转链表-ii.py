#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        def reverse(head:ListNode,length):
            nonlocal succerror
            if length == 1:
                succerror = head.next
                return head,None
            front,_ = reverse(head.next,length-1)
            head.next.next = head
            head.next = succerror
            back = head
            return front,back

        if m == n:
            return head
            
        front = head
        pre = None
        k = m
        while k > 1:
            pre = front
            front = front.next
            k -= 1

        succerror = None
        #反转从front 开始的前n-m个节点
        front,back= reverse(front,n-m+1)
        if back == head:
            return front
        else:
            pre.next = front
            return head
# @lc code=end
s1 = ListNode(3)
s2 = ListNode(5)
s1.next = s2
s = Solution()
print(s.reverseBetween(s1,1,2))