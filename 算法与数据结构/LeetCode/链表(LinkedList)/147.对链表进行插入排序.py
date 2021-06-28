#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        # def insert(front:ListNode,next:ListNode,cnt:int)->ListNode:

        #     if not front: #第一个节点为空
        #         return next,next.next

        #     pre = None
        #     cur = front
        #     back = next.next
        #     k = 0
        #     find = False
        #     while k < cnt:
        #         if find or cur.val < next.val:
        #             pre = cur
        #             cur = cur.next
        #         else:
        #             if not find:
        #                 find = True
        #                 if not pre:
        #                     front = next
        #                 else:
        #                     pre.next = next
        #                 next.next = cur
        #         k += 1
        #     # 此时cur为尾部节点 连接待插入节点后面的节点
        #     cur.next = back
        #     return front,back

        # front = None
        # next = head
        # cnt = 0
        # while next:
        #     front,next= insert(front,next,cnt)
        #     cnt += 1
        # return front
        
        if (not head) or (not head.next) : return head
        left = head
        while left.next:#对第二个开始的数进行判断
            node = left.next#取要判断的数为node
            if node.val >= left.val:#如果node值比大于等于前一个值，那么就不变，指针右移。
                left = left.next
                continue
            left.next = node.next#如果node值比前一个值小，说明需要排序，首先断开node节点。
			#设定左右比较值，pre & post
            pre = head
            post = head.next
            #把node值与pre和post进行比较，主要有三种情况。
            while pre != left.next:
                if node.val <= pre.val:
                    node.next = pre
                    head = node
                    break
                elif pre.val < node.val <= post.val:
                    pre.next = node
                    node.next = post
                    break
                else:
                    pre = post
                    post = post.next
                    
        return head
# @lc code=end
s = Solution()
s1 = ListNode(4)
s2 = ListNode(2)
s3 = ListNode(1)
s4 = ListNode(3)
s1.next = s2
s2.next = s3
s3.next = s4
print(s.insertionSortList(s1))
