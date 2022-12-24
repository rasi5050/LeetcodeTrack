import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for x,y in points:
            heapq.heappush(res, (x**2 + y**2, [x,y]))
        return [heapq.heappop(res)[1] for _ in range(k)]
    #status: correct
    #Analaysis: Time O(logn*n) + O(logn * n) = O(n Logn)
    #Space: O(n); storing heap
    #ref: 12/24/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day60/60,1.studyHeap-x1pomo(5:30-6:00),2.mergeKSortedListsTimed25Mins-x1pomo(6:00-6:30),3.implement-x1pomo(6:30-7:30),4.kSmallestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.topKFrequentElementsTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.findMedianFromDataStreamTimed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

            
        