class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map=defaultdict(list)
        for req,prereq in prerequisites:
            map[req].append(prereq)
        
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for each in map[course]:
                if dfs(each)==False:
                    return False
            del map[course]
            visited.remove(course)
        for course in map.copy():
            if dfs(course)==False:
                return False
        return True
                
        