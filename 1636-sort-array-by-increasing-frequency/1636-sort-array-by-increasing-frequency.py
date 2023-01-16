class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """working code; commented for alter
        map=defaultdict(list)
        c=Counter(nums)
        for val in c:
            map[c[val]].extend([val]*c[val])
        res=[]
        print(map)
        for freq in sorted(map):
            res.extend(sorted(map[freq], reverse=True))
        return res
        """
            
        #status: correct
        #Analysis: Time O(n log n), Space O(n)
        #ref: 1/16/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day83/84C3Ai3QuestionsFromMostFrequentListOf3/10Day3/5+Blind75WeekOne7/14q,2q/dayDay3/7-,1.Pairs of Songs With Total Durations Divisible by 60Timed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Sort Array by Increasing FrequencyTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.beatifulArrangementTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.dailyTemperaturesTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),Blind75WeekOne1;9.Lowest Common Ancestor of a Binary Search TreeTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
        
        #try alter
        
        # c=Counter(nums)
        # return [[tuple[0]]*tuple[1]  for tuple in sorted(sorted(c.most_common(), key=lambda x: x[0], reverse=True), key=lambda y: y[1])]
    
        c=Counter(nums).most_common()
        #sort by value first in reverse then by frequency
        c.sort(reverse=True, key=lambda x: x[0])
        c.sort(key=lambda x : x[1])
        res=[]
        for tuple in c:
            val,freq=tuple[0],tuple[1]
            res.extend([val]*freq)
        return res
    
    
    
    