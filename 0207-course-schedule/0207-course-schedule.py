class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map=defaultdict(list)
        for req, pre in prerequisites:
            map[req].append(pre)
            
        visited=set()   
        def recurse(req):
            if req in visited:
                return False
            visited.add(req)           
            for each in map[req]:
                if recurse(each)==False:
                    return False
            del map[req]
            visited.remove(req)
        for i in range(numCourses):    
            if recurse(i)==False:
                return False
        return True
        
        
        