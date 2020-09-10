#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Node:
    def __init__(self,val = None,isEnd = False):
        self.val = val
        self.next = {}
        self.is_end = isEnd

class Trie:
    def __init__(self):
        self.node = Node()
    
    def insert(self,word:str)->None:
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                tmp.next[i] = Node(i)
            tmp = tmp.next[i]
        tmp.is_end = True

    def search(self, word: str) -> bool:
        tmp = self.node
        for i in word[:-1]:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]

        if word[-1] not in tmp.next:
            return False

        if tmp.next[word[-1]].is_end:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        tmp = self.node
        for i in prefix:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        
        return True

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ''

        trie = Trie()
        for word in strs:
            if not word:
                return ''
            trie.insert(word)

        temp = trie.node
        ret = ''
        cnt = 0

        while len(temp.next) == 1:
            temp = temp.next[word[cnt]]
            ret += word[cnt]
            if temp.is_end:
                return ret
            cnt += 1

        return ret
# @lc code=end
s = Solution()
print(s.longestCommonPrefix(['a','aa']))

