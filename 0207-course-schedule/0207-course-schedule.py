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
            del courseMapping[course]
        return True     
    
    #status: correct, 2nd Day try
    #analysis: Time: O(|V|+|E|), each vertex and edge is visited once
    #Space: O(|V|+|E|), each vertex and edge is stored
    #ref:11/25/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day48/48:1.(P1:doPaypalLeetcodeQuestion6/5;1.4.courseScheduleTimed25Min-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.courseSchedule2TImed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.AllAncestorsOfNodeInADirectedAcyclicGraphTImed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.absorber-x1pomo(10:30-11:00)=x10pomo(6:00-11:00)
