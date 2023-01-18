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
        #addOn: we dont have to loop back to the starting point, because if sum(gas)>sum(cost), it will be guaranteed that we can cover the distance
        return index
    
    #status: correct
    #Analysis: Time O(n), Space O(1)
    #ref: 1/18/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day85/86C3Ai3QuestionsFromMostFrequentListOf7/10Day4/5+Blind15/75,2q/dayDay4/7;1.GasStationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Decode StringTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.trappingRainWaterTimed25Min-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.reverseLinkedListTimed25Mins-x1pomo(9:00-9:30),8.majorityElementTimed25Mins-x1pomo(9:30-10:00),9.addBinaryTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
