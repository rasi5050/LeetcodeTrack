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
        
    #status: correct:
    #ref:11/13/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day37/38:do,1.mergeKSortedListsTimed25Mins-x1pomo(12:00-12:30),2.implement-x2pomo(12:30-13:30),3.removeNthNodeFromEndOfListTimed25Mins-x1pomo(13:30-14:00),4.implement-x2pomo(14:00-15:00),5.reorderListTimed25Mins-x1pomo(15:00-15:30),6.implement-x2pomo(15:30-16:30),7.studyQueue-x1pomo(16:30-17:00),8.stackUsingQueuesTimed25Mins-x1pomo(17:00-17:30),9.implement-x2pomo(17:30-18:30)=x13pomo(12:00-18:30)
#analysis: Time O(n), space O(n)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()