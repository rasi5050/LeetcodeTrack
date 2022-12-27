class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #consider shortest finish time intervals(ref: https://youtu.be/2P-yW7LQr08?t=1054)
        count=0
        intervals.sort()
        for i in range(len(intervals)-1):
            #1--4,2--3
            #  3--5
            #start time of an interval is less than previous ones finish time(implies overlap), discard the second. update the the second with the earlier finish time==> taking on the effective results to the the next element
            if intervals[i][1]>intervals[i+1][0]:
                count+=1
                intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])
        return count
    #status: correct;help from https://leetcode.com/problems/non-overlapping-intervals/discuss/2730719/Python-Greedy-Solution
    #Analysis: Time O(nlogn)
    # Space O(1)
    #ref: 12/27/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day64/64,1.wordSearch2Timed25Mins-x1pomo(5:30-6:00),2.implement-x1pomo(6:00-7:00),3.studyIntervals-x1pomo(7:00-7:30),4.mergeIntervalsTimed;25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.insertIntervalTImed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.nonOverlappingIntervalsTimed25Mins-x1pomo(10:30-11:00),9.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
