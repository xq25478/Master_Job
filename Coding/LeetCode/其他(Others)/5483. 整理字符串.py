'''
给你一个由大小写英文字母组成的字符串 s 。

一个整理好的字符串中，两个相邻字符 s[i] 和 s[i + 1] 不会同时满足下述条件：

0 <= i <= s.length - 2
s[i] 是小写字符，但 s[i + 1] 是相同的大写字符；反之亦然 。
请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。

请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。

注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。
'''
class Solution:
    def makeGood(self, s: str) -> str:
        
        s = list(s)
        n = len(s)
        
        while True:
            i = 0
            n = len(s)
            t=[]
            while i < n:
                if i + 1 < n and abs( ord(s[i+1])-ord(s[i]) ) == 32:
                    i += 2
                else:
                    t.append(s[i])
                    i += 1
            if t == s:
                break
            else:
                s = t[:]
                print(s)
                
        return ''.join(s)