from collections import deque
class MyQueue:

    def __init__(self):
        self.q1=[]
        self.qTemp=[]

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while self.q1:
            self.qTemp.append(self.q1.pop())
        tempVar=self.qTemp.pop()
        while self.qTemp:
            self.q1.append(self.qTemp.pop())
        return tempVar

    def peek(self) -> int:
        while self.q1:
            self.qTemp.append(self.q1.pop())
        tempVar=self.qTemp.pop()
        self.q1.append(tempVar)
        while self.qTemp:
            self.q1.append(self.qTemp.pop())
        return tempVar

    def empty(self) -> bool:
        return True if len(self.q1)==0 else False
    #analysis time O(nk), n: no of elements, k=number of operations, since peek and pop take O(2k)
    #space: O(2n)=(n)
    
    
    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()