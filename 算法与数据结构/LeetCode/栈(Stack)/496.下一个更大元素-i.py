#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #思路 单调栈
        n1 = len(nums1)
        n2 = len(nums2)

        ans = []
        stack = []
        hash = {}

        for i in range(n2-1,-1,-1):
            while  stack and stack[-1] <= nums2[i]:
                stack.pop()
            val = stack[-1] if stack else -1
            hash[nums2[i]] = val
            stack.append(nums2[i])

        for i in range(n1):
            ans.append(hash[nums1[i]])

        return ans
# @lc code=end
s =  Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))

