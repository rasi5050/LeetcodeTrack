class Solution:
    def rob(self, nums: List[int]) -> int:
        """this was wrong approach, it fails to cover all cases, fails at [yes, No, No, Yes] case
        #get odd, even index sums, select max among them
        oddSum=evenSum=0
        for i, val in enumerate(nums):
            if i%2:
                oddSum+=val
            else:
                evenSum+=val
        return oddSum if oddSum>evenSum else evenSum
        """
        
        #use DP
        """
        [1,2,3]
        this can be converted into subprblems of 
        [1] assume at this point only problem exists is [1], whether to rob only a house can be decided as it doesnt have any dependency on other houses, that is our base case
        [1,2] assume at this point the problem is only two houses ie.[1,2]; wether to rob house 2 depends on whether you rob house1
        [1,2,3] assume at this point the problem is only 3 houses ie. [1,2,3]; wether to rob house 3 depends on whether your have robbed the previous houses, ie. at this point you are making decision about house 3 only, all previous decision has been made.
        so whether to rob house 3 is dependent on the maximum amount you can rob if u rob house 3 also, satisfying the criteria, it will be maximum amount till house1 + amount from house3, or if u dont opt to rob house 3 your robbed money will continue as same as what you got upto house 3
        so what essentially I am making a decision is in which combination ie. considering current house or not give me highest money
        """
        """took idea from neetcode solution and changed to version
        dp=[0]*(len(nums)+2)
        for i,w in zip(range(2,len(nums)+2+1),nums):
            dp[i]=max(w + dp[i-2], dp[i-1])
        return dp[-1]
        """
        #concise version from neetcode solution
        house1=house2=0
        for moneyFromCurHouse in nums:
            temp=max(moneyFromCurHouse + house1, house2)
            house1=house2
            house2=temp
        return house2
    #status: correct; didnot understand; solution from neetcode youtube solution (https://www.youtube.com/watch?time_continue=634&v=73r3KWiEvyk&feature=emb_logo&themeRefresh=1)
    #Analysis: O(n); making decision tru each houses, Space O(1)
    #ref: 12/29/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day66/66,1.houseRobber-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.longestIncreasingSubsequenceTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.0/1knapSackTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.longestCommonSubsequenceTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
