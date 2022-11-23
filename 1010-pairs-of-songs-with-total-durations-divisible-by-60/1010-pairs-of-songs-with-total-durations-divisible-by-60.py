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
        
        