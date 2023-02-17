class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #normal approach
        """
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
        """
        #alternate from bottom to top
        @cache
        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            count=0
            count+=dfs(i-1,j)
            count+=dfs(i,j-1)
            return count
        return dfs(m-1,n-1)
        
        
        