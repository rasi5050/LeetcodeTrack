class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

#         arr = []
#         heappush(arr, -3)
#         heappush(arr, -2)
#         heappush(arr, -1)
#         heappush(arr, -5)
#         heappush(arr, -6)
#         heappush(arr, -4)
        
#         print(-heappop(arr))
#         print(-heappop(arr))
        #optimization
        """working code
        temp = []
        kSmall=len(nums)-k+1
        for num in nums:
            heappush(temp, -num)
            if len(temp)>kSmall:
                heappop(temp)
        return -heappop(temp)
        """
    #time complexity: O(nlogk)
    #space complexity: O(k)
    #status: correct
    #ref: 11/3/2022P2:rack1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day31/32:do,1.kthSmallestElementInSortedArrayTimed25Mins-x1pomo(9:00-9:30),2.implement-x2pomo(9:30-10:30),3.search2dMatrixTimed25Mins-x1pomo(10:30-11:00),4.implement-x2pomo(11:00-12:00)-x6pomo(9:00-12:00)

        nums=[-x for x in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heappop(nums)
        return -heappop(nums)
    
    #status: correct
    #time complexity: O(n + logn + (k-1)*O(1)) = O(log n)
    #space complexity: O(1)
      
            