class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #this problem can be rephrased as if sum(gas)>sum(cost), first an index from which if you start so that you can complete the loop
        # ==>if any blocker is found bigger than the current cummulative sum, it says that all the forces combined from the point where you started is not enough to tackle the blocker, hence reset and try from next starting index after the blocker
        
        if sum(gas)<sum(cost): return -1
        cumSum=0
        index=0
        for i in range(len(gas)):
            cumSum+=(gas[i]-cost[i])
            if cumSum<0:
                index=i+1
                cumSum=0
        return index