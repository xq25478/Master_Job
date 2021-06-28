'''
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。
示例 1：
输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：

输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = []

        n = len(arr)
        for i in range(n):
            if i == 0:
                res += [val for val in range(1,arr[i])]
            else:
                res += [val for val in range(arr[i-1]+1,arr[i])]
        if len(res) >=  k:
            return res[k-1]
        else:
            if not res:
                return arr[-1] + k
            else:
                return arr[-1] + k - len(res)