''' 041 缺失的第一个正整数
题目描述:给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
示例1:
输入: [1,2,0]
输出: 3

示例2:
输入: [3,4,-1,1]
输出: 2

示例3:
输入: [7,8,9,11,12]
输出: 1
'''
from typing import List

class Solution:
    #O(N)-O(N)
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash = {}
        n = len(nums)
        for num in nums:
            if num > 0 and num not in hash:
                hash[num] = True

        for i in range(1, n + 1):
            if i not in hash:
                return i
        return n + 1

    #O(N)-O(1) 利用数组本身为hash表的特点
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
