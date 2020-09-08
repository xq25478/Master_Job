#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
##########################DFS##################################
        # if not board:return
        # m = len(board)
        # n = len(board[0])

        # def dfs(i,j):
        #     if 0 <=i < m and 0 <= j < n  and board[i][j] == 'O':
        #         board[i][j] = 'A'
        #         dfs(i-1,j)
        #         dfs(i+1,j)
        #         dfs(i,j+1)
        #         dfs(i,j-1)

        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0 or i == m-1 or j == n-1:
        #             dfs(i,j)
    
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             board[i][j] = 'X'
        #         if board[i][j] == 'A':
        #             board[i][j] = 'O'
#############################BFS###########################################
        if not board:return
        m = len(board)
        n = len(board[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1 and board[i][j] == 'O':
                    queue.append((i,j))

        while queue:
            i,j = queue.popleft()
            if 0 <=i < m and 0 <= j < n  and board[i][j] == 'O':
                board[i][j] = 'A'
                queue.append((i-1,j))
                queue.append((i+1,j))
                queue.append((i,j+1))
                queue.append((i,j-1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'
# @lc code=end

