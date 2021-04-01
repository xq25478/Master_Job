#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            if tuple(sorted(s)) not in hash:
                hash[tuple(sorted(s))] = []

        for s in strs:
            hash[tuple(sorted(s))].append(s)
        
        return [i for i in hash.values()]
# @lc code=end
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))