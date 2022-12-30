class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        #try the brute force way first
        for part in range(1,len(nums)):
            print(sum(nums[:part]), sum(nums[part:]))
            if sum(nums[:part])==sum(nums[part:]):
                return True
        return False
        """#wrong judgement about the problem, jumped into conclusion without checking conditions
        
        #couldnt arrive at solution; my thought process was to some how break into subproblems of conventional array based dp method where it might be taking left right sum values so that at the end of the array I can compare the left==right.
        """
        why i thought this way?==>correlating past questions to adap to this solution.
        error in judgement is, unable to identify causation, hence simply trying yo match patterns
        
        #thought process from neetcode solution.
        this can be converted into one of the partition containing half the sum of total array, ie. if one partition contains half the total sum, other half is guaranteed to be half of the total sum. Hence we focus only on one partition.
        
        This can be developed into if there is a subset, whether its sum is half the sum or not?
        
        hence problem basically reduces to sum of possible subsets you can create so that the its sum is equal to target.
        
        In DP land this can be reduced into whether to add an element to a array or not?
        
        [1] consider at this point you have only elements, now can make choice to include 1 or not, so the possible subsets you can create is [] [1], hence the sums from it will be {0,1}
        [1,2] now further consider the array under purview has got one more element, now would make a choice about 2, whether to consider it or not?, hence the possible subarrays can be [][1][][1][2][1,2], ie. you can decide to include 2 to the current subset, this can be further made concise by using sets {[][1][2][1,2]} 
        [1,2,3] similarly for 3 also
        """
        if sum(nums)%2: return False
        dp = set()
        dp.add(0) #base case: if any of the elements are not included, sum is 0
        target=sum(nums) // 2
        #for each subarray add the current element
        for num in nums:
            dpNext=set()
            for s in dp:
                dpNext.add(s+num)
                dpNext.add(s)
                if target in dpNext: return True
                
            dp=dpNext
        print(dp)
        return False
        
        
    