class Solution:
    def longestPalindrome(self, s: str) -> str:
        #expand around the center (2n-1) centres
        def expandFromCenter(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1;r+=1
            return r-l-1
        if s=='': return ''
        maxLen=0
        start,end=0,0
        for i in range(len(s)):
            len1=expandFromCenter(i,i)     #including the current character
            len2=expandFromCenter(i,i+1)   #excluding the current character 
            l=max(len1,len2)
            if l>end-start:
                start=i-(l-1)//2
                end=i+l//2
        return s[start:end+1]
        
        
       