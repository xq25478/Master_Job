class Solution70:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        a,b,res = 1,2,0
        
        for _ in range(3,n+1):
            res = a + b
            a = b
            b = res

a = Solution70()
print(a.climbStairs(28))