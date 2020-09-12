#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]: 
        if not root:
            return []
        
        stack = [root]
        ret = []
        while stack:
            cnt,sum = 0,0.0
            lay = []
            for i in range(len(stack)):
                node = stack.pop()
                sum += node.val
                cnt += 1
                if node.right:
                    lay.append(node.right)
                if node.left:
                    lay.append(node.left)
            ret.append(sum/cnt)
            stack = lay[:]
        return ret

        
# @lc code=end

