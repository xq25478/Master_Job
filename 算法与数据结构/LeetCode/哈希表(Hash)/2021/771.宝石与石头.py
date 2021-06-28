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
                hash[stone] = 1
            else:
                hash[stone] += 1
        ret = 0
        for stone_type in J:
            if stone_type in hash:
                ret += hash[stone_type]

        return ret
# @lc code=end
s = Solution()
print(s.numJewelsInStones('aA','aAAbbbBBB'))
