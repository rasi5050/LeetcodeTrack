class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """working code; commented for alternate method        
        items=defaultdict(list)
        for x,y in points:
            items[(x**2)+(y**2)].append([x,y])
        # print(items)
        res=[]
        for key in sorted(items.keys()):
            if len(items[key])>1:
                for more in items[key]:
                    res.append(more)
                    k-=1
                    if k==0: return res
            else:
                res.append(*items[key])
                k-=1
                if k==0: return res
        """
        #status: correct
        #Analysis: Time O(n logn); sorting involved
        #Space O(n)
        #ref: 1/5/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day73/74,0.mastercardPsymetrics-x1pomo(5:30-6:00),1.rectangleOverlapTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.kClosestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rectangleAreaTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.twoSumTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

        #alter; use minheap
        
        minHeap=[]
        for index,(x,y) in enumerate(points):
            minHeap.append((x**2+y**2, index))
        heapq.heapify(minHeap)
        res=[]
        for _ in range(k):
            res.append(points[heapq.heappop(minHeap)[1]])
        return res
            
            