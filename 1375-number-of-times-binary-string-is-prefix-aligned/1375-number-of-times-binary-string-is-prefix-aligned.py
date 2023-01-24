class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        #do n^2 algorithm
        """working code; commented to do better
        b=[0]*len(flips)
        preCount=0
        max1Index=0
        curLeftSum=0
        for i in flips:
            b[i-1]=1
            max1Index=max(max1Index, i)
            curLeftSum+=1
            if curLeftSum==max1Index:
                preCount+=1
        return preCount
        """
        
        preCount=0
        max1Index=0
        curLeftSum=0
        for i in flips:
            max1Index=max(max1Index, i)
            curLeftSum+=1
            if curLeftSum==max1Index:
                preCount+=1
        return preCount
        
        #status: correct
        #Analaysis: Time O(n), Space O(1)
        #ref: 1/24/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day91/92Blind29/75,2q/dayDay10/10;1.problems/number-of-times-binary-string-is-prefix-alignedTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day2/5-3q/day+searchOAQuestionsInReddit/csMajor,3.dominoAndTromilloTrailingTImed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.robotRoomCleaner-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.numberOfGoodLeafNodesPairsTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.3SumTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
