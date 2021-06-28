---
title: LeetCode-字典树(Trie)
categories:
- 数据结构与算法
- LeetCode
tags:
- 字典树(Trie)
---

## 208 实现Trie 前缀树
<!--more-->
```
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
```
## 211 添加与搜索单词
采用DFS对.通配符进行搜索查询
```
class TrieNode:
    def __init__(self,val=None,is_end=False):
        self.val = val
        self.is_end = is_end
        self.next = {}

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.node

        for i in word:
            if i not in cur.next:
                cur.next[i] = TrieNode(i)
            cur = cur.next[i]
        cur.is_end = True


    #采用dfs进行搜索
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:return False

        cur = self.node
        n = len(word)

        def dfs(node:TrieNode,word:str,idx:int):
            if word[idx] == '.':
                for i in node.next:
                    if idx == n-1:
                        if node.next[i].is_end == True:
                            return True
                    else:
                        if dfs(node.next[i],word,idx+1):
                            return True
                return False
            else:
                return False if word[idx] not in node.next else node.next[word[idx]].is_end == True if idx == n-1 else dfs(node.next[word[idx]],word,idx+1)

        return dfs(cur,word,0)
```

## 212 单词搜索II
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

```
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

    def delete(self,word:str)->None:
        if self.search(word):
            tmp = self.node
            for i in word:
                tmp = tmp.next[i]

            tmp.is_end = False

from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #优化方向: 将字典节点加入到递归当中 减少重复判断的时间 26%
        def backTrack(ans,x,y,trie_node):
            if trie_node.is_end:
                word = ''.join(ans[:])
                ret.append(word)
                trie.delete(word)
            
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                if 0 <= dx + x < rows and 0 <= dy + y < cols and board[x+dx][y+dy]!='#':
                    word = board[dx+x][dy+y]
                    if word in trie_node.next:
                        board[x+dx][y+dy] = '#'
                        ans.append(word)
                        backTrack(ans,dx+x,dy+y,trie_node.next[word])
                        board[x+dx][y+dy] = word
                        ans.pop()
           
        #异常
        if not board or not board[0] or not words:return []

        #构建字典树
        trie = Trie()
        cur = trie.node #优化
        for w in words:
            trie.insert(w)

        #变量初始化
        rows = len(board)
        cols = len(board[0])
        ret = []

        for i in range(rows):
            for j in range(cols):
                word = board[i][j]
                if word in cur.next:
                    board[i][j] = '#'
                    backTrack([word],i,j,cur.next[word])
                    board[i][j] = word

        return ret
# @lc code=end
s = Solution()
print(s.findWords(
    [['a','b'],
     ['a','a']],
     ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
))
```

## 720 词典中最长的单词

给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

```
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
```