class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #return sorted(s)==sorted(t); working solution, O(logn)
        
        #return Counter(s)==Counter(t); working solution, O(n)
        
        primes={'a': 2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,'g': 17,'h': 19,'i': 23,'j': 29,'k': 31,'l': 37,'m': 41,'n': 43,'o': 47,'p': 53,'q': 59,'r': 61,'s': 67,'t': 71,'u': 73,'v': 79,'w': 83,'x': 89,'y': 97,'z': 101}
        sProd=prod([primes[char] for char in s])
        tProd=prod([primes[char] for char in t])
        return sProd==tProd
    
        #status: correct
        #Analysis: Time O(n), Space O(1)
        #ref: 1/15/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day82/82C3Ai3QuestionsFromMostFrequentListOf0/10Day2/5+Blind75WeekOne0/14q,2q/dayDay2/7-,1.bestTimeToBuyAndSellStocksTimed25Mins-x1pomo(12:30-13:00),2.implement-x1pomo(13:00-13:30),3.validPalindromeTimed25Mins-x1pomo(13:30-14:00),4.implement-x1pomo(14:00-14:30),5.invertBinaryTimed25Mins-x1pomo(14:30-15:00),6.implement-x1pomo(15:00-15:30),7.validAnagramTimed25Mins-x1pomo(15:30-16:00),8.implement-x1pomo(16:00-16:30),9.absorber-x1pomo(16:30-17:00)=x9pomo(12:30-17:00)delayed;5.longestArithmeticSubsequenceTimed25Mins-x1pomo(13:00-13:30),Blind753q/Day,7.2SumTimed25Mins-x1pomo(13:30-14:00),8.validParenthesesTImed25Mins-x1pomo(14:00-14:30),9.mergeTwoSortedListsTimed25Mins-x1pomo(14:30-15:00)//more;1.bestTimeToBuyAndSellStocksTimed25Mins-x1pomo(15:30-16:00),3.validPalindromeTimed25Mins-x1pomo(16:00-16:30),5.invertBinaryTimed25Mins-x1pomo(16:30-17:00)
