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
                
                
            