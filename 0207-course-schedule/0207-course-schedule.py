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
        
        #Status: correct
        #Analysis: Time O(n);visit all nodes of graph atmost once
        #Space O(n)=O(|V|+|E|)for storing graph
        #ref: 1/19/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day86/86C3Ai3QuestionsFromMostFrequentListOf7/10Day5/5+Blind16/75,2q/dayDay5/7;1.courseScheduleTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.groupAnagramsTimed25Mins-x1pomo(7:00-7:30),4.findAllAnagramsInAStringTimed25Mins-x1pomo(7:30-8:00),5.topKFrequentElementsTimed25Mins-x1pomo(8:00-8:30),6.majorityElementTimed25Mins-x1pomo(8:30-9:00),7.addBinaryTimed25Mins-x1pomo(9:00-9:30),8.implement-x1pomo(9:30-10:00),9.diameterOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  

            
        