class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #do recursively
        """correct code; commented for alternate method
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
        """
        #do reverse
        memo={}
        def recurse(x, y):
            if (x,y) in memo:
                return memo[(x,y)]
            if (x,y)==(0,0):
                return 1
            elif x<0 or y<0:
                return 0
            memo[(x-1, y)] = recurse(x-1, y) 
            memo[(x, y-1)] = recurse(x, y-1)
            return memo[(x-1, y)] + memo[(x, y-1)]
        return recurse(m-1, n-1)