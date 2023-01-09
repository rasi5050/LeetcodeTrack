class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #do brute force
        """TLE
        res=[]
        for i in range(len(temperatures)):
            res.append(0)
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    res[i]=j-i
                    break
        return res
        """
        #use stacks
        res=[0]*len(temperatures)
        stack=[]
        
        for i, val in enumerate(temperatures):
            incoming = (val,i)
            while stack and stack[-1][0]<incoming[0]:
                (val,index) = stack.pop()
                res[index]=i-index
            stack.append(incoming)
        return res
        #status: correct
        #Analysis: Time O(n); traversing tru all elements once
        #Space O(n); for storing resultant array
        #ref: 1/8/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day75/76-c3AiDay1/2,0.preserveStreak,1.dailyTemperaturesTImed25Mins-x1pomo(18:00-18:30),2.implement-x2pomo(18:30-19:30),3.absorber-x1pomo(19:30-20:00)=x4pomo(18:00-20:00)

        
                    
                