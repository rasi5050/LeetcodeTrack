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