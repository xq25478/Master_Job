'''
给定一个数组 A[0,1,…,n-1]，
请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

'''
from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        left,right=[1]*n,[1]*n
        res = [1]*n

        for i in range(1,n):
            left[i] = left[i-1]*a[i-1]
            right[n-1-i] = right[n-i]*a[n-i]

        for i in range(n):
            res[i] = left[i]*right[i]
        return res