class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #convert to %60
        for i in range(len(time)):
            time[i]%=60
        #now its 2Sum problem for target=60
        count=0
        map=defaultdict(int)
        for j,val in enumerate(time):
            if (60-val)%60 in map:    #(60-val)%60 , here %60 is given to include the 0 case so that (60-0)%60 returns 0
                count+=map[(60-val)%60]
            map[val]+=1
        return count
    
    #status: correct
    #Analysis: Time O(n);one pass, Space O(n)
    #ref: 1/16/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day83/84C3Ai3QuestionsFromMostFrequentListOf3/10Day3/5+Blind75WeekOne7/14q,2q/dayDay3/7-,1.Pairs of Songs With Total Durations Divisible by 60Timed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Sort Array by Increasing FrequencyTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.beatifulArrangementTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.dailyTemperaturesTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),Blind75WeekOne1;9.Lowest Common Ancestor of a Binary Search TreeTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
