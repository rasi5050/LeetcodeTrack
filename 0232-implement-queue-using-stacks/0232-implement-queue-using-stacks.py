class MyQueue:
    """working code; commented for alter
    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        return self.q.append(x)

    def pop(self) -> int:
        return self.q.popleft()

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return False if self.q else True

    """
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

    #status: correct
    #Analysis: Time O(n) Space O(n)
    #ref: 1/16/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day83/84C3Ai3QuestionsFromMostFrequentListOf3/10Day3/5+Blind75WeekOne7/14q,2q/dayDay3/7-,1.balancedBinaryTreeTImed25Mins-x1pomo(12:30-13:00),2.linkedListCycleTimed25Mins-x1pomo(13:00-13:30),3.implement-x1pomo(13:30-14:00),4.implementQueueUsingStacksTimed25Mins-x1pomo(14:00-14:30),5.firstBadVersionTimed25Mins-x1pomo(14:30-15:00),6.implement-x1pomo(15:00-15:30),7.ransomNoteTImed25Mins-x1pomo(15:30-16:00),8.implement-x1pomo(16:00-16:30)=x8pomo(12:30-16:30)                   

    #alter; implement using 2 stacks
    def __init__(self):
        self.front=[]
        self.back=[]

    def push(self, x: int) -> None:
        while self.back:
            self.front.append(self.back.pop())
        self.front.append(x)

    def pop(self) -> int:
        while self.front:
            self.back.append(self.front.pop())
        return self.back.pop()

    def peek(self) -> int:
        if self.front:
            return self.front[0]
        return self.back[-1]

    def empty(self) -> bool:
        return False if (self.front or self.back) else True

