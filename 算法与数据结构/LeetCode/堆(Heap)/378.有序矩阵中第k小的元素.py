#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # '''
        # 思路 维持一个长度为k的最大堆 对任意num 若num大于堆顶 不添加
        # 若num小于堆顶 加入 pop堆顶
        # 时间复杂度:O(n^2log(n))
        # '''
        # n = len(matrix)
        # heap = []
        # heapq.heapify(heap)

        # for i in range(n):
        #     for j in range(n):
        #         if len(heap) < k:
        #             heapq.heappush(heap,-matrix[i][j])
        #         else:
        #             val = -heapq.heappop(heap)
        #             if matrix[i][j] < val:
        #                 heapq.heappush(heap,-matrix[i][j])
        #             else:
        #                 heapq.heappush(heap,-val)

        # return -heapq.heappop(heap)
        '''
        思路 归并排序 依旧使用最小堆 维持一个全局最小值候选堆
        每次弹出一个最小值 弹出k-1后 堆顶就是第k最小值
        '''
        n = len(matrix)

        heap = [(matrix[i][0],i,0) for i in range(n)]
        heapq.heapify(heap)

        for _ in range(0,k-1):
            _,x,y = heapq.heappop(heap)
            if y!= n-1:
                heapq.heappush(heap,(matrix[x][y+1],x,y+1))

        return heapq.heappop(heap)[0]
# @lc code=end

