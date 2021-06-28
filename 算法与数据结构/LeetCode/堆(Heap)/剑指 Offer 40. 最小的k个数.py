import heapq
from typing import List
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#################################最大堆############################
        heap = []
        heapq.heapify(heap)

        n = len(arr)
        for i in range(n):
            if i < k:
                heapq.heappush(heap,-arr[i])
            else:
                val = -heapq.heappop(heap)
                if arr[i] < val:
                    heapq.heappush(heap,-arr[i])
                else:
                    heapq.heappush(heap,-val)
        return heap
    
###########################排序##############################