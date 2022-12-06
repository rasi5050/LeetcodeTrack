class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #do n^2
        # j=0
        # res=[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             res[i]=j-i
        #             break
        # return res
    #status:TLE, 
    #idea from neetcode youtube solution: half help: (https://www.youtube.com/watch?v=cTBiBSnjO3c&t=710s)
    
    
    
        stack=[(0,temperatures[0])]
        cur=1
        res=[0]*len(temperatures)
        while cur<len(temperatures):
            while stack and temperatures[cur]>stack[-1][1]:  #pop
                index,val=stack.pop()
                res[index]=cur-index
            stack.append((cur, temperatures[cur]))
            cur+=1
        return res
        # status: correct
        #analyis: Time: O(n), each element visited once
        #Sapce: O(n), since using stack to store intermediate results
        #ref:12/6/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day52/52-connectMacChargerBeforeTurningOnInMorning:1.calculatorCopyAnswer(https://www.google.com/search?q=calculator+leetcode&rlz=1C5CHFA_enUS1021US1021&oq=calculator+leetcode&aqs=chrome..69i57.2208j0j4&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:aff25d29,vid:zsJ-J08Qgdk)Video-x1pomo(6:00-6:30),2.copyAnswer-x1pomo(6:30-7:00),3.dailyTemperaturesTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),3.trappingRainWaterTimed25Mins-x1pomo(8:30-9:00),4.implement-x2pomo(9:00-10:00),tuSimpleDay1/4D-1/5Q,1.longestIncreasingSubsequenceTimed25Mins-x1pomo(10:00-10:30),2.implement-x2pomo(10:30-11:30)=x11pomo(6:00-11:30)

                
            
            
        