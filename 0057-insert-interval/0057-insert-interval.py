class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted=False
        for i in range(len(intervals)):
            if intervals[i]>=newInterval:
                intervals.insert(i, newInterval)
                inserted=True
                break
        if not inserted: intervals.append(newInterval)
        #then do merge intervals
        def isOverlap(a, b):
            return a[0]<=b[1] and a[1]>=b[0]
        def mergeOverlap(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]
        
        res=[]
        for i in range(len(intervals)-1):
            if isOverlap(intervals[i], intervals[i+1]):
                intervals[i+1]=mergeOverlap(intervals[i], intervals[i+1])
            else:
                res.append(intervals[i])
        res.append(intervals[-1])
        return res
            