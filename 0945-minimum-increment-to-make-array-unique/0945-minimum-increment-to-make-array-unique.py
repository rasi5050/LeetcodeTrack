class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(1,len(nums)):
            prev,curr=nums[i-1],nums[i]
            if prev>=curr: 
                count+=((prev-curr)+1)
                nums[i]+=((prev-curr)+1)
        return count