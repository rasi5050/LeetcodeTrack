class Solution:
    def maximumSwap(self, num: int) -> int:
        #create (right max,index) array similar to trapping rain water
        num=str(num)
        rightMax=[(0,0)]*len(num)   #this means, after last index, maximum to the right side of current element is zero
        for i in range(len(num)-2,-1,-1):
            if int(num[i+1])>rightMax[i+1][0]:
                rightMax[i]=(int(num[i+1]),i+1)
            else: rightMax[i]=rightMax[i+1]
        
        for j in range(len(num)-1):
            if num[j]=='9' or int(num[j])>=rightMax[j][0]:
                continue
            else:
                return int(num[:j] + str(rightMax[j][0]) + num[j+1:rightMax[j][1]] + num[j] + num[rightMax[j][1]+1:])
        return int(num)
    
    #status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/23/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day90/90Blind26/75,2q/dayDay9/10;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day2/5-3q/day+searchOAQuestionsInReddit/csMajor,1.designAStackWithIncrementOperationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.reformatDateTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.maximumSwapTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.01MatrixTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.longestSubstringWithoutRepeatingCharactersTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
