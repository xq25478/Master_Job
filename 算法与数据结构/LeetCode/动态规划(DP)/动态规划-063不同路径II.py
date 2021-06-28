from typing import List
'''
(i,j) 位置只能从 (i - 1, j)(i−1,j) 和 (i, j - 1)(i,j−1) 走到，这样的条件就是在告诉我们这里转移是 「无后效性」 的，
f(i, j)f(i,j) 和任何的 f(i', j')(i' > i, j' > j)f(i 
′,j  )(i ′>i,j >j) 无关。
动态规划的题目分为两大类，一种是求最优解类，典型问题是背包问题，另一种就是计数类，比如这里的统计方案数的问题，它们都存在一定的递推性质。
前者的递推性质还有一个名字，叫做 「最优子结构」 ——即当前问题的最优解取决于子问题的最优解，后者类似，当前问题的方案数取决于子问题的方案数。
所以在遇到求方案数的问题时，我们可以往动态规划的方向考虑。
'''
class Solution063:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 0:
                    if r == 0 and c == 0:
                        obstacleGrid[r][c] = 1
                    else:
                        left = obstacleGrid[r][c-1] if c > 0 else 0
                        up = obstacleGrid[r-1][c] if r > 0 else 0
                        obstacleGrid[r][c] = left + up
                else:
                    obstacleGrid[r][c] = 0
        return obstacleGrid[rows-1][cols-1]