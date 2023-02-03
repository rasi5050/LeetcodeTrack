class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:   
        map={i:[] for i in range(numCourses)}
        for req,prereq in prerequisites:
            map[req].append(prereq)
            
        visited,cycleSet = set(), set()
        def dfs(course):
            if course in cycleSet:  #cycle in current lookup
                return False
            if course in visited:
                return True
            
            cycleSet.add(course)
            for prereq in map[course]:
                if dfs(prereq)==False:
                    return False
            cycleSet.remove(course)    
            visited.add(course)
            res.append(course)
                
                
        res=[]
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return res