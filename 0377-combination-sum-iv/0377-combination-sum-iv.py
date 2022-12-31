class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #try brute force, create all combinations and check sum(comb)==target
        dp = { 0 : 1 }
        
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]
    
        #status: correct; didnt understand, this is solution from neetcode youtube solution (https://www.youtube.com/watch?v=dw2nMCxG0ik&t=620s)
        #Analysis: Time O(target*len(nums))
        #Space O(target); stores dp array
        #ref: 12/31/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day68/68,1.wordBreakProblemTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.combinationSumTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.houseRobber2Timed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.decodeWaysTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)delayed(6:30-11:30)1.wordBreakProblemTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00),3.combinationSumTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.houseRobber2Timed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.decodeWaysTimed25Mins-x1pomo(11:00-11:30)

        