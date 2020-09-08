#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
#################################倒序#########################
    def reverseWords(self, s: str) -> str:
        s = list(s)

        #处理后面空格
        while s and s[-1] == ' ':
            s.pop()

        #处理前面空格
        s = s[::-1]
        while s and s[-1] == ' ':
            s.pop()

        #依次反转每个单词即可
        n = len(s)
        res = []

        word = []
        for i in range(n):
            if s[i] != ' ':
                word.append(s[i])
            else:
                if word:
                    res.extend(word[::-1])
                    res.append(' ')
                    word = []

        res.extend(word[::-1])
        return ''.join(res)
###########################倒序#############################
    # def reverseWords(self, s: str) -> str:
    #     s = s.strip() # 删除首尾空格
    #     i = j = len(s) - 1
    #     res = []
    #     while i >= 0:
    #         while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
    #         res.append(s[i + 1: j + 1]) # 添加单词
    #         while s[i] == ' ': i -= 1 # 跳过单词间空格
    #         j = i # j 指向下个单词的尾字符
    #     return ' '.join(res) # 拼接并返回
# @lc code=end
s = Solution()
print(s.reverseWords('i m good'))

