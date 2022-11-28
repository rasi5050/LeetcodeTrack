from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #convert all time to %60, then its 2sum Problem
        
        time = [-i%60 for i in time]
        map=defaultdict(list)
        count=0
        
        # print(time)
        
        for i,t in enumerate(time):
            if (60-t)%60 in map:
                count+=len(map[(60-t)%60])
            # elif (t==0 and t in map):
            #     count+=len(map[t])
            map[t].append(i)
        # print(map)
        return count
        
            