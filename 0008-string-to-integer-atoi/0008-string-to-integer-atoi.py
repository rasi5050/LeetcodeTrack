class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign,res=1,0
        i=0
        if i<len(s) and s[i] in {'+','-'}: #first charecter should be + or - if at all it exists
            if s[i]=='-':
                sign=-1
            i+=1
        for j,c, in enumerate(s[i:]):
            if c.isdigit():
                res=res*10 + int(c)
            else:
                break
        res=res*sign
        res=min(res, 2**31-1) if res>=0 else max(res,-2**31)
        return res
    #status: correct; help(https://leetcode.com/problems/string-to-integer-atoi/discuss/3110465/Python3-Fast-Code-and-Simple)
    #Analysis: Time O(n), Space O(1)
    #ref: 2/11/2023P2:track1-cpGrind75;Day107/108;doLeetcodeBlind75-3q/day-21/45Q:completeOn2/15/2023-Day15/15,collateQuestionPatternIntoCategoriesAndTemplate-Day6/5:(addWordDescriptionOnceProblemIsSolvedDay5/4),               1.stringToIntegerTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)shortened(6:00-7:30)

                
            
                