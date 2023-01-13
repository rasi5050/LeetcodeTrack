class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for word in strs:
            map[tuple(sorted(word))].append(word)
        return map.values()
    
    #status: correct
    #Analysis: Time O(n log k), Space O(k*n)
    #ref: 1/13/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day80/80-,0.void-x1pomo(5:30-6:00),1.serialializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.courseScheduleTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.groupAnagramsTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.findAllAnagramsInAStringTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(6:00-11:30)
