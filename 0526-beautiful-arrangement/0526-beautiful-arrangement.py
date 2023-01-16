class Solution:
    def countArrangement(self, n: int) -> int:
        """working code;improve
        count=[0]
        visited=set()
        perm=[]
        def recurse(curr):
            if len(perm)==n:
                count[0]+=1
            
            for i in range(1, n+1):
                if ((len(perm)+1)%i==0 or i%(len(perm)+1)==0) and i not in visited:
                    perm.append(i)
                    visited.add(i)
                    recurse(i)
                    visited.remove(perm.pop())
        
                
        recurse(0)   #dummy value to start
        return count[0]
        """        
        #status: correct
        #Analysis: Time O(n^n), Space O(n)
        #ref: 1/16/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day83/84C3Ai3QuestionsFromMostFrequentListOf3/10Day3/5+Blind75WeekOne7/14q,2q/dayDay3/7-,1.Pairs of Songs With Total Durations Divisible by 60Timed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Sort Array by Increasing FrequencyTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.beatifulArrangementTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.dailyTemperaturesTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),Blind75WeekOne1;9.Lowest Common Ancestor of a Binary Search TreeTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
        
        
        #intui
        count=[0]
        visited=set()
        def recurse(curr):
            if curr==n:
                count[0]+=1
            
            for i in range(1, n+1):
                if ((curr+1)%i==0 or i%(curr+1)==0) and i not in visited:
                    visited.add(i)
                    recurse(curr+1)
                    visited.remove(i)    
        recurse(1)   #dummy value to start
        return count[0]