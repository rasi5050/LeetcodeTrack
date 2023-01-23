class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        #idea: from(https://www.youtube.com/watch?v=Ezj3VDOfd5I); do from all zeroes to as single dummy node to ones; earlier did individual dfs from each zeroes to one, instead make all zeroes at source at once
        frontier=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    frontier.append((i,j))
        res=[[0]*len(mat[0]) for _ in range(len(mat))]
        level=0
        visited=set()
        while frontier:
            next=[]
            for x,y in frontier:
                if not(x<0 or y<0 or x>len(mat)-1 or y>len(mat[0])-1 or (x,y) in visited):
                    if mat[x][y]==1:
                        res[x][y]=level
                        # continue  #earlier thought, it should end when it sees a 1, but found that it should not because there could be 1 which can be only reached through only ones
                    visited.add((x,y))
                    next.append((x-1,y))
                    next.append((x+1,y))
                    next.append((x,y-1))
                    next.append((x,y+1))
            frontier=next
            level+=1
        return res
    
    #status: correct; Rasi's code; partial help(https://www.youtube.com/watch?v=Ezj3VDOfd5I)
    #Analysis: Time O(m*n), Space O(m*n)
    #ref: 1/23/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day90/90Blind26/75,2q/dayDay9/10;P1:doTiktok:SWE OA(DevOps)- 2023 Summer (BS/MS)Day2/5-3q/day+searchOAQuestionsInReddit/csMajor,1.designAStackWithIncrementOperationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.reformatDateTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.maximumSwapTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.01MatrixTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.longestSubstringWithoutRepeatingCharactersTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
