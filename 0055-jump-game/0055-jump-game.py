class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #do recursive solution:
        """TLE
        memo={}
        def recurse(i):
            if i in memo:
                return memo[i]
            
            if i==len(nums)-1:
                return True
            elif i>=len(nums) or nums[i]==0:
                return False
            res=False
            memo[i]=False
            for jumpsInI in range(1,nums[i]+1):
                memo[i]=memo[i] or recurse(i+jumpsInI) 
            return memo[i]
        return recurse(0)
        """
        
        #do greedy as per neetcode youtube solution (https://www.youtube.com/watch?v=Yan0cv2cLy8&t=893s)
        goalIndex = len(nums)-1
        #shift the goalIndex backwards one by one if the previous index can reach it. ie if b can reach c and a can reach b==> a can reach c
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalIndex:
                goalIndex=i
        return not goalIndex #the value can be 0 index or any further index from which it was not be to reduce further, hence if 0 return True else return False
    
        #status: correct; greedy idea from neetcode youtube solution
        #Analysis: Time O(n) visitng all elements once
        #Space O(1); nothing extra stored
        #ref: 1/1/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day69/70,1.uniquePathsTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.jumpGameTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.studyBinary-x1pomo(8:30-9:00),6.sumOfTwoIntegersTimed25mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30),8.numberOf1BitsTimed25Mins-x1pomo(10:30-11:00),9.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(8:00-11:30)1.uniquePathsTimed25Mins-x1pomo(8:00-8:30),2.implement-x2pomo(8:30-9:30),3.jumpGameTimed25Mins-x1pomo(9:30-10:00),4.implement-x2pomo(10:00-11:00),5.studyBinary-x1pomo(11:00-11:30)
