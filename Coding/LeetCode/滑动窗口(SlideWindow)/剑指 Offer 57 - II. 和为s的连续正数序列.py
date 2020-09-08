from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
#思路1 滑动窗口
        start = 1
        right = 1

        sum = 0
        res = []

        while start <= right < target:
            if sum >= target:
                if sum == target:
                    res.append([i for i in range(start,right)])
                sum -= start
                start += 1
            else:
                sum += right
                right += 1

        return res
s = Solution()
print(s.findContinuousSequence(15))