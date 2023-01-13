class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #two sum
        def twoSum(j, target):
            map={}
            
            temp=[]
            for i in range(j+1,len(nums)):
                if target-nums[i] in map:
                    temp.append((i, map[target-nums[i]]))
                map[nums[i]]=i
            for i in range(j):
                if target-nums[i] in map:
                    temp.append((i, map[target-nums[i]]))
                map[nums[i]]=i
            return temp
        res=set()
        targetVisited=set()
        # res=[]
        for j,target in enumerate(nums):
            if target in targetVisited:
                continue
            out=twoSum(j, -target)
            for item in out:
                i,k=item
                # res.append((nums[j],nums[i],nums[k]))
                res.add(tuple(sorted((nums[j],nums[i],nums[k]))))
            targetVisited.add(target)
        return res
    
        #status: correct
        #Analysis: Time O(n^2), Space O(n)
        #ref: 1/13/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day80/80-,1.topKFrequentElementsTimed25Mins-x1pomo(12:30-13:00),2.implement-x2pomo(13:00-14:00),3.containerWithMostWaterTimed25Mins-x1pomo(14:00-14:30),4.implement-x2pomo(14:30-15:30),5.1/12/2022P1Temp:applyInternshipsTimed8Mins:reach600/600Day5/5-20for3HoursperDay,1.apply1st6FromHandshakePortal-x2pomo(14:00-15:00)delayed(16:00-17:00)-x1pomo(15:30-16:00)=x7pomo(12:30-16:00)

                