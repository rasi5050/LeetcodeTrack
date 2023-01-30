class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[math.inf]*(amount+1)
        dp[0]=0
        
        for i in range(1,len(dp)):
            for coin in coins:
                if i-coin>=0:
                    dp[i]=min(dp[i],1+dp[i-coin])
        # print(dp)
        return dp[-1] if dp[-1]!=math.inf else -1
    
    #status: correct; did not understand; help(https://www.youtube.com/watch?v=H9bfqozjoqs&t=953s)
    #Analysis: Time O(n^2), space (n)
    #ref: 1/29/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day97/98Blind35/75;doLeetcodeBlind75-3q/day-5/45Q:completeOn2/15/2023-Day3/15:1.P1:1.numberOfWeakCharactersInTheGameTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.coinChangeTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.productOfArrayExceptSelfTimed25Mins-x1pomo(8:00-8:30),6.minStackTimed25Mins-x1pomo(8:30-9:00),7.validateBinarySearchTreeTimed25Mins-x1pomo(9:00-9:30),8.numberOfIslandsTimed25Mins-x1pomo(9:30-10:00),9.rottingOrangesTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
