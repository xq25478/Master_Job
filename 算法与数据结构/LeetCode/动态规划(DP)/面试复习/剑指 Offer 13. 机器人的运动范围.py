class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0: return 0
        '''
        思路1 动态规划
        '''
        cnt = 1

        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True

        def check_cooridnate(number):
            hundreds = number // 100
            ten = (number-hundreds*100)//10
            last = number%10
            return hundreds + ten + last

        for i in range(m):
            for j in range(n):
                if dp[i][j] == False and check_cooridnate(i) + check_cooridnate(j) <= k:
                    dij = [(-1,0),(0,-1)] #判断上一个足迹是否是true 如果为true必然可以走到
                    for d in dij:
                        new_row = d[0] + i
                        new_col = d[1] + j
                        if 0 <= new_row < m and 0 <= new_col < n and dp[new_row][new_col] == True:
                            dp[i][j] = True
                            cnt+=1
                            break
        return cnt

        '''
        思路2 BFS 广度优先搜索 借助队列实现
        def check_cooridnate(number):
            hundreds = number // 100
            ten = (number-hundreds*100)//10
            last = number%10
            return hundreds + ten + last

        marked = set()  # 将访问过的点添加到集合marked中,从(0,0)开始
        queue = collections.deque()
        queue.append((0,0))
        while queue:
            x, y = queue.popleft()
            if (x,y) not in marked and self.check_cooridnate(x,y) <= k:
                marked.add((x,y)) 
                for dx, dy in [(1,0),(0,1)]:  # 仅考虑向右和向下即可
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        queue.append((x+dx,y+dy)) 
        return len(marked)     
        '''
        #思路3 DFS 深度优先搜索 借助栈实现 代码略
        
s = Solution()
print(s.movingCount(16,8,4))


