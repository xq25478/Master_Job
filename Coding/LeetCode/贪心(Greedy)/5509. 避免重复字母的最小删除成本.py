'''
给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。

返回使字符串任意相邻两个字母不相同的最小删除成本。

请注意，删除一个字符后，删除其他字符的成本不会改变。
'''
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        pre = 0
        ret = 0
        for i in range(1,n):
            if s[pre] == s[i]:
                if cost[pre] > cost[i]: #删除cost[i]
                    ret += cost[i]
                else:
                    ret += cost[pre]
                    pre = i
            else:
                pre = i
        return ret