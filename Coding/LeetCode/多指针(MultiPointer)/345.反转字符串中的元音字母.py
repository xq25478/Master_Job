#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        low, high = 0, length-1
        s = list(s)
        res =['a','e','i','o','u','A','E','I','O','U']
        while low <= high: 
            while low< high and s[high] not in res:
                high-=1
            while low < high and s[low] not in res:
                low += 1
            s[low],s[high]  = s[high],s[low]
            low+=1
            high-=1
        return  "".join(s)
# @lc code=end
s = Solution()
print(s.reverseVowels('hello'))
