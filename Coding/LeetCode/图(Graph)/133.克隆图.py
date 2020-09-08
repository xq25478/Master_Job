#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
# @lc code=start
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':  
        from collections import deque
#BFS
##通过hash map实现深拷贝
        ht = {}

        if not node:
            return 
        root = Node(node.val,[])
        ht[node] = root

        queue = deque()
        queue.append(node)

        while queue:
            temp = queue.popleft()
            for n in temp.neighbors:
                if n not in ht:
                    ht[n] = Node(n.val,[])
                    queue.append(n)
                ht[temp].neighbors.append(ht[n])
        return root

# @lc code=end