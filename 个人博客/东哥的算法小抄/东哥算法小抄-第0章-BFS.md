---
title: 《东哥的算法小抄》-第0章:BFS
categories:
- 数据结构与算法
tags:
- 《东哥的算法小抄》
- BFS
---

BFS和DFS都可以找到最短路径，但是DFS需要花费更高的时间复杂度，BFS需要花费更高的空间复杂度
## 二叉树的最小高度

```
int minDepth(TreeNode root) {
    if (root == null) return 0;
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);
    // root 本⾝就是⼀层，depth 初始化为 1
    int depth = 1;
    while (!q.isEmpty()) 
    {
    int sz = q.size();
    /* 将当前队列中的所有节点向四周扩散 */
    for (int i = 0; i < sz; i++) 
    {
        TreeNode cur = q.poll();
        /* 判断是否到达终点 */
        if (cur.left == null && cur.right == null)
            return depth;
        /* 将 cur 的相邻节点加⼊队列 */
        if (cur.left != null)
        {
            q.offer(cur.left);
        }
        if (cur.right != null)
        {
            q.offer(cur.right);
        }
        /* 这⾥增加步数 */
        depth++;
    }
    return depth;
}
```

## 双向BFS
* 传统的 BFS 框架就是从起点开始向四周扩散，遇到终点时停⽌；⽽双向 BFS 则是从起点和终点同时开始扩散，当两边有交集的时候停⽌。
* 不过，双向 BFS 也有局限，因为你必须知道终点在哪⾥