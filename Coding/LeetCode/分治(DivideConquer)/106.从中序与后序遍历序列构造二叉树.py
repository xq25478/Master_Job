#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def conquer(post_start,post_end,in_start,in_end):

            if post_start > post_end or in_start > in_end:
                return None

            post_order_root = post_end
            in_order_root = map[postorder[post_order_root]]

            root = TreeNode(postorder[post_order_root])
            size_left = in_order_root-in_start

            root.left = conquer(post_start,post_start+size_left-1,in_start,in_order_root-1)
            root.right = conquer(post_start+size_left,post_end-1,in_order_root+1,in_end)

            return root

        post_len = len(postorder)
        in_len = len(inorder)

        if post_len != in_len:
            return None
    
        map = {inorder[i]:i for i in range(in_len)}

        return conquer(0,post_len-1,0,in_len-1)
# @lc code=end
s = Solution()
print(s.buildTree([9,3,15,20,7],[9,15,7,20,3]))

