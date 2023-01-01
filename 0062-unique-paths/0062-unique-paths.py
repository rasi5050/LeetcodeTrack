class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #do recursively
        m,n=m-1,n-1
        memo = {}
        def recurse(x, y, m, n):
            if (x,y,m,n) in memo:
                return memo[(x,y,m,n)]
            if (x,y)==(m,n):
                return 1
            elif x>m or y>n:
                return 0
            memo[(x+1, y, m, n)] = recurse(x+1, y, m, n)
            memo[(x, y+1, m, n)] = recurse(x, y+1, m, n)
            
            return memo[(x+1, y, m, n)] + memo[(x, y+1, m, n)]
        return recurse(0, 0, m, n)