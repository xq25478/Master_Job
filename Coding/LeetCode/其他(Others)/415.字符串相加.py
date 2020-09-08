#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        res = []
        flag = 0
        i = 0

        while i < n1 or i < n2:
            add_1 = 0 if i >= n1 else int(num1[n1-1-i])
            add_2 = 0 if i >= n2 else  int(num2[n2-1-i])
            res.append(str((add_2+add_1+flag)%10))
            flag = (add_1+add_2+flag)//10 
            i += 1
            
        if flag == 1:
            res.append('1')

        return ''.join(res[::-1])

# @lc code=end
s = Solution()
print(s.addStrings('623','14506'))

