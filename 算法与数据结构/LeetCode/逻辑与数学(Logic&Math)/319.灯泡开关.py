#
# @lc app=leetcode.cn id=319 lang=python3
#
# [319] 灯泡开关
#
# 题解:https://zhuanlan.zhihu.com/c_1242508721932464128
# @lc code=start
class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        while i * i <=n:
            i += 1
        return i-1
# @lc code=end

