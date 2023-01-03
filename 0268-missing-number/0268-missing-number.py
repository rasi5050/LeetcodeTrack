class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #subtract each number from sum of whole series
        n=len(nums)
        sumSeries = (n*(n+1))//2        
        for i in nums:
            sumSeries-=i
        return sumSeries
    #status: correct
    #Analysis: Time O(n); looping tru each element
    #Space O(1); only sumSeries
    #ref: 1/3/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day71/72,1.OA:hudsonRiverTrading-x2pomo(5:30-6:30),2.copyQuestionsToDrive-x2pomo(6:30-7:30),3.missingNumberTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.reverseBitsTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.singleNumberTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
