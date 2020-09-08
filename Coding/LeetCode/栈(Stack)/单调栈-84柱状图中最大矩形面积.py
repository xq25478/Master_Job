from typing import List

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

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))