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
        
    #status: correct; didnt understand; help(https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome)
    #Analysis: Time O(n^2), Space O(1)
    #ref: 2/13/2023P2:track1-cpGrind75;Day109/110;doLeetcodeBlind75-3q/day-25/45Q:completeOn2/15/2023-Day17/15,collateQuestionPatternIntoCategoriesAndTemplate-Day8/5:(addWordDescriptionOnceProblemIsSolvedDay6/4),0.absorber-x1pomo(6:00-6:30),1.todaysProjections-x1pomo(6:30-7:00),2.longestPalindromicSubstringTimed25Mins-x1pomo(7:00-7:30),3.implement-x2pomo(7:30-8:00),4.2/13/2023prepareForAbbvieInterviewDay2/3,1.analyzeResume-x2pomo(8:00-9:00),5.developingApproachesToDevOpsScenarios-x1ScenarioAnsAnswer-1/2-x2pomo(9:00-10:00),6.applyInternships-x5SWEFromGitHubPage-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        
       