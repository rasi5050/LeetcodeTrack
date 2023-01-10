class Solution:
    def countArrangement(self, n: int) -> int:
        
        count=[0]
        visited=set()
        def recurse(arr):
            if len(arr)==n+1:
                count[0]+=1
                return
            
            for i in range(1, n+1):
                if i not in visited and (len(arr)%i==0 or i%len(arr)==0):           
                    visited.add(i)
                    arr.append(i)
                    recurse(arr)
                    arr.pop()
                    visited.remove(i)
        recurse(['dummy'])
        return count[0]
    #status: correct
    #Analysis: Time O(n^2), Space O(1)
    #ref: 1/10/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day76/76-,1.implement-x2pomo(12:30-13:30),2.Daily TemperaturesTimed25Mins-x1pomo(13:30-14:00),3.absorber-x1pomo(14:00-14:30)=x4pomo(12:30-14:30)
