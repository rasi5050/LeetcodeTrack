from collections import defaultdict
from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #do brute force
        # count=0
        # for i in range(len(time)):
        #     for j in range(i+1, len(time)):
        #         if (time[i]+time[j])%60==0:
        #             count+=1
        # return count
        
        # for i in range(len(time)):
        #     for j in range(i, len(time)):
        #         print(time[i]+time[j])
        """#correct code, commented to try out alternate version
        timeMap=defaultdict(set)
        minTime, maxTime = 500, 1
        for i,item in enumerate(time):
            timeMap[item].add(i)
            minTime=item if item < minTime else minTime
            maxTime=item if item>maxTime else maxTime
        start,end=(minTime*2)//60, (maxTime*2)//60
        # possibleDurations=[60,120,180,240,300,360,420,480,540,600,660,720,780,840,900,960]
        possibleDurations=[60*i for i in range(start,end+1)]
                          
        totalPairs=0
        for i,item in enumerate(time):
            for duration in possibleDurations:
                if (duration-item) in timeMap:
                    pairs=len(timeMap[duration-item])
                    # same index case
                    if i in timeMap[duration-item]:            
                        pairs-=1
                    totalPairs+=pairs
                    pairs=0
            timeMap[item].remove(i)
        return totalPairs
        """
        
        #intuition: convert to 2sum problem, idea from leetcode discussion(https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60)
        """working code
        time=[eachTime%60 for eachTime in time]    
        timeCounter=Counter()
        totalPairs=0
        for t in time:
            if t==0:t=60
            if 60-t in timeCounter:
                totalPairs+=timeCounter[60-t]
            if t==60:t=0
            timeCounter[t]+=1
        return totalPairs
        """
        #alternate approach2 from leetcode discussion solution (https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60)
        c=[0] * 60
        res=0
        for t in time:
            res += c[-t % 60]     #-t % 60 equivalent to 60-t  #possible combinations till that number 
            c[t % 60] += 1          
        return res
    #status: correct
    #analysis: Time O(n), Space O(n)
    #ref: 11/23/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day46/46:1.(P1:doPaypalLeetcodeQuestion5/5;1.pairsOfSongsWithTotalDurationDivisibleBy60Timed25Mins-x1pomo(5:30-6:00,2.implement-x2pomo(6:00-7:00),3.timeNeededToRearangeABinaryStringTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.palantirDependencyGraphExplanation-x1pomo(8:30-9:00),6.subdomainVisitCountTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.basicCalculatorAnswers-x1pomo(10:30-11:00)=x11pomo(5:30-11:00)
