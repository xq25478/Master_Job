import queue

#双端队列
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value :
            self.deque.pop()

        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
      
        return ans