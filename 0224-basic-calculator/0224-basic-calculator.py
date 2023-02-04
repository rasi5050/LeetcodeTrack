class Solution:
    def calculate(self, s: str) -> int:
        currNum=0
        res=0
        sign=1
        stack=[]
        for i,c in enumerate(s):
            if c.isdigit():
                currNum=currNum*10 + int(c)
            elif c in {'+','-'}:
                res+=(sign*currNum)
                sign=1 if c=='+' else -1
                currNum=0
            elif c=='(':        #record the current state before going into parentheses, (res, sign) and reset both
                stack.append(res)
                stack.append(sign)
                sign=1
                res=0
            elif c==')':
                res+=(sign*currNum) #the last unproccessed currNum;because we were processing it when we found a operator, in this case we have to process it when we see ')'
            
                res*=stack.pop()
                res+=stack.pop()
                currNum=0
        return res+sign*currNum
    #status: correct; didnot understand; help(https://www.youtube.com/watch?v=zsJ-J08Qgdk&t=1188s)
    #Analysis: Time O(N), Space O(N)
    #ref: 2/4/2023P2:track1-cpGrind75;Day101/102;doLeetcodeBlind75-3q/day-14/45Q:completeOn2/15/2023-Day7/15:prepareTiktokDevOpsIntenseFocusDay2/7;1.BasicCalculator3TImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.longestIncreasingPathInAMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x1pomo(8:00-8:30),5.mergeIntervalsTimed25Mins-x1pomo(8:30-9:00),6.decodeStringTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        