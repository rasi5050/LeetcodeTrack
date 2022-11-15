class MinStack:
    #intuition: 2 stacks, maintain minimum at each point in separate stack: idea from neetcode youtube solution(https://www.youtube.com/watch?v=qkLl7nAwDPo)
    def __init__(self):
        self.stack=[]
        self.minStack=[]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
        
    def pop(self) -> None:        
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()