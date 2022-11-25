from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #create mapping
        courseMapping = defaultdict(set)
        for a,b in prerequisites:
            courseMapping[a].add(b)
        visited=set()
        #dfs code
        #it will get a set, process the set
        
        def dfs(mapSet):
            for each in mapSet:
                if each in visited:
                    return False
                visited.add(each)
                if not dfs(courseMapping[each]):
                    return False
                visited.remove(each)
                del courseMapping[each]
            return True
        
        #for each node apply dfs
        for course in courseMapping.copy().keys():
            visited.add(course)
            if not dfs(courseMapping[course]):return False
            visited.remove(course)
        return True            