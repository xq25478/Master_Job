#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq
# @lc code=start
class MedianFinder:
    '''
    思路1 两个堆 一个维持较大一半的最小堆 一个维持较小一半的最大堆
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.min_szie = 0
        self.max_size = 0

    def addNum(self, num: int) -> None:

        #将新添加的元素给最大堆
        heapq.heappush(self.max_heap,-num)
        heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))

        self.min_szie += 1

        if self.max_size < self.min_szie:
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
            self.min_szie -= 1
            self.max_size += 1

    def findMedian(self) -> float:
        return -self.max_heap[0] if self.max_size > self.min_szie else \
            (self.min_heap[0] - self.max_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
s = MedianFinder()
s.addNum(7)
print(s.findMedian())
s.addNum(4)
print(s.findMedian())
s.addNum(5)
print(s.findMedian())

