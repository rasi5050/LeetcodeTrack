class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #use array of size 3:
        bucket=[0]*3
        for n in nums:
            bucket[n]+=1
        
        for i,v in enumerate([0]*bucket[0]+[1]*bucket[1]+[2]*bucket[2]):
            nums[i]=v
            
                