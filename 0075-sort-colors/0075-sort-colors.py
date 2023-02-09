class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """working code in 2 pass; commented for alter
        #use array of size 3:
        bucket=[0]*3
        for n in nums:
            bucket[n]+=1
        
        for i,v in enumerate([0]*bucket[0]+[1]*bucket[1]+[2]*bucket[2]):
            nums[i]=v
        """
        l,i,r=0,0,len(nums)-1
        for _ in range(len(nums)):
            if nums[i]==0:
                nums[l],nums[i]=nums[i],nums[l]
                i+=1
                l+=1
            elif nums[i]==2:
                nums[r],nums[i]=nums[i],nums[r]
                r-=1
            elif nums[i]==1:
                i+=1
                