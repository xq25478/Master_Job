'''
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，
它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，
Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。

已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。

给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。
'''
from typing import List
class Solution:
    #最大化最小值 
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        #1.先求最小磁力的最小可能取值
        min_dis = float('inf')
        for i in range(n-1):
            min_dis = position[i+1]-position[i] if position[i+1] - position[i] < min_dis else min_dis

        #2.再求最小磁力的最大可能取值
        max_dis = (position[n-1]-position[0])/(m-1)   

        def check(mid,position,m):
            cnt = 0
            target = position[0] + mid
            for i in range(n-1):
                if position[i] < target and position[i+1] >= target:
                    cnt += 1
                    target = position[i+1] + mid

            return cnt >= m - 1


        #确定了最小值和最大值 开始进行二分搜索
        l,r = min_dis,max_dis
        while l <= r:
            mid = l + (r-l)//2     
            if check(mid,position,m):
                l = mid + 1
            else:
                r = mid - 1

        return int(l - 1)

