#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:return 0

        n = len(str)
        i = 0

        #排除空格
        while str[i] == ' ' and i < n:
            i += 1
        
        if i == n:#全是空格
            return 0
        
        if str[i]!='+' and str[i]!='-' and (ord(str[i]) > 57 or ord(str[i]) < 48): #非法首字符
            return 0

        ans = 0
        flag = True
        if str[i] == '-' or str[i]=='+':
            flag = True if str[i]== '+' else False 
            i += 1

        while i < n and 0 <= int(str[i]) <= 9:
            ans += int(str[i])
            temp = ans if flag else -ans
            if temp < -2**31:
                return -2**31
            if temp > 2**31-1:
                return 2**31 - 1
            ans = ans * 10
            i += 1
        

        return ans//10 if flag else -ans//10

# @lc code=end
s = Solution()
print(s.myAtoi('-91283472332'))

