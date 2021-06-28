#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
########################递归##############################
# class Solution:
#     def generateTrees(self, n: int) -> List[TreeNode]:
#         def generate(start,end):
#             all_tree = []
#             if start > end:
#                 return [None]
#             for i in range(start,end+1):
#                 left_tree  = generate(start,i-1)
#                 right_tree = generate(i+1,end)
#                 for l in left_tree:
#                     for r in right_tree:
#                         curr_tree = TreeNode(i)
#                         curr_tree.left = l
#                         curr_tree.right = r
#                         all_tree.append(curr_tree)
#             return all_tree
#         return generate(1,n) if n > 0 else []
#########################动态规划###########################
from copy import deepcopy
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        first = TreeNode(1)
        pre = [first]

        for i in range(2,n+1):
            cur = []
            for node in pre:
                #插入到根结点
                insert = TreeNode(i) ###一定要使用deepcopy!!!
                insert.left = deepcopy(node)
                cur.append(insert)

                #插入到右孩子或者右孩子的右孩子或者右孩子的右孩子的...的右孩子
                for j in range(0,n+1):
                    root_copy = deepcopy(node) ### 创建子树 一定要使用deepcopy!!!
                    right = root_copy
                    k = 0
                    while k < j:
                        if not right:
                            break
                        right = right.right
                        k += 1
                    if not right:
                        break
                    right_tree = right.right
                    insert = TreeNode(i)
                    right.right = insert
                    insert.left = right_tree
                    cur.append(root_copy)
            pre = cur
        return pre
# @lc code=end
s = Solution()
print(s.generateTrees(2))