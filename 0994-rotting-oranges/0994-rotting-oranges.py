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
    
    #status: correct
    #Analysis: Time O(n), Space O(1); not inccuring additional storage
    #ref: 1/31/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day98/98Blind39/75;doLeetcodeBlind75-3q/day-9/45Q:completeOn2/15/2023-Day4/15:1.numberOfIslandsTimed25Mins-x1pomo(6:00-6:30),2.rottingOrangesTimed25Mins-x1pomo(6:30-7:00),3.searchInARotatedSortedArrayTimed25Mins-x1pomo(7:00-7:30),4.combinationSumTimed25Min-x1pomo(7:30-8:00),5.implement-x1pomo(8:00-8:30),6.couresWork:DAA:flippedClassroom:P1:DAA:fliipedClassroom:watchReccurenceRelation(https://drive.google.com/drive/u/1/folders/0AJMcog-ghtHLUk9PVA)-x4pomo(8:30-10:30),7.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
