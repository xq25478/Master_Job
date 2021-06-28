#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
import heapq
from typing import List
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        使用hash统计出现频率
        '''
        hash = {}
        for num in nums:
            if num in hash:
                hash[num]+=1
            else:
                hash[num] = 1

        # 使用优先队列 维持一个长度为k的最小堆
        heap = []
        heapq.heapify(heap)
        for num in hash:
            if len(heap) == k:
                if heap[0][0] < hash[num]:
                    heapq.heapreplace(heap,[hash[num],num])
            else:
                heapq.heappush(heap,[hash[num],num])

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res
# @lc code=end
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],1))