#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#
from typing import List
# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                if abs(arr[i]-arr[j]) <= a:
                    for k in range(j+1,n):
                        if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                            ans += 1
        return ans
# @lc code=end

