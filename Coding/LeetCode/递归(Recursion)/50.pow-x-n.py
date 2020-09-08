#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
import functools
# @lc code=start
class Solution:
    
    @functools.lru_cache(maxsize=None)#lru缓存
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == -1:
            return 1/x

        if n%2==0:
            return self.myPow(x,n//2)*self.myPow(x,n//2)
        else:
            return x*self.myPow(x,n-1)
# @lc code=end
s = Solution()
print(s.myPow(2,-3))

