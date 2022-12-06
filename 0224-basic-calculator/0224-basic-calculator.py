class Solution:
    def calculate(self, s: str) -> int:
        #blind copy from https://www.youtube.com/watch?v=zsJ-J08Qgdk&t=482s   : didnot understand 
        cur = res = 0
        sign = 1
        stack = []
        
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in ['+','-']:
                res += sign * cur
                
                sign = 1 if char == '+' else -1
                
                cur=0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                
                sign=1
                
                res=0
            elif char == ')':
                res+=sign * cur
                res*=stack.pop()
                res+=stack.pop()
                
                cur=0
        return res + sign * cur
    
    #ref:12/6/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day52/52-connectMacChargerBeforeTurningOnInMorning:1.calculatorCopyAnswer(https://www.google.com/search?q=calculator+leetcode&rlz=1C5CHFA_enUS1021US1021&oq=calculator+leetcode&aqs=chrome..69i57.2208j0j4&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:aff25d29,vid:zsJ-J08Qgdk)Video-x1pomo(6:00-6:30),2.copyAnswer-x1pomo(6:30-7:00),3.dailyTemperaturesTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),3.trappingRainWaterTimed25Mins-x1pomo(8:30-9:00),4.implement-x2pomo(9:00-10:00),tuSimpleDay1/4D-1/5Q,1.longestIncreasingSubsequenceTimed25Mins-x1pomo(10:00-10:30),2.implement-x2pomo(10:30-11:30)=x11pomo(6:00-11:30)

                
        