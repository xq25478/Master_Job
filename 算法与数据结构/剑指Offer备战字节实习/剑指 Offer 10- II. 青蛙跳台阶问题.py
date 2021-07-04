
arr = [False]*101
arr[1]=1
arr[2]=2
arr[0]=1
class Solution:
    def numWays(self, n: int) -> int:
        if n < 0 :
            return 0
        if arr[n]:
            return arr[n]

        arr[n] = self.numWays(n-1) + self.numWays(n-2)
        return arr[n]%1000000007
