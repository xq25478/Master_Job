#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
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

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
s = WordDictionary()
s.addWord('bad')
s.addWord('dad')
s.addWord('mad')
s.addWord('pad')
s.addWord('bad')
print(s.search('.ad'))
print(s.search('b..'))