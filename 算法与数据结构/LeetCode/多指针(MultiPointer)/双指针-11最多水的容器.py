from typing import List

#011 最多水的容器(https://leetcode-cn.com/problems/container-with-most-water/)
class Solution011:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            res = max(res, min(height[j],height[i]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res   
        