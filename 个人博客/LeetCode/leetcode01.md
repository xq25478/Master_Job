---
title: LeetCode01-两数之和
categories:
- LeetCode
tags:
- 哈希
- LeetCode
---
本题用到的数据结构便是哈希表,当以后碰到这种数组搜索问题的时候，便可以考虑采用这种空间换时间的思想。
<!--more-->
# 算法原理
参见[数据结构与算法-哈希表](https://xiaoqi25478.github.io/2020/07/12/ds_hashtable/)

#代码实现
```
from typing import List
#001 两数之和
class Solution001:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasp_map = {} #采用数组下标作为关键词 因为唯一
        for index,num in enumerate(nums):
            another = target -  num
            if another in hasp_map:
                return [hasp_map[another],index]
            hasp_map[num] = index
        return None
            
if __name__ == '__main__':
    s1 = Solution001()
    print(s1.twoSum([2,2,7,5,1],6))
```