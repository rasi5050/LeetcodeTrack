class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        matrix=mat
        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    top = matrix[i-1][j] if i else float('inf')
                    left = matrix[i][j-1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if cell := matrix[i][j]:
                        bottom = matrix[i+1][j] if i < m - 1 else float('inf')
                        right = matrix[i][j+1] if j < n -1 else float('inf')
                        matrix[i][j] = min(cell, min(bottom, right) + 1)
        return matrix
    
    #status: correct (help from leetcode solutions comments of (lenchen1112) https://leetcode.com/problems/01-matrix/solution/)
    #Analysis: Time O(nm), Space O(1)
    #ref: 12/22/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day58/58,1.01MatrixTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.rottingOrangesTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.cloneGraphTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.pacificAtlanticWaterFlowTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)
