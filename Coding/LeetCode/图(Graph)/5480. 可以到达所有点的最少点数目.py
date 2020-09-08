class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        arr = [i for i in range(n)]
        
        for edge in edges:
            arr[edge[1]] = -1
            
        return [i for i in arr if i != -1]

        