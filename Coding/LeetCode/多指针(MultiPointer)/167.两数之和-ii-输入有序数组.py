#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #双指针解法 时间复杂度O(n)
        low,high = 0,len(numbers)-1

        while low < high:
            if  numbers[low] + numbers[high] < target:
                low += 1
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                return [low+1,high+1]
        return [-1,-1]
# @lc code=end
s = Solution()
print(s.twoSum([2,7,11,15],9))

