'''
用两个栈实现一个队列。队列的声明如下，
请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

来源：力扣（LeetCode）

'''

class CQueue:
    '''
    思路 tail栈负责添加 head栈负责删除 两栈的元素加起来为队列当中的所有元素
    添加操作:直接在tail栈里面添加
    删除操作:先检查head是否为空 不为空直接pop 为空再检查tail 空表明队列没有元素 return -1 否则将tail里面的元素转移到
    head里面来
    '''
    def __init__(self):
        self.head = []
        self.tail = []

    def appendTail(self, value: int) -> None:
        self.tail.append(value)

    def deleteHead(self) -> int:
        if self.head:
            return self.head.pop()

        if not self.tail:
            return -1

        while self.tail:
            self.head.append(self.tail.pop())

        return self.head.pop() 

s = CQueue()
s.appendTail(3)
s.deleteHead()