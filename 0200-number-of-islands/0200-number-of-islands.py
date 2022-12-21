class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #do BFS
        #fill frontier using foor loop to all elements, if element is 1
        noOfIslands=0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n]=='1':
                    noOfIslands+=1
                    frontier=[(m,n)]
                    while frontier:
                        next=[]
                        for index in frontier:
                            i, j = index
                            if grid[i][j] == '1':
                                grid[i][j] = '-1'
                                if 0<i and grid[i-1][j]=='1'                : next.append((i-1,j))
                                if i<len(grid)-1 and grid[i+1][j]=='1'      : next.append((i+1,j))
                                if 0<j and grid[i][j-1]=='1'                : next.append((i,j-1))
                                if j<len(grid[0])-1 and grid[i][j+1]=='1'   : next.append((i,j+1))    
                        frontier=next
        return noOfIslands
    
    #status: correct
    #analysis: Time O(m*n); all the elements of matrix are visited once
    # Space O(n); frontier[] and next[] used for temperory storage
    #ref: 12/21/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day57/58,1.kThSmallestElementInABstTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.study:graph-x1pomo(7:00-7:30),4.numberOfIslandsTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.floodFillTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.01MatrixTimed25Mins-x1pomo(10:30-11:00),9.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
