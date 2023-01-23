class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter=Counter('')
        curMax=0
        #two pointers:
        l=r=0
        for _ in range(len(s)):
            counter[s[r]]+=1
            r+=1
            while counter.most_common() and counter.most_common()[0][1]>1:
                counter[s[l]]-=1
                if counter[s[l]]==0: del counter[s[l]]
                l+=1
            if counter.most_common() and counter.most_common()[0][1]==1:
                curMax=max(curMax, r-l)
            # print(counter)
        return curMax
    
    
    #status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/23/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day90/90Blind26/75,2q/dayDay9/10;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day2/5-3q/day+searchOAQuestionsInReddit/csMajor,1.designAStackWithIncrementOperationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.reformatDateTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.maximumSwapTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.01MatrixTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.longestSubstringWithoutRepeatingCharactersTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
