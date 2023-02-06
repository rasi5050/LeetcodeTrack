class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxSize=maxSize

    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1
        
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

#status: correct
#Analysis: Time O(n), Space O(n)
#ref: 2/6/2023P2:track1-cpGrind75;Day102/102;doLeetcodeBlind75-3q/day-16/45Q:completeOn2/15/2023-Day10/15:prepareTiktokDevOpsIntenseFocusDay3/7;1.(https://leetcode.com/problems/design-a-stack-with-increment-operation/)-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.(https://leetcode.com/discuss/interview-question/1263982/thomson-reuters-oa-circular-printer)-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.(https://leetcode.com/problems/count-sorted-vowel-strings/discuss/1021180/python-start-and-bars-explained)-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.absorber-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
