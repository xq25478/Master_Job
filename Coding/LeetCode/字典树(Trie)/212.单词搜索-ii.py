#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start

#Trie实现
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