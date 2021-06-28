#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
from typing import List
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #自己的解法 模拟每一分钟的橘子腐烂过程
        # rows = len(grid)
        # cols = len(grid[0])

        # def rot(i:int,j:int)->int:
        #     cnt = 0
        #     dij = [(0,1),(0,-1),(-1,0),(1,0)]
        #     for d in dij:
        #         _row = i + d[0]
        #         _col = j + d[1]
        #         if 0 <= _row < rows and 0 <= _col < cols and grid[_row][_col] == 1:
        #             grid[_row][_col] = 3 #本轮坏掉的新鲜橘子
        #             cnt += 1
        #     return cnt
    
        # def updateOranges():
        #     for i in range(rows):
        #         for j in range(cols):
        #             if grid[i][j] == 3:
        #                 grid[i][j] = 2 

        # def onceRot()->int:
        #     cnt = 0
        #     for i in range(rows):
        #         for j in range(cols):
        #             if grid[i][j] == 2:
        #                 cnt += rot(i,j)
        #     return cnt

        # def checkOranges()->int:
        #     cnt = 0
        #     for i in range(rows):
        #         for j in range(cols):
        #             if grid[i][j] ==1:
        #                 cnt += 1
        #     return cnt          

        # minute = 0
        # while True:
        #     cnt = onceRot()#
        #     if cnt > 0: #本轮有新鲜橘子被腐烂
        #         updateOranges()
        #         minute += 1
        #     else:       #本轮没有橘子被腐烂
        #         if checkOranges():
        #             return -1
        #         else:
        #             return minute     
############################################################################## 
        #正解 BFS(通常用于解决最短路径问题)
        rows = len(grid)
        cols = len(grid[0])

        rotten = {(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 2}
        fresh  = {(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 1}

        time  = 0
        while fresh:
            if not rotten:return -1

            rotten = {(i+di,j+dj) for i,j in rotten for di,dj in [(0,1),(0,-1),(1,0),(-1,0)] if (i+di,j+dj) in fresh}
            fresh -= rotten
            time += 1

        return time

# @lc code=end

