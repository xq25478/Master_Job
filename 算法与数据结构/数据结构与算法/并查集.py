class UnionFind:
    def __init__(self,n):
        self.count = n  #记录连通分量
        self.fa = [i for i in range(n)]  #fa[i]表示i的父节点
        self.size = [1 for _ in range(n)]

    def find(self,x)->int:
        while x != self.fa[x]:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union(self,i,j): #连通任意两个节点
        x = self.find(i)
        y = self.find(j)

        if x == y:return

        ## 路径优化
        if self.size[x] > self.size[y]: 
            self.fa[y] = x
            self.size[x] += self.size[y]
        else:
            self.fa[x] = y
            self.size[y] += self.size[x]  
        self.count -= 1

    def getCount(self):
        return self.count

    def connected(self,i,j)->bool:
        return self.find(i) == self.find(j)




