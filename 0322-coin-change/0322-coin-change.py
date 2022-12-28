class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         dp=[0]*(amount+1)
#         dp[amount]=1
#         for i in range(amount-1, -1, -1):            
#             dp[i] = max(dp[i+1]) 
        """
        dp=[0]
        i=0
        coins=set(coins)
        while dp[-1]<=amount:
            print(dp)
            print(coins)
            if dp[-1]==amount: return len(dp)-1
            if not coins: return -1
            if amount-dp[-1]>=max(coins):
                dp.append(dp[-1]+max(coins))
            else:
                coins.remove(max(coins))
        #this is wrong because its considering only one path
        """
        #try recursive
        """wrong concept
        memo={}
        def recurse(i):
            if i in memo: return memo[i]
            if i==0: return 1
            if i<0: return 0
            memo[i]=min(recurse(i-1), recurse(i-2), recurse(i-5))
            return memo[i]
        return recurse(amount)
        #wrong concept
        """
        #complete idea from neet code youtube solution: (https://www.youtube.com/watch?v=H9bfqozjoqs&t=1130s)
        #intuition; this can be constructed as what is the number of coins required to obtain a particular sum.
        """
        eg, say you want to know how many coins are required to reach a sum of 1, this can be divided into subproblem of how many coins needed to reach sum 0.
        similarly how many coins needed to reach 3, might be decided by how many coins needed for 2 , similarly for 1.
        
        This can be developed as a reccurence: T(n) = min(1+ dp[n-coin] for coin in coins)
            ie. if amount ==7, and coins are [1,2,3,5]
            dp[7] = min(1 + dp[7-1], 1 + dp[7-2], 1 + dp[7-3], 1 + dp[7-5])
            further simplified dp[7] = min(1 + dp[6], 1 + dp[5], 1 + dp[4], 1 + dp[2])
            1 + dp[6] is explained as if 1amount is taken(ie. 1coin) remaining amount is 6,
            hence given amount1 is taken how many more coins are need for it to become 7, that is given by
            take 1 coin(here amount1) then find number of coins required for 6, hence 1 + dp[6]
            
            """
        dp=[math.inf]*(amount+1)
        dp[0]=0 #to get amount 0 , zero coins are required
        for m in range(1, amount+1):
            for c in coins:
                if m-c>=0:
                    dp[m]=min(dp[m], 1 + dp[m-c])
        print(dp)
        return dp[amount] if dp[amount]!=math.inf else -1
                        
        #status: correct; complete help from neetcode youtube solution(https://www.youtube.com/watch?v=H9bfqozjoqs&t=1130s); understanding dynamic programming
        #Analysis: Time O(amount * len(coins))
        #Space O(amount)
        #ref: 12/28/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day65/66,1.2.studyDynamicProgramming2(https://dev.to/nikolaotasevic/dynamic-programming--7-steps-to-solve-any-dp-interview-problem-3870)-x1pomo(5:30-6:00),2.climbingStairsTimed25Mins-x1pomo(6:00-6:30),3.implement-x2pomo(6:30-7:30),4.coinChangerTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.houseRobber-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.longestIncreasingSubsequenceTimed25Mins-x1pomo(10:30-11:00),9.absorber-1pomo(11:00-11:30)=x12pomo(5:30-11:30)

                        
                        