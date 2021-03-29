from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        # 建Key
        for s in strs:
            if tuple(sorted(s)) not in hash:
                hash[tuple(sorted(s))] = []

        # 添Value
        for s in strs:
            hash[tuple(sorted(s))].append(s)
        return [i for i in hash.values()]