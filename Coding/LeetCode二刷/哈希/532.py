from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hash = {}
        for num in nums:
            hash[num] = 1 if num not in hash else hash[num] + 1

        ret = 0
        if k == 0:
            for key in hash:
                if hash[key] >= 2:
                    ret += 1
        else:
            for key in hash:
                if key + k in hash:
                    ret += 1
        return ret
