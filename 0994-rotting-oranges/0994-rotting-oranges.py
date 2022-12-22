class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #intuition: similar to 01-matrix question using dp, what is the distance to the closest rotten orange, do dp from top left and right bottom, if after still there is a fresh orange return -1
        
        import copy
        grid2=copy.deepcopy(grid)
        #alternate idea: do BFS for each rotten orange
        maxDays=0
        visited=set()
        res=[[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                grid=copy.deepcopy(grid2)
                print(grid)
                if grid[m][n]==2:             #rotten; do BFS
                    frontier=[(m,n)]
                    level=0
                    while frontier:
                        next=[]
                        for index in frontier:
                            i, j = index
                            res[i][j]=min(res[i][j], level)
                            grid[i][j]='#'
                            if i>0 and grid[i-1][j]==1: next.append((i-1, j)) 
                            if i<len(grid)-1 and grid[i+1][j]==1: next.append((i+1, j)) 
                            if j>0 and grid[i][j-1]==1: next.append((i, j-1)) 
                            if j<len(grid[0])-1 and grid[i][j+1]==1: next.append((i, j+1))   
                        frontier=next
                        level+=1
        for i, row in enumerate(res):
            for j, cell in enumerate(row):
                if cell==float('inf') and grid2[i][j]==1: return -1
                if cell!=float('inf'): maxDays=max(maxDays, cell)
        
        return maxDays
    
        
        