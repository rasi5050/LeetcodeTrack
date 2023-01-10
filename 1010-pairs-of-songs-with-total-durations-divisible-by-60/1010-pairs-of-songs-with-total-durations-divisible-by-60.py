class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #convert problem into 2 sum by modding all value by 60
        for i in range(len(time)):
            time[i]%=60
        
        map={}
        total=0
        for t in time:
            # if t==0 and t in map:
            #     total+=map[t]
            if (60-t)%60 in map:
                total+=map[(60-t)%60]
            map[t] = map.get(t,0) + 1
        return total
                
        