class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """working code; TLE
        sumList=sum(nums)
        if sumList<goal: return 0
        if sumList==goal: return 1
        count=0
        for i in range(len(nums)):
            curSum=nums[i]
            if curSum==goal:
                count+=1
            for j in range(i+1, len(nums)):
                curSum+=nums[j]
                if curSum==goal:
                    count+=1
                elif curSum>goal: break
        return count
        """        
        #something to do with prefix sums
        
        
        P=[0]
        for x in nums: P.append(P[-1]+x)
        print(P)
        
        count=Counter()
        ans=0
        for x in P:   #for each value in prefix sum
            ans+=count[x]
            count[x+goal] += 1
        return ans