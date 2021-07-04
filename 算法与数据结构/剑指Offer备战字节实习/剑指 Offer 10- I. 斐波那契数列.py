class Solution:
    def __init__(self):
        self.fibonacci = [False]*101
        self.fibonacci[0]=0
        self.fibonacci[1]=1
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n ==  1:
            return 1
        if not self.fibonacci[n]:
            self.fibonacci[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.fibonacci[n]%1000000007

        