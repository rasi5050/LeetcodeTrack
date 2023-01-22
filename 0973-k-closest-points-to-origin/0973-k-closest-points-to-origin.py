class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x,y in points:
            heap.append((x**2+y**2,[x,y]))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
            