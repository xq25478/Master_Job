#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from typing import List
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        res = 0 #总的糖果数
        cur = 0 #当前小孩吃的糖果数
        end = 0 #顶点结束地方
        for i in range(N):
            if i == 0:
                cur = 1
                value = cur
            else:
                if ratings[i] >= ratings[i-1]:
                    cur = 1 if ratings[i] == ratings[i-1] else cur + 1
                    end = i
                    value = cur
                else:#ratings[i] < ratings[i-1]:
                    if i-end + 1 > value:
                        res += (i-end) if cur==1 else 0 # 此时需要调整顶点
                    else:
                        res += (i-end-1) if cur==1 else 0 #此时不需要调整顶点
                    cur = 1
            res += cur
        return res
# @lc code=end
s = Solution()
# print(s.candy([1,0,2]))
# print(s.candy([1,2,2]))
# print(s.candy([29,51,87,87,72,12]))
# print(s.candy([1,3,2,2,1]))#7
# print(s.candy([1,3,4,5,2]))
# print(s.candy([1,6,10,8,7,3,2]))
# print(s.candy([0,1,2,3,2,1]))
print(s.candy([1,2,3,1,0]))

