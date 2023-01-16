# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        """working code; commented for alter
        #intuition: something to do with binary search
        left=1
        right=n
        while left<=right:
            mid=(left+right)//2
            fnCall=isBadVersion(mid)
            fnCallPrev=isBadVersion(mid-1)
            if fnCallPrev==False and fnCall==True:
                return mid
            elif fnCall==False:
                left=mid+1
            else:
                right=mid-1
        """
        #status: correct
        #Analysis: Time O(log n), Space O(1)
        #ref: 1/16/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day83/84C3Ai3QuestionsFromMostFrequentListOf3/10Day3/5+Blind75WeekOne7/14q,2q/dayDay3/7-,1.balancedBinaryTreeTImed25Mins-x1pomo(12:30-13:00),2.linkedListCycleTimed25Mins-x1pomo(13:00-13:30),3.implement-x1pomo(13:30-14:00),4.implementQueueUsingStacksTimed25Mins-x1pomo(14:00-14:30),5.firstBadVersionTimed25Mins-x1pomo(14:30-15:00),6.implement-x1pomo(15:00-15:30),7.ransomNoteTImed25Mins-x1pomo(15:30-16:00),8.implement-x1pomo(16:00-16:30)=x8pomo(12:30-16:30)                   

        left=1
        right=n
        while left<=right:
            mid=(left+right)//2
            fnCall=isBadVersion(mid)
            if fnCall==False:
                left=mid+1
            else:
                right=mid-1
        return left