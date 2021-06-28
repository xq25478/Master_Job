'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "

'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        hash = [0]*26

        for i in range(len(s)):
            val = ord(s[i])-97
            hash[val] += 1
        
        for i in range(len(s)):
            val = ord(s[i])-97
            if hash[val] == 1:
                return s[i]

        return " "