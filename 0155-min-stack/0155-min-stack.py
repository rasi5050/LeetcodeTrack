class MinStack:

    def __init__(self):
        self.stack=[]
        self.curMin=math.inf
    def push(self, val: int) -> None:
        if self.stack:
            self.curMin=min(val, self.stack[-1][1])
            self.stack.append([val, self.curMin])
                                  #store as [(val, minimumValueTillNow)]
        else:
            self.stack.append([val, val])
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        # print(self.stack)
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

