class Solution:
    def countBits(self, n: int) -> List[int]:
        """working code; commented for alternate solution
        def countOnes(a):
            count=0
            while a:
                count+=a&1
                a>>=1
            return count
        res=[]
        for i in range(n+1):
            res.append(countOnes(i))
        return res
    #status: correct
    #Analysis: O(n)*O(10^5)=O(n), Space O(n)
    #ref: 1/2/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day70/70,0.applyForOncampusJobEventsAndTechServices,1.sumOfTwoIntegersTimed25mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.numberOf1BitsTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.countingBitsTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.missingNumberTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
        """
        
        def solve(n):
            #base condition
            if n==0: return 0
            elif n==1: return 1
            
            if n%2: return 1 + solve(n//2)
            else: return solve(n//2)
        res=[]
        for i in range(n+1):
            res.append(solve(i))
        return res
            
    