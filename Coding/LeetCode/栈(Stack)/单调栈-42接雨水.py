''' 042 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6 
'''
from typing import List
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

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))



