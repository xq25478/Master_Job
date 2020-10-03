#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hash = {}
        for stone in S:
            if stone not in hash:
                hash[stone] = 0
            else:
                hash[stone] += 1
        ret = 0
        for stone_type in J:
            if stone_type in hash:
                ret += hash[stone_type]

        return ret

import sys
import io
def readlines():
    for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
        yield line.strip('\n')   

if __name__ == "__main__":
    line = readlines()

# @lc code=end

