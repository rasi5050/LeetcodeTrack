class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or s[i]=="2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)
    
    #status: correct; didnot understand; solution from neetcode(https://www.youtube.com/watch?v=6aEyTjOwlJU&t=924s)
    #Analysis Time O(n)
    # Space O(n)
    #ref: 12/31/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day68/68,1.wordBreakProblemTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.combinationSumTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.houseRobber2Timed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.decodeWaysTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)delayed(6:30-11:30)1.wordBreakProblemTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00),3.combinationSumTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.houseRobber2Timed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.decodeWaysTimed25Mins-x1pomo(11:00-11:30)
