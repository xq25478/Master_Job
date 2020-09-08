# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #快慢指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        for _ in range(1,n):
            cur = cur.next
        first = cur

        cur = head
        pre_node = None

        while first.next !=None:
            pre_node = cur
            first = first.next
            cur = cur.next

        if pre_node == None:
            return head.next
            
        pre_node.next = cur.next
        return head

s = Solution()
s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(3)
s4 = ListNode(4)
s5 = ListNode(5)
s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = None
head = s.removeNthFromEnd(s1,1)
while head!= None:
    print(head.val)
    head = head.next