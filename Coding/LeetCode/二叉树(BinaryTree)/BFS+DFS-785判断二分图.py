from typing import List
import collections

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #dfs
        n = len(graph)
        UNCOLORED,RED,BLUE = 0,1,2
        color_group = [UNCOLORED]*n
        valid = True

        def dfs(node,color):
            nonlocal valid
            color_group[node] = color
            c_next = RED if color == BLUE else BLUE
            for num in graph[node]:
                if color_group[num] == UNCOLORED:
                    dfs(num,c_next)
                    if not valid:
                        return
                elif color_group[num] == color:
                    valid = False
                    return 
        for i in range(n):
            if color_group[i] == UNCOLORED:
                dfs(i,RED) 
                if not valid:
                    break
        return valid

    def isBipartiteBFS(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED,RED,BLUE = 0,1,2
        color_group = [UNCOLORED]*n

        for i in range(n):
            if color_group[i] == UNCOLORED:
                color_group[i] = RED
                q = collections.deque([i])
                while q:
                    node = q.popleft()
                    cNei = (BLUE if color_group[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color_group[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color_group[neighbor] = cNei
                        elif color_group[neighbor] != cNei:
                            return False
        return True
s =Solution()
print(s.isBipartiteBFS([[1,3], [0,2], [1,3], [0,2]]))