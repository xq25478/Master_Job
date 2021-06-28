#
# @lc app=leetcode.cn id=1535 lang=python3
#
# [1535] 找出数组游戏的赢家
#
from typing import List
# @lc code=start
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        prev = max(arr[0], arr[1])
        if k == 1:
            return prev

        consecutive = 1
        maxNum = prev
        length = len(arr)

        for i in range(2, length):
            curr = arr[i]
            if prev > curr:
                consecutive += 1
                if consecutive == k:
                    return prev
            else:
                prev = curr
                consecutive = 1
            maxNum = max(maxNum, curr)
        
        return maxNum
# @lc code=end
s = Solution()
print(s.getWinner([2,1,3,5,4,6,7],2))
