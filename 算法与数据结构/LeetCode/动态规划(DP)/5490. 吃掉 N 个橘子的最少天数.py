'''
5490. 吃掉 N 个橘子的最少天数
厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：

吃掉一个橘子。
如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
每天你只能从以上 3 种方案中选择一种方案。

请你返回吃掉所有 n 个橘子的最少天数。

'''
class Solution:
    def __init__(self):
        #离散化DP 
        self.dp = {}

    def minDays(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2 or n == 3:
            return 2
        
        if n in self.dp:
            return self.dp[n]

        ret = min(self.minDays(n // 2) + 1 + (n % 2),self.minDays(n // 3) + 1 + (n % 3));

        self.dp[n] = ret
        return ret

s = Solution()

print(s.minDays(100))