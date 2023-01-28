class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for aster in asteroids:
            while stack and stack[-1]>0 and aster<0:   #both are in opposite direction
                if stack[-1]<abs(aster):
                    stack.pop()
                elif stack[-1]>abs(aster):  #discard current aster
                    break
                elif stack[-1]==abs(aster):    
                    stack.pop()
                    break
            else:
                stack.append(aster)
        return stack
    
    #status: correct; help (https://leetcode.com/problems/asteroid-collision/discuss/109666/Python-O(n)-Stack-based-with-explanation)
    #Analysis: Time O(n), Space O(n)
    #ref: 1/28/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day95/96Blind31/75,2q/dayDay14/14;doLeetcodeBlind75-3/45Question/Day:completeOn2/15/2023-Day1/15:1.P1:1.wallsAndGatesTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.asteroidCollisionTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.cloneGraph-x1pomo(8:00-8:30),6.Evaluate Reverse Polish NotationTimed25Mins-x1pomo(8:30-9:00),7.implement-x1pomo(9:00-9:30),8.courseSchedule-x1pomo(9:30-10:00),10.implementTrieTimed25Mins-x1pomo(10:00-10:30),11.coinChangeTimed25Mins-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)delayed-1.P1:1.wallsAndGatesTimed25Mins-x1pomo(7:30-8:00),2.implement-x1pomo(8:00-8:30),3.asteroidCollisionTimed25Mins-x1pomo(8:30-9:00),4.implement-x1pomo(9:00-9:30),5.cloneGraph-x1pomo(9:30-10:00),6.Evaluate Reverse Polish NotationTimed25Mins-x1pomo(10:00-10:30),7.implement-x1pomo(10:30-11:00)

    