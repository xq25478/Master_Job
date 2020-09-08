#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#
from typing import List
# @lc code=start
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        n = len(A)

        def get_num(l,r):
            res = 0
            i = 1
            for idx in range(r,l-1,-1):
                if A[idx] == 1:
                    res += i
                i = i*2
            return res

        counts_1 = []
        for i in range(n):
            if A[i] == 1:
                counts_1.append(i)

        if not counts_1:
            return [1,n-1]

        if len(counts_1) % 3 != 0:
                return [-1,-1]
        
        k = len(counts_1) // 3
        z = n-1 - counts_1[-1] #0的个数

        l = 0
        i = counts_1[k-1] + z
        j = counts_1[2*k-1] + z
        r = n-1
        if get_num(l,i) ==  get_num(i+1,j)and  get_num(i+1,j) == get_num(j+1,r):
            return [i,j+1]
        else:
            return [-1,-1]

# @lc code=end
s = Solution()
print(s.threeEqualParts([1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0]))

