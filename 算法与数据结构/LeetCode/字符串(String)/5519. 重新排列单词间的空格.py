"""
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，
并且两个单词之间至少存在一个空格。题目测试用例保证 text 至少包含一个单词 。请你重新排列空格，使
每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请将
多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。返回 重新排
列空格后的字符串 。
"""
class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt_null,cnt_word = 0,0
        n = len(text)
        ch_pre = False
        index = []
        
        for i in range(n):
            if text[i] == ' ':
                cnt_null += 1
                ch_pre = False   
            else:
                if not ch_pre:
                    cnt_word += 1
                    index.append(i)
                ch_pre = True  
    
        ret = ''
        a = 0 if cnt_word == 1 else cnt_null // (cnt_word-1)
        b = cnt_null if cnt_word == 1 else cnt_null % (cnt_word-1)

        for i,idx in enumerate(index):
            while idx < n and text[idx] != ' ':
                ret += text[idx]
                idx += 1
            if i != len(index)-1:
                ret += ' '*a
        ret += ' '*b
        return ret
                
            