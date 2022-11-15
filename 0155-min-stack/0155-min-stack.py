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
    
    #status: correct
    #analysis: Time O(n): depends on the size of the input
    #Space O(n): O(2n) space is used, n for each stacks
    #ref: 11/15/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day39/40:do,1.studyStacks-x1pomo(6:00-6:30),2.validParenthesesTimed25Mins-x1pomo(6:30-7:00),3.implement-x2pomo(7:00-8:00),4.minStackTimed25Mins-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.asteroidCollisionTimefd25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00)=x10pomo(6:00-11:00)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()