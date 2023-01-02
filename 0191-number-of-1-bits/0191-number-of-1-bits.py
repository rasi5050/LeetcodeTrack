class Solution:
    def hammingWeight(self, n: int) -> int:
        """working code: commented for reduction
        count=0
        while n:
            if n & 1: count+=1
            n>>=1  #divide by 2 a.k.a remove last bit
        return count    
        """
    #status: correct
    #Analysis: Time O(32) = O(1), Space O(1)
    #ref: 1/2/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day70/70,0.applyForOncampusJobEventsAndTechServices,1.sumOfTwoIntegersTimed25mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.numberOf1BitsTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.countingBitsTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.missingNumberTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
        
        count=0
        while n:
            count+=n&1
            n>>=1
        return count