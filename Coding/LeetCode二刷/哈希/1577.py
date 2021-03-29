from typing import List

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import defaultdict
        hashmapnums1,hashmapnums2 = defaultdict(int),defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i + 1,len(nums1)):
                hashmapnums1[nums1[i] * nums1[j]] += 1
        for i in range(len(nums2)):
            for j in range(i + 1,len(nums2)):
                hashmapnums2[nums2[i] * nums2[j]] += 1
        ans = 0
        for i in range(len(nums1)):
            if nums1[i] ** 2 in hashmapnums2.keys():
                ans += hashmapnums2[nums1[i] ** 2]
        for i in range(len(nums2)):
            if nums2[i] ** 2 in hashmapnums1.keys():
                ans += hashmapnums1[nums2[i] ** 2]
        return ans
