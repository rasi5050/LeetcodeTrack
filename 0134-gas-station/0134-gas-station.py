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
        
        #status: correct
        #Analysis: Time O(n), Space O(1)
        #ref: 1/11/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day78/78-,1.gasStationTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.decodeStringTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.trappingRainWaterTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.binarySubArraysWithSumTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
