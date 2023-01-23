class Solution:
    def maximumSwap(self, num: int) -> int:
        # idea: iterating from left to right, if any number to the right of the current number is maxium than current number, it should be swapped, hence there should be a way to know the maximum to the right side in O(1), it possible by precalculating an array with (max values and till that point, index) starting from right side to left side//similar to trapping rain water question.
        
        # on the first occurance of current<right max, swap both elements and return the number
        #create (right max,index) array similar to trapping rain water
        """working;commented for alter
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
        """
    #status: correct; Rasi's Solution
    #Analysis: Time O(n), Space O(n)
    #ref: 1/23/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day90/90Blind26/75,2q/dayDay9/10;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day2/5-3q/day+searchOAQuestionsInReddit/csMajor,1.designAStackWithIncrementOperationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.reformatDateTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.maximumSwapTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.01MatrixTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.longestSubstringWithoutRepeatingCharactersTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
        
        num=list(str(num))
        #reverse max
        maxToRight=[(0,0)]*len(num)   #(val, index)
        
        for i in range(len(num)-2,-1,-1):
            if int(num[i+1])>int(maxToRight[i+1][0]):
                maxToRight[i]=(num[i+1], i+1)
            else: maxToRight[i] = maxToRight[i+1]
                
        for j in range(len(num)-1):
            if int(num[j])<int(maxToRight[j][0]):
                num[j],num[maxToRight[j][1]]    = maxToRight[j][0], num[j]
                return int(''.join(num))
        return int(''.join(num))
                
        
        