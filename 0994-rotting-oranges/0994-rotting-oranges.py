class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #do multi source BFS from all rotten oranges
        frontier=[]
        numberOfFreshApples=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    frontier.append((i,j))
                elif grid[i][j]==1:
                    numberOfFreshApples+=1
        if numberOfFreshApples==0: return 0
        numberOfFreshApples+=len(frontier)
        numberOfDays=0
        # print(numberOfFreshApples)
        firstFlag=True
        while frontier:
            next=[]
            for each in frontier:
                i,j=each
                if (not(i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1) and grid[i][j]==1) or firstFlag:
                    grid[i][j]=2
                    # print(i,j, 'numberOfDays: ',numberOfDays )
                    numberOfFreshApples-=1
                    next.append((i-1, j))
                    next.append((i+1, j))
                    next.append((i, j-1))
                    next.append((i, j+1))
            frontier=next
            numberOfDays+=1
            firstFlag=False
        # print(numberOfDays, numberOfFreshApples)
        return numberOfDays-2 if numberOfFreshApples==0 else -1