class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            currWord=[]
            currNum=[]
            
            #keep popping
            if char ==']':
                while stack[-1]!='[':
                    currWord.append(stack.pop())
                stack.pop()         #poping opening bracket
                curWord="".join(currWord)
                currWord=currWord[::-1]
                while stack and stack[-1].isdigit():
                    currNum.append(stack.pop())
                currNum=int("".join(currNum)[::-1])
                stack+=list(currWord*currNum)
            else:    
                stack.append(char)
        return ''.join(stack)
    
        #status: correct
        #Analaysis: Time O(n); traversing tru elements once
        #Space O(n); storing stack
        #ref: 1/8/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day75/76-c3AiDay1/2,0.preserveStreak,1.dailyTemperaturesTImed25Mins-x1pomo(18:00-18:30),2.implement-x2pomo(18:30-19:30),3.absorber-x1pomo(19:30-20:00)=x4pomo(18:00-20:00)

        