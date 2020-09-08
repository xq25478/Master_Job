'''
给你一个由若干 0 和 1 组成的二维网格 grid ，其中 0 表示水，而 1 表示陆地。岛屿由水平方向或竖直方向上相邻的 1 （陆地）连接形成。
如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。
一天内，可以将任何单个陆地单元（1）更改为水单元（0）。
'''
from typing import List
class UnionFind:
    def __init__(self, n):  # n 为总节点数，从0开始标号
        self.n = n
        self.fa = [i for i in range(n)]  # fa[i]是i节点的家长节点编号
        # 由于路径压缩只在查询时进行，因此要依靠秩矩阵进行带秩合并(让树平缓)
        self.rank = [1 for _ in range(n)]  # rank[i]是树的高度

    def find(self, x):  # 带有压缩路径的查询方法，避免成链
        if x == self.fa[x]:
            return x
        else:  # 直接指向同一族的家长节点
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]

    def union(self, i, j):  # 归并两点间的关系
        x, y = self.find(i), self.find(j)

        if self.rank[x] <= self.rank[y]:  # 选择秩比较大的节点作为家长节点
            self.fa[x] = y
        else:
            self.fa[y] = x

        if self.rank[x] == self.rank[y] and x != y:
            self.rank[y] += 1  # 如果深度相同且根节点不同，则新的根节点的深度+1

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        uf = UnionFind(row * col)
        island_pos = None
        land_count = 0
        map_pos = lambda t: t[0] * col + t[1]

        ## 1. 并查集查清有多少联通和联通的分量 ##
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    island_pos = (i, j)  # 任意一个陆地/联通分量
                    land_count += 1
                    for d in directions:
                        x, y = i + d[0], j + d[1]
                        if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                            uf.union(map_pos((i, j)), map_pos((x, y)))

        if not island_pos:  # 没有联通分量
            return 0

        pre_connect = -1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fa = uf.find(map_pos((i, j)))
                    if pre_connect == -1:
                        pre_connect = fa
                    elif pre_connect != fa:  # 多于一个联通分量
                        return 0
        ## end 1. ##
        if land_count == 1:  # 排除一个tarjan的特殊情况，即只有一块陆地时是无法被判断为割点的
            return 1  # 直接返回1即可

        # 2. 找到割点
        dfn, low = [0] * (row * col), [0] * (row * col)

        def tarjan(u_pos, parent=None, tick=1):  # 找割点的数量
            u = map_pos(u_pos)
            dfn[u] = low[u] = tick
            child_cnt = 0  # 联通子树数量
            for d in directions:
                v_pos = (u_pos[0] + d[0], u_pos[1] + d[1])
                if not (0 <= v_pos[0] < row and 0 <= v_pos[1] < col and grid[v_pos[0]][v_pos[1]] == 1):
                    continue
                v = map_pos(v_pos)
                if dfn[v] == 0:  # 未被访问过
                    if tarjan(v_pos, u_pos, tick + 1):  # 找到一个割点就返回
                        return True
                    low[u] = min(low[u], low[v])

                    child_cnt += 1

                    # 判断割点
                    q1 = parent is None and child_cnt >= 2  # 根节点至少有两个儿子时，根节点u是割点
                    q2 = parent and low[v] >= dfn[u]  # 非根节点，此时u是割点
                    if q1 or q2:  
                        return True

                elif v != parent:  # 已访问过
                    low[u] = min(low[u], dfn[v])
            return False

        return 1 if tarjan(island_pos) else 2