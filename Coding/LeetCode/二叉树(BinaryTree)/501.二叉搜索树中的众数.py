#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans=[]
        most=0
        last=None
        cnt=0

        def inorder(node):
            if not node: return 
            nonlocal ans,most,last,cnt
            if node.left: inorder(node.left)
            if node.val==last:
                cnt+=1
            else: cnt=1
            if cnt==most: ans.append(node.val)
            elif cnt>most:
                most=cnt
                ans=[node.val]
            last=node.val
            if node.right: inorder(node.right)

        inorder(root)
        return ans
# @lc code=end

