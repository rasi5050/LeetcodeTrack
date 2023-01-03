class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #subtract each number from sum of whole series
        n=len(nums)
        sumSeries = (n*(n+1))//2
        
        for i in nums:
            sumSeries-=i
        return sumSeries