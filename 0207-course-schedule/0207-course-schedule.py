from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #intuition: do dfs on all sources, in a dive from source to end, check for cycle in the current iteration (idea completion form neetcode youtube solution(https://www.youtube.com/watch?time_continue=868&v=EgI5nU9etnU&feature=emb_logo&themeRefresh=1))
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
    
    #status: correct
    #analysis: Time: O(|V|+|E|), if we consider this a graph it iterates tru all the vertices and edges exaclty once.
    #Space: O(|V|+|E|) , to store adjacency list
    #ref:11/24/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day47/48:1.(P1:doPaypalLeetcodeQuestion6/5;1.timeNeededToRearangeABinaryStringTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.palantirDependencyGraphExplanation-x1pomo(7:00-7:30),4.courseScheduleTimed25Min-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.AllAncestorsOfNodeInADirectedAcyclicGraphTImed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.absorber-x1pomo(10:30-11:00)=x11pomo(5:30-11:00)
