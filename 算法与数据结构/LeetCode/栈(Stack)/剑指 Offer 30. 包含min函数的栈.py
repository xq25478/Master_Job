'''
定义栈的数据结构，请在该类型中实现一个能够得到栈
的最小元素的 min 函数在该栈中，调用 min、push 及 
pop 的时间复杂度都是 O(1)。
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.min_stk:
            self.min_stk.append(x)
        else:
            if x > self.min_stk[-1]:
                self.min_stk.append(self.min_stk[-1])
            else:
                self.min_stk.append(x)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        
    def top(self) -> int:
        if len(self.stk):
            return self.stk[-1]

    def min(self) -> int:
        if len(self.min_stk):
            return self.min_stk[-1]