class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #do brute force
        """
        res=-1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res=max(res, nums[j]-nums[i])
        return res if res else -1
        """
        #this is Time O(n^2); think better
        
        #do kadanes algoriths
        
        #loop and calculate max every iteration; if a new minimum is found, update the minimum
        res=0
        curMin=curMax=nums[0]
        for n in nums[1:]:
            if n<curMin: 
                curMin=n
                curMax=n
            elif n>curMax: 
                curMax=n
                res = max(res, curMax - curMin)
        return res if res else -1
    
        #status: correct
        #Analysis: Time O(n); one pass algorithm, Space O(1)
        #ref: 1/6/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day74/74-ciscoDay2/2,1.maximumDifferenceBetweenIncresingElementsTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.wordSearch2Timed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.burstBaloonsTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.decodeWaysTimde25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(6:00-11:30)

        
        
                