#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v = 0
        h = 0
        for m in moves:
            if m == 'L':
                v -= 1
            elif m == 'R':
                v += 1
            elif m == 'U':
                h += 1
            else:
                h -= 1
        
        return v == 0 and h == 0
        
# @lc code=end

