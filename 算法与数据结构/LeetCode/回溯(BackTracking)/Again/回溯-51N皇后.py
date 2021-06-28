#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return 
        res = []
        board = [['.']*n for _ in range(n)]

        def backTrack(board:List[List[str]],row:int):
            if row == n:
                temp =[]
                for i in range(len(board)):
                    temp.append(''.join(board[i]))
                res.append(temp)
                return 
            for col in range(n):
                if not isVaild(board,row,col):
                    continue
                board[row][col] = 'Q'
                backTrack(board,row+1)
                board[row][col] = '.'

        #是否可以在指定列存放Q
        def isVaild(board:List[List[str]],row:int,col:int)->bool:
            n = len(board[0])
            #列冲突
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            #行冲突
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            #左上方
            i,j= row-1,col-1
            while i >=0 and j >=0 :
                if board[i][j] == 'Q':
                    return False
                i-=1
                j-=1
            #右上方
            i,j=row-1,col+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            return True    
        backTrack(board,0)
        return res
s = Solution()
print(s.solveNQueens(4))
# @lc code=end

