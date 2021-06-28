---
title: LeetCode-栈
categories:
- 数据结构与算法
- LeetCode
tags:
- 栈
---

## 20 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。

左括号必须以正确的顺序闭合。
<!--more-->
```
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:return True
        n = len(s)
        if n & 1 == 1:return False

        s1 = []
        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                s1.append(s[i])
            else:
                if s1 and ( ( s1[-1] == '(' and s[i] == ')' ) \
                       or   ( s1[-1] == '[' and s[i] == ']' )  \
                       or   ( s1[-1] == '{' and s[i] == '}' ) ):
                    s1.pop()
                else:
                    return False

        return True if not s1 else False
```

## 946 验证栈序列
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。
```
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed or not popped:return True
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack 
```

## 剑指Offer30 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

```
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.min_stk:
            self.min_stk.append(x)
        else:
            if x > self.min_stk[-1]:
                self.min_stk.append(self.min_stk[-1])
            else:
                self.min_stk.append(x)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        
    def top(self) -> int:
        if len(self.stk):
            return self.stk[-1]

    def min(self) -> int:
        if len(self.min_stk):
            return self.min_stk[-1]
```

## 496 下一个更大元素-i
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

```
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #思路 单调栈
        n1 = len(nums1)
        n2 = len(nums2)

        ans = []
        stack = []
        hash = {}

        for i in range(n2-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            val = stack[-1] if stack else -1
            hash[nums2[i]] = val
            stack.append(nums2[i])

        for i in range(n1):
            ans.append(hash[nums1[i]])

        return ans
```

## 503 下一个更大元素-ii
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

```
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
```
## 556 下一个更大元素-iii
给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
```
```

## 42 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入: [0,1,0,2,1,0,1,3,2,1,2,1]

输出: 6 
```
class Solution:
    #单调递减栈
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3: return 0
        res, i = 0, 0
        stack = []
        while i < length:
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                bottom = height[stack.pop()] #水池底部高度
                if len(stack) == 0: #无左边界
                    break
                left = stack[-1]
                res += ( min(height[i],height[left])-bottom )*(i-left-1)
            stack.append(i)
            i += 1
        return res
```
## 柱状图中最大矩形面积
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

```
class Solution:
    #单调栈解法
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left =  [0]*n
        right = [0]*n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack= []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
```