from collections import defaultdict
from typing import List

#127 单词接龙(https://leetcode-cn.com/problems/word-ladder/)
class Solution127:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        # Since all words are of same length.
        L = len(beginWord)
        all_combo_dict = defaultdict(list)

        #建立每个单词的通用状态
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)

        #BFS
        queue = [(beginWord,1)]
        visited = {beginWord:True}

        while queue:
            curr_word,level= queue.pop(0)
            for i in range(L):
                #中间状态
                inter_word = curr_word[:i]+"*"+curr_word[i+1:]
                for word in all_combo_dict[inter_word]:
                    if word==endWord:
                        return level+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word,level+1))
                all_combo_dict[inter_word] = []
        return 0

s127 = Solution127()
print(s127.ladderLength("hit","cog", ["hot","dot","dog","lot","log","cog"]))
