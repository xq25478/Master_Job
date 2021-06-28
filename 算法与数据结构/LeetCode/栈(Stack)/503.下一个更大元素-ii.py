#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #思路 单调栈
        n = len(nums)
        ans = [0]*n
        stack = []

        for i in range(2*n-1,-1,-1):
            #辅助数组
            while  stack and stack[-1] <= nums[i%n]:
                stack.pop()
            ans[i%n] = stack[-1] if stack else -1
            stack.append(nums[i%n])
        
        return ans
# @lc code=end
s = Solution()
print(s.nextGreaterElements([2,1,2,4,3]))
