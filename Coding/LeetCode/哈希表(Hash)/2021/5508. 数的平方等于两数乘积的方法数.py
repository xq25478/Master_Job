'''
给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：

类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length
类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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
