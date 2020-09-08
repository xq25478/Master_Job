##############LeetCode之回溯算法##################
#有关回溯算法的讲解:https://baike.baidu.com/item/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95/9258495?fr=aladdin
import numpy as np 
from typing import List

#037 解数独(https://leetcode-cn.com/problems/sudoku-solver/)
class Solution037:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        作者：yybeta
        链接：https://leetcode-cn.com/problems/sudoku-solver/solution/pythonsethui-su-chao-guo-95-by-mai-mai-mai-mai-zi/
        执行用时：96 ms, 在所有 Python3 提交中击败了90.77%的用户
        内存消耗：13.8 MB, 在所有 Python3 提交中击败了11.11% 的用户
        """
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)] # 块剩余可用数字

        empty = [] # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':# 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i//3)*3+j//3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):
                return True
            i,j = empty[iter]
            b = (i//3)*3+j//3
            for val in row[i] & col[j] & block[b]:#该元素在三个表格中均存在的话 进行填写
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()
        return board #调试添加

if __name__ == '__main__':
    s = Solution037()
    res = s.solveSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]])
    print(res)
