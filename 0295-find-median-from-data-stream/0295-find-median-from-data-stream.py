import heapq
class MedianFinder:
    """working code: commented to avoid inbuilt sort 
    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        return None

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)%2:
            #odd
            return self.arr[len(self.arr)//2]
        else:
            return (self.arr[(len(self.arr)//2)-1] + self.arr[len(self.arr)//2])/2
    """

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
    #status: success; ineficient as its using sort() for each findMedian
    #Analysis: Time O(n*nlogn)   Space O(n)
    #ref: 12/24/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day60/60,1.studyHeap-x1pomo(5:30-6:00),2.mergeKSortedListsTimed25Mins-x1pomo(6:00-6:30),3.implement-x1pomo(6:30-7:30),4.kSmallestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.topKFrequentElementsTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.findMedianFromDataStreamTimed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
    #idea: use maxHeap for left half of list and minHeap to store right half of list
    def __init__(self):
        self.maxHeap=[]
        self.minHeap=[]

    def addNum(self, num: int) -> None:
        maxHeap, minHeap = self.maxHeap, self.minHeap
        if not maxHeap or num<=-maxHeap[0]: heapq.heappush(maxHeap, -num)
        else:
            heapq.heappush(minHeap, num)
            
        #balancing heaps
        if len(minHeap) > len(maxHeap):
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        elif len(maxHeap) > len(minHeap) + 1:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        return None

    def findMedian(self) -> float:
        maxHeap, minHeap = self.maxHeap, self.minHeap
        if len(maxHeap) > len(minHeap): return -maxHeap[0]
        else: return (-maxHeap[0] + minHeap[0])/2
    
    #status: success; idea from (https://leetcode.com/problems/find-median-from-data-stream/discuss/2805054/python3-Max-and-Min-heaps-oror-SortedList-oror-O(log-n))
    #Analaysis: Time O(log n); limited by O(heappush or heappop)
    #Space O(n); total elements stored in heap
    #ref: 12/24/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day60/60,1.studyHeap-x1pomo(5:30-6:00),2.mergeKSortedListsTimed25Mins-x1pomo(6:00-6:30),3.implement-x1pomo(6:30-7:30),4.kSmallestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.topKFrequentElementsTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.findMedianFromDataStreamTimed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

