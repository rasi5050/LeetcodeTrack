class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjacency matrix
        map=defaultdict(list)
        for course,prereq in prerequisites:
            map[course].append(prereq)
        visited=set()
        def recurse(prereq):
            #base conditions
            if prereq in visited:
                return False
            
            visited.add(prereq)
            for each in map[prereq]:
                if recurse(each)==False:
                    return False
            visited.remove(prereq)
            del map[prereq]
            
            
        for course in map.copy():
            if recurse(course)==False:
                return False
        return True    
        
            
        