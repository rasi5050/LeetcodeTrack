class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        def isOverlap(a,b):
            x1,y1=a
            x2,y2=b
            return (x1<=y2 and x2<=y1) or (x2<=y1 and x1<=y2)
            
        def merge(a,b):
            x1,y1=a
            x2,y2=b
            return [min(x1,x2), max(y1,y2)]
        res=[intervals[0]]
        for interval in intervals[1:]:
            if isOverlap(res[-1],interval):
                res[-1]=merge(res[-1],interval)
            else:
                res.append(interval)
        return res
        #status: correct
        #Analysis: Time O(nlog n), Space O(n)
        #ref: 2/4/2023P2:track1-cpGrind75;Day101/102;doLeetcodeBlind75-3q/day-14/45Q:completeOn2/15/2023-Day7/15:prepareTiktokDevOpsIntenseFocusDay2/7;1.BasicCalculator3TImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.longestIncreasingPathInAMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x1pomo(8:00-8:30),5.mergeIntervalsTimed25Mins-x1pomo(8:30-9:00),6.decodeStringTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

    