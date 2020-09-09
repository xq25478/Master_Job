#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        res = []
        vaild = 0
        flag = False
        rows = len(board)
        cols = len(board[0])
        if cols == 1 and rows == 1:
            return board[0][0] == word

        visited = [[False]*cols for _ in range(rows)]

        def backTrack(i,j):
            nonlocal flag
            nonlocal vaild
            if ''.join(res) == word:
                flag = True
                return 
            if board[i][j] ==  word[vaild] and visited[i][j] ==  False:
                vaild += 1
                res.append(board[i][j])
                visited[i][j] = True
                #print(res,i,j,vaild)
                if i > 0:
                    backTrack(i-1,j)
                    if flag:#这里必须要添加！！！因为上一行找到了就不需要再找
                        return
                if j > 0:    
                    backTrack(i,j-1)  
                    if flag:#这里必须要添加！！！因为上一行找到了就不需要再找
                        return
                if  i < rows-1:
                    backTrack(i+1,j)     
                    if flag:#这里必须要添加！！！因为上一行找到了就不需要再找
                        return
                if j < cols-1:
                    backTrack(i,j+1)
                    if flag:#这里必须要添加！！！因为上一行找到了就不需要再找
                        return
                visited[i][j] = False
                res.pop()
                vaild -= 1
         
        for i in range(rows):
            for j in range(cols):
                if flag:
                    return True
                backTrack(i,j)
        return flag
# @lc code=end
s = Solution()
# print(s.exist
# ([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ],"ABCB"
# ))
print(s.exist
([
  ['a'],
],"a"
))

