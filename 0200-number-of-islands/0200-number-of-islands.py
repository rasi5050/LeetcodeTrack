class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #do BFS
        #fill frontier using foor loop to all elements, if element is 1
        noOfIslands=0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n]=='1':
                    # print(grid)
                    noOfIslands+=1
                    frontier=[(m,n)]
                    while frontier:
                        next=[]
                        for index in frontier:
                            i, j = index
                            # print(index)
                            if grid[i][j] == '1':
                                grid[i][j] = '-1'
                                if 0<i and grid[i-1][j]=='1'            : next.append((i-1,j))
                                if i<len(grid)-1 and grid[i+1][j]=='1'     : next.append((i+1,j))
                                if 0<j and grid[i][j-1]=='1'           : next.append((i,j-1))
                                if j<len(grid[0])-1 and grid[i][j+1]=='1'  : next.append((i,j+1))    
                        frontier=next[:]
        print(grid)
        return noOfIslands