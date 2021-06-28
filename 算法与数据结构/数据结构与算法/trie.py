'''
Trie 树优于哈希表的另一个理由是，随着哈希表大小增加，
会出现大量的冲突，时间复杂度可能增加到 O(n)O(n)，其中 nn 
是插入的键的数量。与哈希表相比，Trie 树在存储多个具有相同
前缀的键时可以使用较少的空间。此时 Trie 树只需要 O(m)O(m) 的
时间复杂度，其中 mm 为键长。而在平衡树中查找键值需要 O(m \log n)O(mlogn) 时间复杂度。
'''
# 字典树节点
class Node:
    def __init__(self,val = None,next=[],isEnd = False):
        self.val = val
        self.next = {i.val: i for i in next}
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

    #搜索字典树中是否存在某个单词
    '''
    rtype:True if exsits otherwise false
    '''
    def search(self,word:str)->bool:
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

        def startWith(self,prefix:str)->bool:
            tmp = self.node
            for i in prefix:
                if i not in tmp.next:
                    return False
                tmp = tmp.next[i]
            
            return True

