class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for char in s:                      #O(n)
            if char==')':
                revWord=""
                while stack[-1]!='(': revWord+=stack.pop()          #O(n)
                stack.pop()
                for char in revWord: stack.append(char)       #O(n)           
            else:stack.append(char)
        return "".join(stack)
    
    #analysis: Time O(n^2)
    #Space O(n)
    #ref: 11/22/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day45/46:1.(P1:doPaypalLeetcodeQuestion4/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),2.happyNumberTimed25Mins-x1pomo(5:30-6:00),3.implement-x2pomo(6:00-7:00),4.squaresOfASortedArrayTimed25Mins-x1pomo(7:00-7:30),5.implement-x2pomo(7:30-8:30),6.reverse-substrings-between-each-pair-of-parenthesesTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.basicCalculatorAnswers-x1pomo(10:00-10:30),8.basicCalculator2Timed25Mins-x1pomo(10:30-11:00),9.implement-x2pomo(11:00-12:00)=x13pomo(5:30-12:00)
