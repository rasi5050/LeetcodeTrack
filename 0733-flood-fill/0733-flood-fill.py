class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """working code;commented to try with bfs
        if image[sr][sc]==color : return image      
        def dfs(i, j):
            nonlocal image
            nonlocal color
            nonlocal fromColor
            if i<0 or j<0 or i>len(image)-1 or j>len(image[0])-1 or image[i][j]!=fromColor:
                return 
            image[i][j]=color
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        fromColor = image[sr][sc]    
        dfs(sr, sc)    
        return image
        """
    #status: correct; adapted base cases from (https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution)
    #analysis: Time O(n); might have to color all elements if all connected to it
    #Space O(1); not storing anything extra
    #ref: 12/21/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day57/58,1.kThSmallestElementInABstTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.study:graph-x1pomo(7:00-7:30),4.numberOfIslandsTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.floodFillTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.01MatrixTimed25Mins-x1pomo(10:30-11:00),9.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
        #bfs
        fromColor=image[sr][sc]
        if fromColor==color: return image
        frontier=[(sr,sc)]
        while frontier:
            next=[]
            for index in frontier:
                i,j=index
                if not (i<0 or j<0 or i>len(image)-1 or j>len(image[0])-1 or image[i][j]!=fromColor):
                    image[i][j]=color
                    next.append((i-1, j))
                    next.append((i+1, j))
                    next.append((i, j-1))
                    next.append((i, j+1))
            frontier=next[:]
        return image
    
    
    