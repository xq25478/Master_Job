##############LeetCode之链表操作##################

#02 两数相加
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution002:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = l1
        step_flag = 0
        pre_l1 = None
        pre_l2 = None

        while l2!=None or l1!=None:
            if l1 == None and l2 == None:
                break
            if l1 == None:
                new_l1_node = ListNode(0)
                pre_l1.next = new_l1_node 
                l1 = new_l1_node
            if l2 == None:
                new_l2_node = ListNode(0)
                pre_l2.next = new_l2_node 
                l2 = new_l2_node

            add_value = l1.val + l2.val + step_flag
            step_flag = add_value // 10
            add_value = add_value % 10
            l1.val = add_value

            pre_l1 = l1
            pre_l2 = l2
            l2 = l2.next
            l1 = l1.next

        if step_flag == 1:
            new_node = ListNode(1)
            pre_l1.next = new_node
        return res