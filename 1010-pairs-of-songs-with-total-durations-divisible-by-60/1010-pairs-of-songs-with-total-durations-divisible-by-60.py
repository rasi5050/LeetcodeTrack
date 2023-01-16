class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #convert to %60
        for i in range(len(time)):
            time[i]%=60
        print(time)
        #now its 2Sum problem for target=60
        count=0
        map=defaultdict(int)
        for j,val in enumerate(time):
            if (60-val)%60 in map:
                count+=map[(60-val)%60]
            map[val]+=1
        return count