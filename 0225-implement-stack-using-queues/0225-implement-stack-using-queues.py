from queue import Queue
class MyStack:
    def __init__(self):
        self.q1=Queue()
        self.tempQ=Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        if self.q1.empty():
            return None
        else:
            while self.q1.qsize()>1:
                self.tempQ.put(self.q1.get())
            tempVar=self.q1.get()
            self.q1=self.tempQ
            self.tempQ=Queue()
            return tempVar
    def top(self) -> int:
        
        if self.q1.empty():
            return None
        else:
            while self.q1.qsize()>1:
                self.tempQ.put(self.q1.get())
            tempVar=self.q1.get()
            self.q1=self.tempQ
            self.tempQ=Queue()
            self.q1.put(tempVar)
            return tempVar
    def empty(self) -> bool:
        return self.q1.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()