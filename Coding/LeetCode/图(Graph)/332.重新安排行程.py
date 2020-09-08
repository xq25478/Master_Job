#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
from typing import List
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import collections
        #DFS 不需要进行回溯
        #题目保证至少存在一条合理的行程 也就是说每次从字典序中取出最小的一个路径 直到取出的路径不存在终点
        #那个不存在终点的路径一定是最终的行程终点  巧妙之处在于通过后序遍历避开进入死胡同问题
        def dfs(name:str):
            while hash[name]:
                dfs(hash[name].pop())
            ans.append(name)

        hash = collections.defaultdict(list)
        for ticket in tickets:
            hash[ticket[0]] += [ticket[1]]


        #对邻接表进行排序
        for h in hash:
            hash[h].sort(reverse=True)

        ans = []
        dfs('AFK')
        return ans[::-1]
# @lc code=end
s = Solution()
print(s.findItinerary(
[
["AFK","C"],["C","AFK"],["AFK","B"]
]
))
