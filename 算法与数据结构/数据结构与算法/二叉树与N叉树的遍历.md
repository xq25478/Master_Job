# 二叉树遍历
* 前序:根-左-右
* 中序:左-根-右
* 后序:左-右-根
* [参考文章](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-er-cha-shu-suo-you-bian-li-mo-ban-ji-zhi-s/)

## 节点定义
```
class BSTNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
## 递归
```
def recuriveTraversal(root:BSTNode):
    if not root:
        return []
    #preOrder
    [root.val] + self.recuriveTraversal(root.left) + self.recuriveTraversal(root.right)

    #inOrder
    self.recuriveTraversal(root.left) + [root.val] + self.recuriveTraversal(root.right)

    #postOrder
    self.recuriveTraversal(root.left) + self.recuriveTraversal(root.right) + [root.val] 
```
## 非递归
```
def unRecuriveTraversal(root:BSTNode):
    if not root:return []
    res = []
    stack = [root]

    #preOrder 
    while stack:
        cur = stack.pop()
        res.append(cur.val)

        if cur.right:
            stack.append(cur.right)

        if cur.left:
            stack.append(cur.left)

    #inOrder
    while stack:
        cur = stack.pop()
        if cur.right:
            stack.append(cur.right)
        res.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        
    #postOrder
    while stack:
        cur = stack.pop()

        if cur.right:
            stack.append(cur.right)

        if cur.left:
            stack.append(cur.left)

        res.append(cur.val)
```
## 层序遍历
```
def sequenceTraversal(self,root:BSTNode):
    if not root:
        return []
    cur,res = [root],[]

    while cur:
        lay,layer = [],[]
        for node in cur:
            layer.append(node.val)
            if node.left:lay.append(node.left)
            if node.right:lay.append(node.right)
        cur = lay
        res.append(layer)
```
# N叉树遍历
## 节点
```
class NSTNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
```
## 递归
```
def recurive(self,root:NSTNode):
    if not root:return []

    #preOrder
    res = [root.val]
    for node in root.children:
        res += self.recurive(node)

    return res
```
## 非递归
```
def unRecurive(self,root:NSTNode):
    if not root:return []
    stack = [root]
    res = []
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        stack.extend(cur.children[::-1])
```