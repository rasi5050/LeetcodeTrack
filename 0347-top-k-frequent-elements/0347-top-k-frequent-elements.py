import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count frequency
        frequency=defaultdict(int)
        for occur in nums:                  #O(n)
            frequency[occur]+=1
        res=[]
        for freq in frequency:              #O(n)
            heapq.heappush(res, (frequency[freq], freq))  #O(log (k+1))
            if len(res)>k: heapq.heappop(res)
        return [res[i][1] for i in range(k)]
    #status: correct
    #Analysis: TimeO(n log (k+1)); heap size limited to (k+1), heappop and heappush is O(log(k+1)), hence here it is repeated n times ==> O(n Log (k+1))
    #Space O(k+1); size of heap
    #ref: 12/24/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day60/60,1.studyHeap-x1pomo(5:30-6:00),2.mergeKSortedListsTimed25Mins-x1pomo(6:00-6:30),3.implement-x1pomo(6:30-7:30),4.kSmallestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.topKFrequentElementsTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.findMedianFromDataStreamTimed25Mins-x1pomo(10:30-11:00),9.implement-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

    