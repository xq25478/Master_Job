'''
给你一个仅包含小写英文字母和 '?' 字符的字符串 s<var> </var>，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。

注意：你 不能 修改非 '?' 字符。

题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。
'''
class Solution:
    def modifyString(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
    
        for i in range(n):
            if arr[i] == '?':
                a1,a2 = '?','?'
                if 0 <= i-1 < n and arr[i-1] != '?':
                    a1 = arr[i-1]
                if 0 <= i+1 < n and arr[i+1] != '?':
                    a2 = arr[i+1]
                    
                for j in range(26):
                    if j!=ord(a1)-ord('a') and j!=ord(a2)-ord('a'):
                        arr[i] = chr(j+ord('a'))
                        
        return ''.join(arr)