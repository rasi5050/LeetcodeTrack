class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x,y in points:
            heap.append((x**2+y**2,[x,y]))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
            
        #status: correct
        #Analysis : Time O(n); heapify is O(n), Space O(n)
        #ref: 1/22/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day89/90Blind26/75,2q/dayDay8/10;1.kClosestPointToOriginTimed25Mins-x1pomo(12:00-12:30),2.longestSubstringWithoutRepeatingCharacterTimed25Mins-x1pomo(12:30-13:00),3.implement-x1pomo(13:00-13:30),4.3SumTimed25Mins-x1pomo(13:30-14:00),9.binaryTreeLevelOrderTraversalTImed25Mins-x1pomo(14:00-14:30), 10.cloneGraphTimed25Mins(14:30-15:00)=x6pomo(12:00-15:00)alter,1.01MatrixTimed25Mins-x1pomo(12:00-12:30),2.implement-x1pomo(12:30-13:00),3.kClosestPointToOriginTimed25Mins-x1pomo(13:00-13:30),4.longestSubstringWithoutRepeatingCharacterTimed25Mins-x1pomo(13:30-14:00),5.implement-x1pomo(14:00-14:30),5.3SumTimed25Mins-x1pomo(14:30-15:00)=alter=>1.minimumIncrementToMakeArrayUniqueTimed25Mins-x1pomo(12:00-12:30),2.implement-x2pomo(12:30-13:00),3.1.kClosestPointToOriginTimed25Mins-x1pomo(13:00-13:30),2.longestSubstringWithoutRepeatingCharacterTimed25Mins-x1pomo(13:30-14:00),3.implement-x1pomo(14:00-14:30),4.3SumTimed25Mins-x1pomo(14:30-15:00)

        