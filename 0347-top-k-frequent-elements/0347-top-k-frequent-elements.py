class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use heaps:
        
        c=Counter(nums)
        heap=[(-freq, val) for val,freq in c.items()]    #-freq is used to make it max heap
        heapq.heapify(heap)
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            
            