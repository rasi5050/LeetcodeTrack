class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #write for single source
        """correct answer;TLE; unbale to figure out how to add memoization to the current setup
        visited=set()
        currLen=0
        maxLen=0
        memo={}
        def dfs(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            nonlocal currLen
            nonlocal maxLen
            if (x,y) not in visited:
                visited.add((x,y))
                currLen+=1
                # memo[(x,y)]=
                maxLen=max(maxLen, currLen)
                if not(x-1)<0                and matrix[x-1][y]>matrix[x][y]: dfs(x-1,y)
                if not(x+1)>len(matrix)-1    and matrix[x+1][y]>matrix[x][y]: dfs(x+1,y)
                if not(y-1)<0                and matrix[x][y-1]>matrix[x][y]: dfs(x,y-1)
                if not(y+1)>len(matrix[0])-1 and matrix[x][y+1]>matrix[x][y]: dfs(x,y+1)
                currLen-=1
                visited.remove((x,y))
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j)
        return maxLen
        """
        """
        #adding memoization to dfs
        visited=set()
        @cache
        def dfs(x,y):
            if (x,y) not in visited:
                visited.add((x,y))
                up=down=left=right=0
                if not(x-1)<0                and matrix[x-1][y]>matrix[x][y]: up=dfs(x-1,y)
                if not(x+1)>len(matrix)-1    and matrix[x+1][y]>matrix[x][y]: down=dfs(x+1,y)
                if not(y-1)<0                and matrix[x][y-1]>matrix[x][y]: left=dfs(x,y-1)
                if not(y+1)>len(matrix[0])-1 and matrix[x][y+1]>matrix[x][y]: right=dfs(x,y+1)
                visited.remove((x,y))
                return 1+max(up, down, left, right)
        maxLen=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxLen=max(maxLen, dfs(i,j))
        return maxLen
        """
        
    
    
    #reducing lines
        #visited set is not required because it will be prevented by the increasing chain that higher number will not be able to enter the chain from higher value to lower value
        @cache
        def dfs(x,y):
                up=down=left=right=0
                if not(x-1)<0                and matrix[x-1][y]>matrix[x][y]: up=dfs(x-1,y)
                if not(x+1)>len(matrix)-1    and matrix[x+1][y]>matrix[x][y]: down=dfs(x+1,y)
                if not(y-1)<0                and matrix[x][y-1]>matrix[x][y]: left=dfs(x,y-1)
                if not(y+1)>len(matrix[0])-1 and matrix[x][y+1]>matrix[x][y]: right=dfs(x,y+1)
                return 1+max(up, down, left, right)
        maxLen=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxLen=max(maxLen, dfs(i,j))
        return maxLen
    
        
#         #do DP
#         #extra rows and columns on top, bottom, left, right for base cases
#         dp=[[0]*(len(matrix[0])+2) for row in range(len(matrix)+2)]
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 dp[i+1][j+1]=max(1+dp[i-1+1][j+1] if (i-1>=0) and matrix[i-1][j]<matrix[i][j] else 1, 1+dp[i+1][j-1+1] if (j-1>=0) and matrix[i][j-1]<matrix[i][j] else 1)
#         maxLen=0 
#         for i in range(len(matrix)-1, -1, -1):
#             for j in range(len(matrix[0])-1,-1,-1):
#                 dp[i+1][j+1]=max(dp[i+1][j+1] ,max(1+dp[i+1+1][j+1] if ((i+1)<=len(matrix)-1) and matrix[i][j]>matrix[i+1][j] else 1, 1+dp[i+1][j+1+1] if ((j+1)<=len(matrix[0])-1) and matrix[i][j]>matrix[i][j+1] else 1))
#                 maxLen=max(maxLen, dp[i+1][j+1])
#         print(dp)
#         return maxLen
                
                
    