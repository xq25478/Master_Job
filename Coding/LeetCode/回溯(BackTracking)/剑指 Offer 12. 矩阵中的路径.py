'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
'''
import functools
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    '''
    思路 经典回溯
    '''
        if not board:
            return False
        if not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])
        self.visited = [[False]*cols for _ in range(rows)]

        def backTrack(row,col,cnt):
            if cnt == len(word):
                return True

            if board[row][col] == word[cnt]:
                if cnt == len(word)-1:
                    return True
                dij = [(-1,0),(1,0),(0,1),(0,-1)]
                for d in dij:
                    new_row = d[0] + row
                    new_col = d[1] + col
                    if 0 <= new_row < rows and 0 <= new_col < cols and self.visited[new_row][new_col] == False:
                        self.visited[new_row][new_col] = True
                        if  backTrack(new_row,new_col,cnt+1):
                            return True
                        self.visited[new_row][new_col] = False
            return False

        for i in range(rows):
            for j in range(cols):
                self.visited[i][j] = True
                if backTrack(i,j,0):
                    return True
                self.visited[i][j] = False
        return False
s = Solution()
print(
s.exist(
[
    ["q"],
],"q"

))