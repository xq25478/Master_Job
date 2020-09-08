#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
from typing import List
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isVaild(l,r,s)->bool:
            num = 0
            i = r
            factor = 1
            if l == r:
                return True

            if int(s[l]) == 0:
                return False
            while i >= l:
                num += factor * int(s[i])
                factor*=10
                i-=1

            if num >= 0 and num <= 255:
                return True
            else:
                return False

        def backTrack(i,cnt,s):
            if i == n and cnt == 5:
                res.append(''.join(ans)[0:-1:1])
                return 
            if cnt == 5 and i < n:
                return 
                
            for j in range(i,n):
                if isVaild(i,j,s):
                    ans.append(s[i:j+1]+'.')
                    backTrack(j+1,cnt+1,s)
                    ans.pop()
        n = len(s)
        res = []
        ans = []
        backTrack(0,1,s)
        return res
# @lc code=end
s = Solution()
print(s.restoreIpAddresses("101023"))

