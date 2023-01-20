class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=maxSum=nums[0]
        for n in nums[1:]:
            if curSum<=0:
                curSum=n    
            else:
                curSum+=n
            maxSum=max(maxSum, curSum)
        return maxSum