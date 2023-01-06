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
        
        
                