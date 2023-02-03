class Solution:
    def calculate(self, s: str) -> int:
        #using stack
        stack=[]
        currNum=0
        prevOpr='+'
        for i,c in enumerate(s):
            if c.isdigit():
                currNum=currNum*10 + int(c)
            if c in {'+','-','*','/'} or i==len(s)-1:
                if prevOpr=='+':
                    stack.append(currNum)
                elif prevOpr=='-':
                    stack.append(-currNum)
                elif prevOpr=='*':
                    stack.append(int(stack.pop()*currNum))
                elif prevOpr=='/':
                    stack.append(int(stack.pop()/currNum))
                currNum=0
                prevOpr=c
        return sum(stack)
            
        #status: correct
        #Analysis: Time O(n), Space O(n); using stack
        #ref: 2/3/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day101/102;doLeetcodeBlind75-3q/day-14/45Q:completeOn2/15/2023-Day7/15:prepareTiktokDevOpsFullForceDay2/7;1.BasicCalculator2TImed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.BasicCalculator3TImed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.courseSchedule2Timed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.longestIncreasingPathInAMatrixTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.mergeIntervalsTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

                    
                
            
            
            
    
            