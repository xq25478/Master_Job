#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#
from typing import List
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:return -1
        n = len(nums)
        s = sum(nums)

        pre_fix = [0]*(n+1)

        for i in range(1,n+1):#pre_fix[i] [0,i-1]
            pre_fix[i] = pre_fix[i-1] + nums[i-1]

        for i in range(n):
            if pre_fix[i] == s-pre_fix[i]-nums[i]:
                return i
        return -1
# @lc code=end
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))

