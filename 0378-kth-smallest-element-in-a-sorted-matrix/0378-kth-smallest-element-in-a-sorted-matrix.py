class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #intuition: double loop for all elements, then then add to some data structures upto k elements are filled and return struct[k-1]
        """
        available data structures:
            array
            hashMap
            heap
            trees
            
            normal iterate tru elements then insert in sorted order,
            until we insert all elements how to identify it
            [[1,5,9],
             [2,6,10],
             [3,7,11]]"""
        """working code1
        #naive approach
        
        listTemp=[]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                listTemp.append(matrix[row][col])
        listTemp.sort()
        return listTemp[k-1]
        """
        #status:wrong
        #Intuition2: use maxHeap, discard elements when len > k; from leetcode discussions: (https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise)
        
        maxheap=[]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                #using negative numbers to emulate min heap using max heap
                heappush(maxheap, -matrix[row][col])
                if len(maxheap) > k:
                    heappop(maxheap)
        return -maxheap[0]
    
    #time complexity: O(row * col * log K)
    # NB: heap takes O(log K) for operation, since its handling only handling among k elements
    
    # space complexity: O(k) : since we are discarding elements when size grows than k
    
    #ref: 11/3/2022P2:rack1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day31/32:do,1.kthSmallestElementInSortedArrayTimed25Mins-x1pomo(9:00-9:30),2.implement-x2pomo(9:30-10:30),3.search2dMatrixTimed25Mins-x1pomo(10:30-11:00),4.implement-x2pomo(11:00-12:00)-x6pomo(9:00-12:00)
