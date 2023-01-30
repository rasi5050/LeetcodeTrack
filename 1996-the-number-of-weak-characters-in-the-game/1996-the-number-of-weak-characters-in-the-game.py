class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0],-x[1]))
        #now if we traverse from properties[::-1], attack values are already sorted, do dont have to care, only have to care if reverse sorted defence values are breaking the constraint
        # ie. if a defense value is lower than the previous maximum
        
        currMax=0
        weakCounter=0
        for _,defense in properties[::-1]:
            if defense<currMax:
                weakCounter+=1
            currMax=max(currMax,defense)
        return weakCounter
        
    #status: correct
    #Analysis: Time O(n), Space O(1)
    #ref: 1/29/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day97/98Blind35/75;doLeetcodeBlind75-3q/day-5/45Q:completeOn2/15/2023-Day3/15:1.P1:1.numberOfWeakCharactersInTheGameTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.coinChangeTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.productOfArrayExceptSelfTimed25Mins-x1pomo(8:00-8:30),6.minStackTimed25Mins-x1pomo(8:30-9:00),7.validateBinarySearchTreeTimed25Mins-x1pomo(9:00-9:30),8.numberOfIslandsTimed25Mins-x1pomo(9:30-10:00),9.rottingOrangesTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

    
    
