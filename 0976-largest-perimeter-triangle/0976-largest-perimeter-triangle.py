class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #valid triangle is a+b>c for all sides, sum of two sides should be strictly greater than third side for any combination of a, b, c
        """
        #brute force O(n^3)
        maxPeri=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    a,b,c=nums[i], nums[j], nums[k]
                    if a+b>c and b+c>a and c+a>b:
                        maxPeri=max(maxPeri, a+b+c)
        return maxPeri
        """
                        
        #idea:sort(idea from leetcode solution)
                
        nums.sort()
        for i in range(len(nums)-1-2,-1,-1):
            a,b,c=nums[i], nums[i+1], nums[i+2]
            if a+b>c:
                return a+b+c
        return 0