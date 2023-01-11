class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        trailLen=len(gas)
    
        """working;TLE
        gas+=gas
        cost+=cost
        
        for x in range(trailLen):
            veh=gas[x]
            for i in range(x, x+trailLen+1):   
                if i!=x and i%(x+trailLen)==0: 
                    
                    return x

                veh=veh-cost[i]+gas[i+1] if veh-cost[i]>=0 else -1
                # print(x, i, veh, gas[i+1], cost[i])
                if veh<0: break
        return -1
        """
        
        #do ask kadane's algorithm; help from (https://www.youtube.com/watch?v=lJwbPZGo05A)
        
        if sum(gas)<sum(cost): return -1  #no enough gas to complete the loop
        
        total=0
        startIndex=0
        
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            
            if total<0:
                total=0
                startIndex=i+1
        return startIndex