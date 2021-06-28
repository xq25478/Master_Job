#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i2 = i3 = i5 = 0

        for _ in range (1,n):
            ugly = min(res[i2]*2,res[i3]*3,res[i5]*5)
            res.append(ugly)

            if ugly == res[i2]*2:
                i2+=1
            if ugly == res[i3]*3:
                i3+=1
            if ugly == res[i5]*5:
                i5+=1

        return res[n-1]
# @lc code=end

