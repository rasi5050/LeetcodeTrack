from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """#code not working
        #courseMapping
        preReqMapping=defaultdict(set)
        for a,b in prerequisites:
            preReqMapping[a].add(b)
        visited=set()  
        courseOrder=set()
        courseCompleteList={i for i in range(numCourses)}
        #dfs, once completed add to courseOrder
        def dfs(preReqSet):
            for each in preReqSet:
                if each in visited:
                    return [False]
                visited.add(each)
                if not dfs(preReqMapping[each]):return False
                visited.remove(each)
                del preReqMapping[each]
            if preReqSet: courseOrder.add(each)
            return True
                    
                
        #for each item dfs, once completed add to courseOrder
        for course in range(numCourses):
            visited.add(course)
            if course in preReqMapping and not dfs(preReqMapping[course]): return False
            visited.remove(course)
            if course in preReqMapping: del preReqMapping[course]
            # courseOrder.append(course)
        courseOrder=list(courseOrder)
        for course in courseCompleteList-set(courseOrder):
            courseOrder.append(course)
        return courseOrder
    """
        
        #solution from neetcode youtube (https://www.youtube.com/watch?v=Akt3glAwyfY&t=975s)
        #adjacency list
        preReqMap={ i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReqMap[crs].append(pre)
            
        output=[]
        visit,cycle=set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for pre in preReqMap[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output