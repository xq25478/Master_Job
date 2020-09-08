#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
    '''
    分治
    前序遍历
    根---左子树---右子树
    中序遍历
    左子树---根---右子树
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def conquer(pre_start,pre_end,in_start,in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            pre_order_root = pre_start
            in_order_root = map[preorder[pre_order_root]]

            root = TreeNode(preorder[pre_order_root])
            size_left = in_order_root-in_start

            root.left = conquer(pre_start+1,pre_start+size_left,in_start,in_order_root-1)
            root.right = conquer(pre_start+size_left+1,pre_end,in_order_root+1,in_end)

            return root

        pre_len = len(preorder)
        in_len = len(inorder)

        if pre_len != in_len:
            return None
    
        map = {inorder[i]:i for i in range(in_len)}

        return conquer(0,pre_len-1,0,in_len-1)
# @lc code=end

