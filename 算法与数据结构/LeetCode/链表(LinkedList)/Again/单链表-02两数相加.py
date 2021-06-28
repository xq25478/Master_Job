##############LeetCode之链表操作##################

#02 两数相加
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        step_flag = 0
        
        cur = ret

        while l2!=None or l1!=None:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            add_value = val1 + val2 + step_flag
            step_flag = add_value // 10
            add_value = add_value % 10
            cur.next = ListNode(add_value)
            cur = cur.next

            l2 = None if not l2 else l2.next
            l1 = None if not l1 else l1.next

        if step_flag == 1:
            cur.next = ListNode(1)

        return ret.next