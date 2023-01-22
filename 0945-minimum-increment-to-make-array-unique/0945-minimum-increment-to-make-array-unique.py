class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        visited=set()
        count=0
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                count+=((nums[i-1]-nums[i])+1)
                nums[i]+=((nums[i-1]-nums[i])+1)
            # visited.add(nums[i])
        return count