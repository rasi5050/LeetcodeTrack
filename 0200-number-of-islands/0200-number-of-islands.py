class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #intuition: apply dfs on all nodes
        m,n=len(grid), len(grid[0])
        visited=set()
        def neighbors(s):
            x,y=s[0],s[1]
            res=[(x+1,y) if x+1<m else None,(x-1,y) if x-1>=0 else None,(x,y+1) if y+1<n else None,(x,y-1) if y-1>=0 else None]
            return [ i for i in res if i]
        
        def dfs(s):
            if s not in visited and grid[s[0]][s[1]]=="1":
                visited.add(s)
                for adj in neighbors(s):
                    dfs(adj)
        
        count=0
        for i in range(m):
            for j in range(n):
                
                l1=len(visited)
                dfs((i,j))
                l2=len(visited)
                if l2>l1:
                    print(i,j)
                    count+=1
        return count
    #status: correct
    #analysis: Time O(m*n), its visiting all elements to make decision
    # Space O(m*n): it stores visited set()
    #ref:11/21/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day44/44:1.doOnSunday:mathWorks-lastDate21 Nov 2022 10:39 AM EST (America - New York)-105MinutesAsperHackerRank(90Mins,expected60MinsAsPerMathworks):doOn11/21/2022-x3pomo(5:30-7:00),2.addQuestionsToDrive-x2pomo(7:00-8:00),3.(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,4.lruCacheTimed25Min-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.numberOfIslandsTimed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00)=x11pomo(5:30-11:00)

    