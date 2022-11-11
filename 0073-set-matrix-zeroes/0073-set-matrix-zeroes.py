class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #intuition: hashMap the positions, then change to zeroes
        
        #steps:
        #1.hashMap=defaultdict(list)
        #2.for i in range(len(matrix))
        #3.for j in range(len(matrix[0]))
        #4.if matrix[i][j]==0
        #5.hashMap[i].append(j)
        #6.for i in hashMap:
        #7.for j in hashMap[i]:
        #8.matrix[i]=[0 for _ in range(len(matrix[0]))]
        #9.for x in range(len(matrix)):
        #10.matrix[x][j]=0
        #return
        """
        from collections import defaultdict
        hashMap=defaultdict(list)
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    hashMap[i].append(j)
        for i in hashMap:
            matrix[i]=[0 for _ in range(cols)]
            for j in hashMap[i]:
                for x in range(rows):
                    matrix[x][j]=0
        """
        #status: success
        #ref: 11/5/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day33/34:do,1.setMatrixZeroes-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.spiralMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rotateImageTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.absorber-x1pomo(10:30-11:00)=x10pomo(6:00-11:00)
        #time complexity: O(mn)
        #space complexity: O(mn)
        
        #optimization O(1) space: intuition from leetcode: use first row and first col to represent status of entire row or column discussion(https://leetcode.com/problems/set-matrix-zeroes/discuss/657430/Python-Solution-w-approach-explanation-and-readable-with-space-progression-from%3A-O(m%2Bn)-and-O(1))
        
        #steps:
        #1.represent states in first row and col
        #2.then update zeros based on states
        rows=len(matrix)
        cols=len(matrix[0])
        firstRow='n'
        firstCol='n'
        for i in range(cols):
            if matrix[0][i]==0:
                firstRow='x'
        for i in range(rows):
            if matrix[i][0]==0:
                firstCol='x'
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    matrix[i][0]='x'
                    matrix[0][j]='x'  
        for i in range(1,rows):
            if matrix[i][0]=='x':
                matrix[i] = [0 for _ in range(cols)]
        for j in range(1,cols):
            if matrix[0][j]=='x':
                for x in range(1,rows):
                    matrix[x][j]=0
        if firstRow=='x':
            matrix[0] = [0 for _ in range(cols)]
        if firstCol=='x':
            for j in range(rows):
                matrix[j][0]=0
        for i in range(cols):
            if matrix[0][i]=='x':
                matrix[0][i]=0
        for i in range(rows):
            if matrix[i][0]=='x':
                matrix[i][0]=0
        
        #status: intuition from leetcode discussion, implentation @Rasi
        #status: correct
        #time complexity: O(mn)
        #space complexity: O(1) ==> used first row and first col as state store
        
        # observations:
        #1.missed mutliple edge cases
        #2.reinitialized thoughts to not to update first row and last row to zeroes until last 
        #3.introduced two variables for firstRow and firstCol if the entire first row or col is zeroed
        #ref: 11/5/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day33/34:do,1.setMatrixZeroes-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.spiralMatrixTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rotateImageTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.absorber-x1pomo(10:30-11:00)=x10pomo(6:00-11:00)
        
            
        
            

        