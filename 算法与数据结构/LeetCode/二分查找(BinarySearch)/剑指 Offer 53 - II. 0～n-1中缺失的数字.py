'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，
并且每个数字都在范围0～n-1之内。在范围0～n-1内的n
个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(n)
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)
        #O(1)

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        return left 
s = Solution()
print(s.missingNumber([0,1,2,3,5]))