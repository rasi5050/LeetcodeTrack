class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #sliding window using pointer
        
        goal=Counter(p)
        window=Counter(s[:len(p)])
        res=[]
        i=-1
        for i,(l,r) in enumerate(zip(s[:len(s)-((len(p)-1))],s[len(p):])):
            if window==goal:
                res.append(i)
            window[l]-=1
            window[r]+=1
        #last window case   
        if window==goal:
            res.append(i+1)
        return res
    
    #status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/19/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day86/86C3Ai3QuestionsFromMostFrequentListOf7/10Day5/5+Blind16/75,2q/dayDay5/7;1.courseScheduleTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.groupAnagramsTimed25Mins-x1pomo(7:00-7:30),4.findAllAnagramsInAStringTimed25Mins-x1pomo(7:30-8:00),5.topKFrequentElementsTimed25Mins-x1pomo(8:00-8:30),6.majorityElementTimed25Mins-x1pomo(8:30-9:00),7.addBinaryTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.diameterOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
