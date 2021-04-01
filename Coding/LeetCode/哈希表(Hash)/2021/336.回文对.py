#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
from typing import List
# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        palid_str = []

        rev_words = {}
        res =[]

        for idx,word in enumerate(words):
            rev_words[word[::-1]] = idx
            #本身就是回文串
            if word == word[::-1]:
                palid_str.append(idx)
            
        for idx,word in enumerate(words):
            if word:
                for i in range(len(word)):
                    left,right = word[:i],word[i:]
                    if left == left[::-1] and right in rev_words and idx != rev_words[right]:#左边回文 右边与其他构成回文  整体回文
                        res.append([rev_words[right],idx])
                    if right == right[::-1] and left in rev_words and idx != rev_words[left]:#右边回文 左边与其他构成回文  整体回文
                        res.append([idx,rev_words[left]])
            else:
                #空串与回文串(但不是本身)组成一对
                for loc in palid_str:
                    if loc!= idx:
                        res.append([idx,loc])
        return res
# @lc code=end
s = Solution()
print(s.palindromePairs(['abcd','dcba','lls','s','sssll']))

