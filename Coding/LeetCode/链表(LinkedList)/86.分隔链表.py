#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        biger = []
        smaller = []
        cur =  head
        while cur:
            if cur.val >= x:
                biger.append(cur.val)
            else:
                smaller.append(cur.val)
            cur = cur.next

        ret = smaller + biger

        if not ret:
            return None

        root = ListNode(-1)

        cur = root
        for i in range(len(ret)):
            # new = ListNode(ret[i])
            cur.next = ListNode(ret[i])
            cur = cur.next

        return root.next
# @lc code=end
s = Solution()
s1 = ListNode(1)
s2 = ListNode(4)
s3 = ListNode(3)
s4 = ListNode(2)
s5 = ListNode(5)
s6 = ListNode(2)
s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = s6

print(s.partition(s1,3))