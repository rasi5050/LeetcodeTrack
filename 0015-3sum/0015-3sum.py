class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #no for each target apply 2Sum 2 solution
        
        nums.sort()
        def twoSum2(index, target):
            l,r=index+1,len(nums)-1
            while l<r:
                threeSum=target+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([nums[index], nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:  #skip duplicates
                        l+=1
                
            
        res=[]
        for i,val in enumerate(nums):
            index=i
            target=val
            if i>0 and val==nums[i-1]:
                continue
            twoSum2(index, target)
        return res
        
        #status: correct
        #Analysis: Time O(n^2), Space O(n)
        #ref: 1/26/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day93/94Blind29/75,2q/dayDay12/12;1.P1:doOA:1.robotRoomCleaner-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.numberOfGoodLeafNodesPairsTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.3SumTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.binaryTreeLevelOrderTraversalTimed25Mins-x1pomo(9:00-9:30),8.cloneGraph-x1pomo(9:30-10:00),9.Evaluate Reverse Polish NotationTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
