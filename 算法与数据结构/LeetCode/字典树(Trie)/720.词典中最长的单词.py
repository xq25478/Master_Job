#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
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

class Solution:
    from typing import List
    def longestWord(self, words: List[str]) -> str:
        def dfs(node:Node,s:str):
            nonlocal max_size
            nonlocal ret
            if len(s) > max_size:
                ret = s[:]
                max_size = len(s)
            elif len(s) == max_size:
                tmp = [s,ret]
                tmp.sort()
                ret = tmp[0]

            for i in node.next:
                if node.next[i].is_end == True:
                    dfs(node.next[i],s+i)

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        head = trie.node
        ret = ''
        max_size = 0

        dfs(head,'')

        return ret
# @lc code=end
s = Solution()
print(s.longestWord(["w","wo","wor","worl", "world"]))
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(s.longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]))