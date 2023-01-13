class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        water=0
        while i<j:
            water=max(water, min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return water
        #status: correct
        #Analysis: Time O(n), Space O(1)
        #ref: 1/13/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day80/80-,1.topKFrequentElementsTimed25Mins-x1pomo(12:30-13:00),2.implement-x2pomo(13:00-14:00),3.containerWithMostWaterTimed25Mins-x1pomo(14:00-14:30),4.implement-x2pomo(14:30-15:30),5.1/12/2022P1Temp:applyInternshipsTimed8Mins:reach600/600Day5/5-20for3HoursperDay,1.apply1st6FromHandshakePortal-x2pomo(14:00-15:00)delayed(16:00-17:00)-x1pomo(15:30-16:00)=x7pomo(12:30-16:00)

            