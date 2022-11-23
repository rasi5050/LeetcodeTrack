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
        for i,item in enumerate(time):
            timeMap[item].add(i)

        possibleDurations=[60,120,180,240,300,360,420,480,540,600,660,720,780,840,900,960]
                          
        totalPairs=0
        for i,item in enumerate(time):
            for duration in possibleDurations:
                if (duration-item) in timeMap:
                    pairs=len(timeMap[duration-item])
                    # print("item ", item , "duration-item ",duration-item,timeMap, "len ", pairs)
                    # same index case
                    if i in timeMap[duration-item]:            
                        pairs-=1
                    totalPairs+=pairs
                    pairs=0
            timeMap[item].remove(i)
            if len(timeMap[item])==0: del timeMap[item]
            # print(totalPairs)
        return totalPairs
        
        
        