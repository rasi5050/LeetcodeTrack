import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for x,y in points:
            heapq.heappush(res, (x**2 + y**2, [x,y]))
        return [heapq.heappop(res)[1] for _ in range(k)]
            
        