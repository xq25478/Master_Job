---
title: LeetCode-位运算
categories:
- 数据结构与算法
- LeetCode
tags:
- 位运算
---

## 剑指Offer64 求1+2+3...+n
<!--more-->
不使用if else while for 等等
```
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res
```
## 剑指 Offer 65 不用加减乘除做加法
* [题解](链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/)
```
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

```

## 剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
```
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0 
        for i in range(len(nums)):
            res ^= nums[i]

        div = 1
        while div & res == 0:
            div <<= 1
        
        a = 0
        b = 0
        for i in range(len(nums)):
            if nums[i] & div:
                a ^= nums[i]
            else:
                b ^= nums[i]

        return [a,b]
```

## 201 数字范围按位与
给定范围[m, n],其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与(包含 m, n 两端点)。