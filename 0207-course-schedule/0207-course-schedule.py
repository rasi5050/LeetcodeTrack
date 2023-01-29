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
                
        #status: correct
        #Analysis: Time O(n), Space O(n)
        #ref: 1/29/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day96/96Blind32/75;doLeetcodeBlind75-3q/day-2/45Q:completeOn2/15/2023-Day2/15:1.P1:1.TheMazeTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Evaluate Reverse Polish NotationTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.courseSchedule-x1pomo(8:00-8:30),6.implementTrieTimed25Mins-x1pomo(8:30-9:00),7.implement-x1pomo(9:00-9:30),8.coinChangeTimed25Mins-x1pomo(9:30-10:00),9.implement-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)

        