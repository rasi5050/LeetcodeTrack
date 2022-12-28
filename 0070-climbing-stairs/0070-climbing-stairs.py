class Solution:
    def climbStairs(self, n: int) -> int:
        """correct answer; commented to try DP approach
        memo={}
        def recurse(i):
            if i in memo: return memo[i]
            if i<0: return 0
            elif i==0: return 1
            memo[i]=recurse(i-1) + recurse(i-2)
            return memo[i]
        return recurse(n)
        """
    #do using dp:
    # say stairs are represented in array with indexes 
    # 0,1,2,3,4,5
    #[ , , , , , ]
        """
    the subproblems are (n-2) depends on (n-1) and n because from (n-2) you can go to (n-2+1) or (n-2+2) taking 1 or 2 steps. 
    ie from 5 you cannot go anywhere, hence for 5 number of ways to go is 1; hence base case.
    from 4 you can go to 5 or 6, but 6 is out of bounds, hence it can go to only 5 and number of ways 4 can go depends of number of ways 5 can go, which is 1, hence 4 is also 1. ==> 4-1, 5-1
    
    further 3, from 3 we can go to 4 and 5, ie. total number of ways to go from 3 is the number of ways to go from 4 and 5, which is 1+1=2 etc.
    # 0,1,2,3,4,5
    #[ , , , ,1,1]  base cases
    
    # 0,1,2,3,4,5
    #[ , , ,2,1,1]  for 3
    
    # 0,1,2,3,4,5
    #[ , ,3,2,1,1]  for 2
    
    # 0,1,2,3,4,5
    #[ ,5,3,2,1,1]  for 1
    
    # 0,1,2,3,4,5
    #[ 8,5,3,2,1,1]  for 0, hence dp[0] is the answer; this is same as arrayizing the bottom up recursion tree
        """
    
        #using DP
        """    working code; commented for optimization
        dp =[0]*(n+1)
        #base cases
        dp[n]=dp[n-1]=1
        for i in range(n-2, -1, -1):
            dp[i]=dp[i+1]+dp[i+2]
        return dp[0]
        """
    #this is further optimized to 
        dp1=dp2=1
        for i in range(n-2, -1, -1):
            dp1T=dp1
            dp1=dp1+dp2
            dp2=dp1T
        return dp1
    #status: correct: dp idea from neetcode youtube solution (https://www.youtube.com/watch?time_continue=619&v=Y0lT9Fck7qI&feature=emb_logo)
    #Analysis: Time O(number of subproblems * work per subproblem)=O(n)*O(number of ways to go from further subprblem)= O(1) ==> O(n)
    # Space: O(1), storing only 2 variables dp1, dp2
    #ref: 12/28/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day65/66,1.2.studyDynamicProgramming2(https://dev.to/nikolaotasevic/dynamic-programming--7-steps-to-solve-any-dp-interview-problem-3870)-x1pomo(5:30-6:00),2.climbingStairsTimed25Mins-x1pomo(6:00-6:30),3.implement-x2pomo(6:30-7:30),4.coinChangerTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.houseRobber-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.longestIncreasingSubsequenceTimed25Mins-x1pomo(10:30-11:00),9.absorber-1pomo(11:00-11:30)=x12pomo(5:30-11:30)
