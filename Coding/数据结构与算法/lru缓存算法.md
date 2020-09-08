# LRU缓存算法
* lru结构:哈希链表
* lru淘汰策略:频率淘汰
* 新加入/新访问的节点放置队头
* 若缓存满，则删除队尾元素
* 参考《东哥的算法小抄》P351:LRU缓存机制

## 链表节点结构 包含前驱和后驱 键值对
```
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
```
## 双链表定义
```
class DoubleList:
    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None       
```
### 向链表头部添加节点
    def addFirst(self,x:Node):
        if self.len == 0:
            self.head = x
            self.head.next = self.tail
            self.tail = x
            self.tail.pre = self.head
        else:
            temp = self.head
            self.head = x
            x.next = temp
            temp.pre = x
        
        self.len += 1

### 删除某一结点
    def remove(self,x:Node):
        temp1 = x.pre
        temp2 = x.next
        temp1.next = temp2

        #如果是头节点
        if x.key == self.head.key:
            temp = self.head.next
            self.head = temp  
        else:
            pre_node = x.pre
            next_node = x.next
            pre_node.next = next_node
            if next_node:
                next_node.pre =  pre_node
        self.len -= 1
    
### 删除最后一个节点
    def removeLast(self):
        if self.len == 1:
            last = self.head
            self.head = None
            self.tail = None
        else:
            last = self.tail
            pre_node = self.tail
            pre_node.next = None
            self.tail = pre_node

        self.len -= 1
        return last

### 返回链表长度
```
def __len__(self):
    return self.len
```
### 打印链表信息
```
def printList(self):
    cur = self.head
    for _ in range(self.len):
        print((cur.key,cur.val),"->",end='')
        cur = cur.next
    print("")
```
## LRU类定义
class LRUCache:
### Init
```
def __init__(self,capacity):
    self.hash_table = {}
    self.capacity = capacity
    self.cache = DoubleList()
```
### 存入
```
def put(self,key,val):
    node = Node(key,val)
    if key in self.hash_table:
        self.cache.remove(self.hash_table[key])
        self.cache.addFirst(node)
        self.hash_table[key] = node
    else:
        if self.capacity == len(self.cache):
            last = self.cache.removeLast()
            del self.hash_table[last.key]
        self.cache.addFirst(node)
        self.hash_table[key] = node
```            
### 读取
```
def get(self,key):
    if key not in self.hash_table:
        print('key:%d not exsit!'%(key))
        return -1

    val = self.hash_table[key].val
    self.put(key,val)
    return val
```
### 打印
```
def printCache(self):
    self.cache.printList()
```

## 测试
```
cache = LRUCache(3)
cache.put(1,1)
cache.put(2,5)
cache.put(3,7)
cache.printCache()
cache.put(4,8)
cache.printCache()
cache.get(2)
cache.printCache()
```
    