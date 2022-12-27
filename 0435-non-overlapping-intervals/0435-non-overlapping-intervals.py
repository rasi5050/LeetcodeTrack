class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #consider shortest finish time intervals(ref: https://youtu.be/2P-yW7LQr08?t=1054)
        count=0
        intervals.sort()
        for i in range(len(intervals)-1):
            #1--4,2--3
            #  3--5
            if intervals[i][1]>intervals[i+1][0]:
                count+=1
                intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])
        return count
        