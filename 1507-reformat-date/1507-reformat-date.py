class Solution:
    def reformatDate(self, date: str) -> str:
        monthToNum = {'Jan' : '01','Feb' : '02','Mar' : '03','Apr' : '04','May' :  '05','Jun' : '06','Jul' : '07','Aug' : '08','Sep' : '09','Oct' : '10','Nov' : '11','Dec' : '12'}
        date=date.split()
        DD=date[0][:-2] if len(date[0])==4 else '0'+date[0][:-2]
        MM=monthToNum[date[1]]
        YYYY=date[2]
        return YYYY+'-'+MM+'-'+DD
    #status: correct
    #Analaysis : Time O(1), Space O(1)
    #ref: 1/23/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day90/90Blind26/75,2q/dayDay9/10;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day2/5-3q/day+searchOAQuestionsInReddit/csMajor,1.designAStackWithIncrementOperationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.reformatDateTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.maximumSwapTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.01MatrixTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.longestSubstringWithoutRepeatingCharactersTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
