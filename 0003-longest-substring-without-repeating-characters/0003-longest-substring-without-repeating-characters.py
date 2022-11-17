class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #intuition: use two pointer
        
        counter=0
        subString=deque()
        subStringSet=set()
        i=j=0
        
        while j<len(s):
            if s[j] in subStringSet:
                while subString[0]!=s[j]:
                    subStringSet.remove(subString[0])
                    subString.popleft()
                    i+=1
                subString.popleft()
                i+=1
            subString.append(s[j])
            subStringSet.add(s[j])
            j+=1
            counter=max(counter, j-i)   
        return counter
    
    #status: correct
    #analysis: Space O(2n)=O(n)
    #Time O(n), earlier it was O(n^2), since The search was within the deque which will take O(n), now its replaced with set(), hence check will take only O(1)
    #ref:11/17/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day40/40:(P1:doPaypalLeetcodeQuestion1/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.twoSumTimed25Mins-x1pomo(5:30-6:00),2.longestSubstringWithoutRepeatingCharactersTimed25Mins-x1pomo(6:00-6:30),3.implement-x2pomo(6:30-7:30),4.medianOfTwoSortedArraysTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.zigzagConversionTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30)=x10pomo(5:30-10:30)
