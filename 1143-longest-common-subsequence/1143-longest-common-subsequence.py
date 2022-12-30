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
    