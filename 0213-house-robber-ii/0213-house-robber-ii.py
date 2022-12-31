class Solution:
    def rob(self, nums: List[int]) -> int:
       
        if len(nums)==1: return nums[0]
        house1=house2=0
        for moneyFromCurHouse in nums:
            temp=max(moneyFromCurHouse + house1, house2)
            house1=house2
            house2=temp
        houseR2=houseR1=0
        for moneyFromCurHouse in reversed(nums):    #... n R2 R1
            temp=max(moneyFromCurHouse + houseR1, houseR2)
            houseR1=houseR2
            houseR2=temp
        
        return max(house1, houseR1)
    #status: correct; idea trigger from neetcode solution to modify house robber 1 solution
    #Analysis: O(n)+ O(n) = O(n)
    # Space O(1); constant number of varaibles
    #ref: 12/31/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day68/68,1.wordBreakProblemTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.combinationSumTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.houseRobber2Timed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.decodeWaysTimed25Mins-x1pomo(10:00-10:30),8.implement-x2pomo(10:30-11:30)=x12pomo(5:30-11:30)delayed(6:30-11:30)1.wordBreakProblemTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00),3.combinationSumTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.houseRobber2Timed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.decodeWaysTimed25Mins-x1pomo(11:00-11:30)
