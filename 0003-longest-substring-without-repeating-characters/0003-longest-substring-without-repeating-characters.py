class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex={}
        l=0
        maxLen=0
        for r,c in enumerate(s):
            if c in lastIndex:
                l=max(lastIndex[c]+1,l)  #the left should be 1more than the last occurance or the current l, whichever is greater
            maxLen=max(maxLen, r-l+1)
            lastIndex[c]=r
        return maxLen
    
    #status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/23/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day90/90Blind26/75,2q/dayDay9/10;1.3SumTImed25Mins-x1pomo(12:00-12:30),2.BinaryTreeLevelOrderTraversalTimed25Mins-x1pomo(12:30-13:00),3.closeGraphTimed25Mins-x1pomo(13:00-13:30),4.implement-x1pomo(13:30-14:00)-x4pomo(12:00-14:00)
