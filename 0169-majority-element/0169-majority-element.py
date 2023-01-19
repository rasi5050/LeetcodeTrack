class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #do Moore's voting algorithm
        #whenever the count of assumed majority goes to zero, majority is reset to next element
        count=0
        for n in nums:
            if count==0:
                currMajority=n
                count+=1
            elif currMajority==n:
                count+=1
            else:
                count-=1
        return currMajority  