class Solution:
    def isHappy(self, n: int) -> bool:
        """correct code:commmented for optimization
        visited=set()
        sumN=0
        while(True):                          #dont know  
            visited.add(n)                    #O(1)
            while(n):                         #O(n)
                sumN+=(n%10)**2               #O(1)
                n//=10
            if sumN==1:
                return True
            elif sumN in visited:
                return False
            n, sumN=sumN, 0
        """ 
        #status: correct
        #analysis: dont know
        #ref:11/22/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day45/46:1.(P1:doPaypalLeetcodeQuestion4/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),2.happyNumberTimed25Mins-x1pomo(5:30-6:00),3.implement-x2pomo(6:00-7:00),4.squaresOfASortedArrayTimed25Mins-x1pomo(7:00-7:30),5.implement-x2pomo(7:30-8:30),6.reverse-substrings-between-each-pair-of-parenthesesTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.basicCalculatorAnswers-x1pomo(10:00-10:30),8.basicCalculator2Timed25Mins-x1pomo(10:30-11:00),9.implement-x2pomo(11:00-12:00)=x13pomo(5:30-12:00)
        
        visited, sumN=set(), 0
        while(n not in visited):                          #dont know  
            visited.add(n)                    #O(1)
            while(n):                         #O(n)
                sumN+=(n%10)**2; n//=10               #O(1)
            if sumN==1:return True
            n, sumN=sumN, 0
        return False
            
            