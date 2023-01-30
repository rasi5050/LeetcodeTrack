class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #use trapping rain water logic, using two arrays left and right
        
        leftPrefix=[0]*len(nums)
        rightPrefix=[0]*len(nums)
        leftPrefix[0]=1       #set multiplicative identity at end
        rightPrefix[-1]=1
        
        for i in range(1,len(nums)):
            leftPrefix[i]=leftPrefix[i-1]*nums[i-1]
        for j in range(len(nums)-1-1, -1, -1):
            rightPrefix[j]=rightPrefix[j+1]*nums[j+1]
        res=[]
        for i in range(len(nums)):
            res.append(leftPrefix[i]*rightPrefix[i])
        return res
    
        #status: correct
        #Analysis: Time O(n), Space O(n)
        #ref: 1/29/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day97/98Blind35/75;doLeetcodeBlind75-3q/day-5/45Q:completeOn2/15/2023-Day3/15:1.P1:1.numberOfWeakCharactersInTheGameTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.coinChangeTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.productOfArrayExceptSelfTimed25Mins-x1pomo(8:00-8:30),6.minStackTimed25Mins-x1pomo(8:30-9:00),7.validateBinarySearchTreeTimed25Mins-x1pomo(9:00-9:30),8.numberOfIslandsTimed25Mins-x1pomo(9:30-10:00),9.rottingOrangesTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
