#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #转换为数组
        def dfs(left:int,right:int):
            if left == right:return TreeNode(arr[left])
            if left > right:return None
            
            mid = left + (right-left)//2
            root = TreeNode(arr[mid])
            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)

            return root

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)
        left = 0
        right = n - 1
        root = dfs(left,right)
        
        return root

    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     #快慢指针
    #     if not head:return None

    #     if not head.next:return TreeNode(head.val)

    #     mid = head #寻找中点
    #     fast = head
    #     pre = head

    #     step = True
    #     while fast.next:
    #         if step:
    #             pre = mid
    #             mid = mid.next
    #         step = not step
    #         fast = fast.next

    #     pre.next = None #前面一段   
    #     root = TreeNode(mid.val)
    #     root.left = self.sortedListToBST(head)
    #     root.right = self.sortedListToBST(mid.next)

    #     return root
# @lc code=end

