class MyCircularQueue:
    #intuition: use 2 lists
    def __init__(self, k: int):
        self.q=[]
        self.qTemp=[]
        self.k=k

    def enQueue(self, value: int) -> bool:
        if len(self.q)<self.k:self.q.append(value);return True

    def deQueue(self) -> bool:
        if self.q:
            for _ in range(len(self.q)-1):
                self.qTemp.append(self.q.pop())
            tempVar=self.q.pop()
            for _ in range(len(self.qTemp)):
                self.q.append(self.qTemp.pop())
            return True

    def Front(self) -> int:
        if self.q:
            for _ in range(len(self.q)-1):
                self.qTemp.append(self.q.pop())
            tempVar=self.q.pop()
            self.q.append(tempVar)
            for _ in range(len(self.qTemp)):
                self.q.append(self.qTemp.pop())
            return tempVar
        else:return -1

    def Rear(self) -> int:
        return self.q[-1] if self.q else -1

    def isEmpty(self) -> bool:
        return False if self.q else True

    def isFull(self) -> bool:
        return True if len(self.q)==self.k else False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()