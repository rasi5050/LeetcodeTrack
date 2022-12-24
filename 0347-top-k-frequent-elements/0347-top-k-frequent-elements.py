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
            heapq.heappush(res, (frequency[freq], freq))
            if len(res)>k: heapq.heappop(res)
        return [res[i][1] for i in range(k)]