'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

'''
class Solution:
    #思路 简单的动态规划
    def fib(self, n: int) -> int:
        dp_1 = 0
        dp_2 = 1
        if n == 0:
            return 0

        for _ in range(2,n+1):
            new_dp = dp_1 + dp_2
            dp_1,dp_2 = dp_2,new_dp
            
        return dp_2%1000000007