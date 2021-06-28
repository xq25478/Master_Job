
# 给你一个整数 n 和一个整数数组 rounds 。有一条圆形赛道由 n 个扇区组成，
# 扇区编号从 1 到 n 。现将在这条赛道上举办一场马拉松比赛，
# 该马拉松全程由 m 个阶段组成。其中，第 i 个阶段将会从扇区 rounds[i - 1] 开始，
# 到扇区 rounds[i] 结束。举例来说，第 1 阶段从 rounds[0] 开始，到 rounds[1] 结束。
# 请你以数组形式返回经过次数最多的那几个扇区，按扇区编号 升序 排列。
# 注意，赛道按扇区编号升序逆时针形成一个圆（请参见第一个示例）。

# 题目 blahblah 说了很长, 但仔细分析可以发现, 中间部分对结果完全没影响, 
# 中间不管有多少个值多少圈, 对于每个扇区增加的次数都是相同的
# 所以我们可以只考虑起点和终点, 简化为一圈的情况, 这一圈经过的扇
# 区是额外的部分, 最终结果只需要考虑起点和终点途径的扇区即可
# 注意终点可能小于起点, 这时候就要先从 1 到终点, 再从起点遍历
# 到 n 即可(因为最终结果要按顺序)
# 链接：https://leetcode-cn.com/problems/most-visited-sector-in-a-circular-track/solution/di-203-chang-zhou-sai-ti-jie-by-suibianfahui-3/

from typing import List
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s,e =  rounds[0],rounds[-1]
        if s <= e:
            return list(range(s,e+1))
        else:
            # [1, 终点]+[起点, n]
            return list(range(1, e + 1)) + list(range(s, n + 1))
                
s =  Solution()
print(s.mostVisited(4,[1,3,1,2]))