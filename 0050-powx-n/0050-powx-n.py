class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recurse(x, n):
            if x == 0: return 0
            if n == 0: return 1            
            
            res = recurse(x, n//2)
            res = res * res
            return x * res if n%2 else res
        res = recurse(x, abs(n))
        return res if n>=0 else 1/res
    
        #status: correct; idea from neetcode youtube solution (https://www.youtube.com/watch?v=g9YQyYi4IQQ)
        #Analaysis: Time O(log n); because divide and conquer
        #Space O(1)
        #ref: 1/4/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day72/72,1.reverseBitsTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.singleNumberTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.pow(x,n)Timed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.sqrt(n)Timed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(6:00-11:30)

            
            
        