# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #思路 链表1走完走链表2 链表2走完走链表1 相遇即为有公共焦点
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pt_a = headA
        pt_b = headB
        a = 0
        b = 0
        #[4 1 8 4 5] [5 0 1 8 4 5]
        while pt_a and pt_b:
    
            if pt_a is pt_b:
                return pt_a

            if not pt_a.next:
                pt_a = headB
                a += 1
                if a == 2:
                    return None
            else:
                pt_a = pt_a.next

            if not pt_b.next:
                pt_b = headA
                b+=1
                if b == 2:
                    return None
            else:
                pt_b = pt_b.next

        return None