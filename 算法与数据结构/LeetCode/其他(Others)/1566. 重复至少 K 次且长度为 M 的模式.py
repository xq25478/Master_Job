'''
给你一个正整数数组 arr，请你找出一个长度为 m 且在数组中至少重复 k 次的模式。

模式 是由一个或多个值组成的子数组（连续的子序列），连续 重复多次但 不重叠 。 模式由其长度和重复次数定义。

如果数组中存在至少重复 k 次且长度为 m 的模式，则返回 true ，否则返回  false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        def helper(i)->bool:
            for j in range(1,k):
                for p in range(m):
                    if i+j*m+p >= n or arr[i+j*m+p] != arr[i+p]:
                        return False
            return True

        n = len(arr)
        for i in range(n):
            if helper(i):
                return True

        return False