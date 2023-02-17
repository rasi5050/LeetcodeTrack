class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #normal approach
        
        @cache
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            count=0
            count+=dfs(i+1,j)
            count+=dfs(i,j+1)
            return count
        return dfs(0,0)
        
        
        