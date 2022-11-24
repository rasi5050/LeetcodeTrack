from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        preReqMapping=defaultdict(set)
        for preReq in prerequisites:
            preReqMapping[preReq[0]].add(preReq[1])
            
        def dfs(preReq):
            for eachMap in preReq:
                if eachMap in currentChain:
                    return False
                currentChain.add(eachMap)
                if eachMap in preReqMapping and dfs(preReqMapping[eachMap])==False:
                    return False
                currentChain.remove(eachMap)
                if eachMap in preReqMapping: del preReqMapping[eachMap]
        
        for course in range(numCourses):
            currentChain={course}
            if course in preReqMapping and dfs(preReqMapping[course])==False:
                return False 
        return True