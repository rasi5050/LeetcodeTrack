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
    