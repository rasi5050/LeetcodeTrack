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
    #status: correct
    #Analysis: Time O(n); each course is visited once
    #Space O(n)
    #ref: 1/13/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day80/80-,0.void-x1pomo(5:30-6:00),1.serialializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.courseScheduleTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.groupAnagramsTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.findAllAnagramsInAStringTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(6:00-11:30)

        
        
        