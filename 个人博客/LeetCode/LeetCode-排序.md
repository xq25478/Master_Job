---
title: LeetCode-排序
categories:
- 数据结构与算法
- LeetCode
tags:
- 排序
---

## 剑指 Offer 45. 把数组排成最小的数
此题求拼接起来的 “最小数字” ，本质上是一个排序问题。排序判断规则： 设nums任意两数字的字符串格式x和y，则

若拼接字符串 x + y > y + x，则 m > n

反之，若 x + y < y + x，则 n < m

根据以上规则，套用任何排序方法对 nums 执行排序即可。

<!--more-->
采用快速排序实现
```
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def fast_sort(l , r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)
        
        strs = [str(num) for num in nums]
        fast_sort(0, len(strs) - 1)
        return ''.join(strs)
```

## 剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

```
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def _mergeSort(arr:List[int],temp:List[int],left:int,mid:int,right:int)->int:
            inv_count = 0
            #arr_copy = arr[:]  #每次申请临时数组极为耗费时间 删除
            #对两个子数组进行排序归并成大数组
            i = left
            j = mid + 1
            k = left

            #数组的两边已经分别有序 只需进行选择排序即可
            while ( i<= mid ) and ( j <= right ):
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                    inv_count += j-mid-1
                else :
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i <= mid :
                temp[k] = arr[i]
                k += 1
                i += 1
                inv_count += j-mid-1

            while j <= right:
                temp[k] = arr[j]
                k += 1
                j += 1  

            nums[left:right+1] = temp[left:right+1]
            return inv_count
            
        #递归式归并排序 自顶向下
        def mergeSortRecursive(arr:List[int],temp:List[int],left:int,right:int):
            inv_count = 0
            if left < right :
                mid = (left+right)//2
                inv_count = mergeSortRecursive(arr,temp,left,mid) + mergeSortRecursive(arr,temp,mid+1,right)
                inv_count += _mergeSort(arr,temp,left,mid,right)

            return inv_count

        if not nums: return 0
        temp = [0]*len(nums)
        return mergeSortRecursive(nums,temp,0,len(nums)-1)
```

## 350 两个数组的交集II
给定两个数组，编写一个函数来计算它们的交集。
```
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #排序
        len1 = len(nums1)
        len2 = len(nums2)
        nums1.sort()
        nums2.sort()
        res = []
        index1 = 0
        index2 = 0
        while index1 < len1 and index2 < len2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
        return res

```

## 合并区间
给出一个区间的集合，请合并所有重叠的区间。
```
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0]) #按照第0轴排序
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged
```

