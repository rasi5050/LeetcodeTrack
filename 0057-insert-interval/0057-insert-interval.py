class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #insert interval and merge
        if not intervals: return [newInterval]
        inserted=False
        for i in range(len(intervals)):
            if newInterval[0]<=intervals[i][0]:
                intervals.insert(i, newInterval)
                inserted=True
                break
        if not inserted: intervals.append(newInterval)
        def checkOverlap(a,b):
            return b[0]<=a[1] and b[1]>=a[0] or a[1]>=b[0] and a[0]<=b[1]

        def mergeOverlap(a,b):
            return [min(a[0],b[0]),max(a[1],b[1])]
        
        res=[intervals[0]]
        for inter in intervals[1:]:
            a,b=res[-1], inter
            if checkOverlap(a, b):
                res[-1]=mergeOverlap(a,b)
            else:
                res.append(inter)
        return res