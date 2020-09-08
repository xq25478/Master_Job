#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
from typing import List
import collections
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        res = []
        queue = [root]
        def bfs(queue):
            if len(queue) == 0 :
                return 
            res.append([ i.val for i in queue])
            queue = [childen for node in queue for childen in node.children]
            bfs(queue)
        bfs(queue)
        return res
# @lc code=end

