"""
给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。

在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。

返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为负数，则返回 -1 。

注意，取余是在得到最大积之后执行的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-non-negative-product-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        r, c = len(grid),len(grid[0])
        _min = [[0]*c for _ in range(r)]
        _max = [[0]*c for _ in range(r)]

        _min[0][0] = _max[0][0] = grid[0][0]
        for i in range(1,c):
            _min[0][i] = grid[0][i]*_min[0][i-1]
            _max[0][i] = grid[0][i]*_max[0][i-1]
        for j in range(1,r):
            _min[j][0] = grid[j][0]*_min[j-1][0]
            _max[j][0] = grid[j][0]*_max[j-1][0]

        for i in range(1,r):
            for j in range(1,c):
                _min[i][j] = min( 
                                    min(_min[i][j-1]*grid[i][j],_min[i-1][j]*grid[i][j]),
                                    min(_max[i][j-1]*grid[i][j],_max[i-1][j]*grid[i][j])
                                )           
                _max[i][j] = max( 
                                    max(_min[i][j-1]*grid[i][j],_min[i-1][j]*grid[i][j]),
                                    max(_max[i][j-1]*grid[i][j],_max[i-1][j]*grid[i][j])
                                )   

        return _max[r-1][c-1] % (10**9+7) if _max[r-1][c-1] >=0 else -1
