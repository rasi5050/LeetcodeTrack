class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        def dfs(i,j):
            if (i,j) in visited or (i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1) or grid[i][j]=='0':
                return
            visited.add((i,j))
            grid[i][j]='0'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
        numberOfIslands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    numberOfIslands+=1
                    dfs(i,j)
        return numberOfIslands