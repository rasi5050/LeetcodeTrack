class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adjacency list
        adj = { i:[] for i in range(numCourses)}
        for req in prerequisites:
            a,b=req
            adj[a].append(b)
        # print(adj)    
        
        visited=set()
        def dfs(course):
            if course in visited: return False
            if adj[course] == []: return True
            visited.add(course)
            for pre in adj[course]:
                if not dfs(pre): return False
            visited.remove(course)    
            adj[course]=[]
            return True
                
                
        for req in prerequisites:
            if dfs(req[0])==False: return False
        return True