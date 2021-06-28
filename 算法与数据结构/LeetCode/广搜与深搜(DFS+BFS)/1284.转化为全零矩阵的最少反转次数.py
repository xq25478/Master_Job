#
# @lc app=leetcode.cn id=1284 lang=python3
#
# [1284] 转化为全零矩阵的最少反转次数
#
# @lc code=start
from typing import List
import queue
class Solution:
    #BFS
    def minFlips(self, mat: List[List[int]]) -> int:
    
        def encode(mat,m,n):
            x = 0
            for i in range(m):
                for j in range(n):
                    x = x*2 + mat[i][j]
            return x
        
        def decode(x,m,n):
            mat = [[0]*n for _ in range(m)]
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    mat[i][j] =  x&1
                    x >>= 1
            return mat
        
        def covert(mat,m,n,i,j):
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(0,0)]:
                i0,j0 = i+di,j+dj
                if 0 <= i0 < m and 0 <=j0 < n:
                    mat[i0][j0] ^= 1

        m,n = len(mat),len(mat[0])
        x_start,step=encode(mat,m,n),0

        if x_start == 0:
            return step
        
        visited = set()
        visited.add(x_start)
        q = queue.Queue()

        q.put_nowait(x_start)

        while not q.empty():
            step += 1
            k = q.qsize()

            for _ in range(k):
                status = decode(q.get_nowait(),m,n)
                for i in range(m):
                    for j in range(n):
                        covert(status,m,n,i,j)
                        x_cur = encode(status,m,n)
                        if x_cur == 0:
                            return step
                        if x_cur not in visited:
                            visited.add(x_cur)
                            q.put_nowait(x_cur)
                        covert(status,m,n,i,j)
        return -1     
# @lc code=end
s = Solution()
print(s.minFlips([[0,0],[0,1]]))