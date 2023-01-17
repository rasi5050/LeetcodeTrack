class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+2)
        dp[n]=1
        for i in range(n-1, -1, -1):
            dp[i]=dp[i+1]+dp[i+2]   
        return dp[0]
    
    #status: correct; didnt understand;-second try;
    #Analysis: Time O(n), Space O(n)
    #ref: 1/17/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day84/84C3Ai3QuestionsFromMostFrequentListOf7/10Day4/5+Blind15/75,2q/dayDay4/7;1.binarySubArraysWithSumTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.generateParenthesesTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.serializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.climbingStairsTimed25Mina-x1pomo(9:00-9:30),8.longestPalindromeTimed25Mins-x1pomo(9:30-10:00),9.reverseLinkedListTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
