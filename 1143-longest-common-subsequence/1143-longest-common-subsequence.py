class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #do brute force; create all subsets and manually compare each element
            
        """
        def subsets(word):
            sub= {""}
            for c in word:
                subTemp=set()
                for s in sub:
                    subTemp.add(s+c)
                    subTemp.add(s)
                sub=subTemp
            return sub
        sub1=subsets(text1)
        sub2=subsets(text2)
        if len(sub1)<len(sub2): 
            sub1,sub2=sub2, sub1
            
        res=0
        for sub in sub1:
            if sub in sub2:
                res=max(res,len(sub))
        return res
        #this is O(2^N + 2^N + N) solution
        """
        #solution from neetcode
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
        
        #status: correct; neetcode solution
        #Analysis: Time O(len(text1) * len(text2)), Space O(len(text1) * len(text2))
        #ref: 12/30/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day67/68,1.0/1knapSackTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.longestCommonSubsequenceTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.wordBreakProblemTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.combinationSumTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)

    