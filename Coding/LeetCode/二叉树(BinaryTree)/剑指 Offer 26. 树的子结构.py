'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        
        if not B or not A:
            return False

        def dfs(A:TreeNode,B:TreeNode):
            if not B:
                return True
            if not A and B:
                return False

            return dfs(A.left,B.left) and dfs(A.right,B.right) if A.val == B.val else False

        stack = [A]

        while stack:
            _A = stack.pop()
            if dfs(_A,B):
                return True
            if _A.left:
                stack.append(_A.left)
            if _A.right:
                stack.append(_A.right)

        return False