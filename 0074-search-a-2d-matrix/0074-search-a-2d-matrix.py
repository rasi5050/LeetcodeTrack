class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #intuition: find row, binary search
        
        #steps:
        #1.for row in matrix:
        #2. if row[0]<=target<=row[-1]
        #3. break
        #4. at end return False
        #5.binary search target, if True
        #6. return False
        
        #implement
        """correct code: commented for optimization
        for row in matrix:
            if row[0]<=target<=row[-1]:
                left=0
                right=len(row)-1
                while left<=right:
                    mid = (left+right)//2
                    if target==row[mid]:
                        return True
                    elif target<row[mid]:
                        right=mid-1
                    else:
                        left=mid+1
                return False
        return False
        """
    #status: correct
    
    #m=num rows, n=num cols
    #time complexity: O(logm + logn)
    #space complexity: O(1)
    #ref: 11/3/2022P2:rack1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day31/32:do,1.kthSmallestElementInSortedArrayTimed25Mins-x1pomo(9:00-9:30),2.implement-x2pomo(9:30-10:30),3.search2dMatrixTimed25Mins-x1pomo(10:30-11:00),4.implement-x2pomo(11:00-12:00)-x6pomo(9:00-12:00)
    
    #optimization: use binary search instead of loop rows
    
    #steps:
    #1.top=0, down=len(matrix)-1
    #2.if matrix[mid][0]<=target<=matrix[mid][0]
    #3.then apply 2nd binary search
    
        top=0
        down=len(matrix)-1
        while(top<=down):
            midR=(top+down)//2
            if matrix[midR][0]<=target<=matrix[midR][-1]:
                left=0            
                right=len(matrix[0])-1    
                while left<=right:
                    midC = (left+right)//2
                    if target==matrix[midR][midC]:
                        return True
                    elif target<matrix[midR][midC]:
                        right=midC-1
                    else:
                        left=midC+1
                return False
            elif target<matrix[midR][0]:
                down=midR-1
            else:
                top=midR+1
        return False

        #status: success
        #time complexity O(logm + logn)
        #nested binary search, BS on row, then BS on satisying col
        #space O(1)

               
            
            