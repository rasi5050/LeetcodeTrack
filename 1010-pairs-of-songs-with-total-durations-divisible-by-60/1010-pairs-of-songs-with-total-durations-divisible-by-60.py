from collections import defaultdict
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
        
        
        