class CQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s1.append(value)

    def deleteHead(self) -> int:
        if not self.s2: # 要点 只有当队首空的时候才考虑将队尾的元素加入到队首
            while self.s1:
                self.s2.append(self.s1.pop())

        if not self.s2:   
            return -1
        return self.s2.pop()