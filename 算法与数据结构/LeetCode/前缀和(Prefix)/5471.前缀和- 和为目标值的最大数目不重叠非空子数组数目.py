'''
给你一个数组 nums 和一个整数 target 。

请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。

示例 1：

输入：nums = [1,1,1,1,1], target = 2
输出：2
解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
示例 2：

输入：nums = [-1,3,5,1,4,2,-9], target = 6
输出：2
解释：总共有 3 个子数组和为 6 。
([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。
示例 3：

输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
输出：3
示例 4：

输入：nums = [0,0,0], target = 0
输出：3

提示：
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
'''
from typing import List
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """ 贪心：从左向右寻找第一个符合要求的子数组，发现后重置，并继续查找
        pre记录当前的前缀和，初始为0
        mp记录出现过的前缀和，题目要求不重叠，故使用set实现即可，初始只含0
        当发现有pre[i] - pre[j] == target (j < i)时，表示发现一个满足要求的子数组
            即pre - target in mp
            此时应: ans += 1，且初始化 mp 和 pre
        否则在mp中记录该前缀和
        """
        mp = set([0])
        pre = 0  # 前缀和
        ans = 0
        for n in nums:
            pre += n
            if pre - target in mp:
                ans += 1
                mp = set([0])
                pre = 0
            else:
                mp.add(pre)
        return ans