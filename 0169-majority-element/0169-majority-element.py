class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        freq=0
        lastVisited=nums[0]
        for n in nums:
            if n==lastVisited:
                freq+=1
                if freq>len(nums)//2:
                    return n
            else:
                lastVisited=n
                freq=1
                
        #status: correct, idea(https://leetcode.com/problems/majority-element/solution/):approach3
        #Analysis: Time O(nlogn); for sorting, Space O(1)
        #ref: 1/18/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day85/86C3Ai3QuestionsFromMostFrequentListOf7/10Day4/5+Blind15/75,2q/dayDay4/7;1.GasStationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Decode StringTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.trappingRainWaterTimed25Min-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.reverseLinkedListTimed25Mins-x1pomo(9:00-9:30),8.majorityElementTimed25Mins-x1pomo(9:30-10:00),9.addBinaryTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
