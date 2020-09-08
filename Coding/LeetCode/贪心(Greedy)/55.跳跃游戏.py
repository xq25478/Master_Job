#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List
import functools
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 自己
        # n = len(nums)
        # @functools.lru_cache(maxsize=None) #这道题必须使用缓存装饰器记忆化
        # def recursive(last,cur):
        #     if nums[cur] < last-cur:
        #         return False

        #     for i in range(cur-1,-1,-1):
        #         if recursive(cur,i):
        #             return True

        #     return nums[cur] >= last-cur if cur == 0 else False

        # for  i in range(n-2,-1,-1):
        #     if recursive(n-1,i):
        #         return True
        # return True if n == 1 else False

        #官解 更新最远可以到达的位置
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
# @lc code=end
s = Solution()
print(s.canJump([2,3,1,1,4]))

