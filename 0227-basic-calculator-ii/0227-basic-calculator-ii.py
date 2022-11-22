class Solution:
    def calculate(self, s: str) -> int:
        
        operator='+'
        cur=prev=res=i=0
        curNumS=""
        while i < len(s):
            cur_char=s[i]
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    curNumS+=s[i]
                    i+=1
                i-=1
                curNum=int(curNumS)
                if operator=='+':
                    res+=curNum
                    prev=curNum
                elif operator=='-':
                    res-=curNum
                    prev=-curNum
                elif operator=='*':
                    res-=prev
                    res+=prev*curNum
                    
                    prev=prev*curNum
                elif operator=='/':
                    res-=prev
                    res+=int(prev/curNum)
                    
                    prev = int(prev/curNum)
                curNumS=""
            elif cur_char != ' ':
                operator=s[i]
            i+=1
        return res
        
        #status: correct; complete help from (https://www.youtube.com/watch?v=W3Rg4HVSZ9k&t=939s)
        #analysis: Time O(n)
        #Space: O(1), fixed number of variables
        #ref:11/22/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day45/46:1.(P1:doPaypalLeetcodeQuestion4/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),2.happyNumberTimed25Mins-x1pomo(5:30-6:00),3.implement-x2pomo(6:00-7:00),4.squaresOfASortedArrayTimed25Mins-x1pomo(7:00-7:30),5.implement-x2pomo(7:30-8:30),6.reverse-substrings-between-each-pair-of-parenthesesTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.basicCalculatorAnswers-x1pomo(10:00-10:30),8.basicCalculator2Timed25Mins-x1pomo(10:30-11:00),9.implement-x2pomo(11:00-12:00)=x13pomo(5:30-12:00)
