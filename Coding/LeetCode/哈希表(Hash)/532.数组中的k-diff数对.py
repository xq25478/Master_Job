#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = {}

        for num in nums:
            dic[num] = 1 if num not in dic else dic[num] + 1

        ret = 0
        if k == 0:
            for v in dic:
                if dic[v] >= 2:
                    ret += 1
        elif k > 0:
            for v in dic:
                if v + k in dic:
                    ret += 1           
        return ret
# @lc code=end

