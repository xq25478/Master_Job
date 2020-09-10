#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
from typing import List
# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def addList(res:List[int], ans: List[int]):
            n1 = len(res)
            n2 = len(ans)
            arr = []
            flag = 0
            i = 0

            while i < n1 or i < n2:
                add_1 = 0 if i >= n1 else int(res[n1-1-i])
                add_2 = 0 if i >= n2 else  int(ans[n2-1-i])
                arr.append(str((add_2+add_1+flag)%10))
                flag = (add_1+add_2+flag)//10 
                i += 1
                
            if flag == 1:
                arr.append('1')
            return arr[::-1]

        n1 = len(num1)
        n2 = len(num2)
        if n2 > n1:
            num1,num2=num2,num1
            n1,n2=n2,n1

        res = []
        for idx2 in range(n2-1,-1,-1):
            ans = []
            flag = 0
            for idx1 in range(n1-1,-1,-1):
                val = int(num1[idx1])*int(num2[idx2]) + flag
                flag = val // 10
                val = val % 10
                ans.append(val)
            if flag:
                ans.append(flag)

            ans = ans[::-1]
            temp = [0]*(n2-1-idx2)
            ans.extend(temp)
            res = addList(res,ans)

        #剔除前缀0
        res= res[::-1]
        while len(res) > 1  and res[-1] == '0':
            res.pop()

        res = res[::-1]
        return ''.join(res)
# @lc code=end
s = Solution()
print(s.multiply('999','999'))
