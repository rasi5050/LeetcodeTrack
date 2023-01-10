class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mapVal={}
        
        mapFreq=defaultdict(list) #freq: val
        
        for n in nums:
            mapVal[n]=mapVal.get(n, 0)+1

        for val in mapVal:
            mapFreq[mapVal[val]].append(val)
        res=[]
        for freq in sorted(mapFreq):
            for val in sorted(mapFreq[freq])[::-1]:
                res=res+[val]*freq
        return res
    
    #status: correct
    #Analysis: Time O(nlogn * nlogn), Space O(n)
    #ref: 1/10/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day77/78-,1.checkGoldmanOaPreviousAttemptQuestion-x1pomo(5:30-6:00),2.do4.goldmanSachsOA;lastDate1/10/2023Oa-x3pomo(6:00-7:30),3.addQuestionsToDrive-x1pomo(7:30-8:00),4.Pairs of Songs With Total Durations Divisible by 60Timed25Mins-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.Sort Array by Increasing FrequencyTImed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00),8.Beautiful ArrangementTimed25Mins-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

            