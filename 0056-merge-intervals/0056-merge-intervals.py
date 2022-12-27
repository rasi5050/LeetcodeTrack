class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlap(a, b):
            return a[0]<=b[1] and a[1]>=b[0]
        def mergeOverlap(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]
        intervals.sort()
        res=[]
        #compare intervals[i] and intervals[i+1] at a time, if no overlap add to res.append(intervals[i]), if over lap update overlap to intervals[i+1], consider edge case to include last element in array
        for i in range(len(intervals)-1):
            if isOverlap(intervals[i], intervals[i+1]):
                intervals[i+1]=mergeOverlap(intervals[i], intervals[i+1])
            else:
                res.append(intervals[i])
        res.append(intervals[-1])
        return res
        #status: correct; partial help from overlap and merging methods of https://www.techinterviewhandbook.org/algorithms/interval/
        #Analysis: Time O(n); length of intervals
        #Space O(n); all the intervals might be unique
        #ref: 12/27/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day64/64,1.wordSearch2Timed25Mins-x1pomo(5:30-6:00),2.implement-x1pomo(6:00-7:00),3.studyIntervals-x1pomo(7:00-7:30),4.mergeIntervalsTimed;25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.insertIntervalTImed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.nonOverlappingIntervalsTimed25Mins-x1pomo(10:30-11:00),9.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

                
            