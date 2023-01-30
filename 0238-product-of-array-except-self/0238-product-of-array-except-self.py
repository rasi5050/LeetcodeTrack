class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #use trapping rain water logic, using two arrays left and right
        
        leftPrefix=[0]*len(nums)
        rightPrefix=[0]*len(nums)
        leftPrefix[0]=1       #set multiplicative identity at end
        rightPrefix[-1]=1
        
        for i in range(1,len(nums)):
            leftPrefix[i]=leftPrefix[i-1]*nums[i-1]
        for j in range(len(nums)-1-1, -1, -1):
            rightPrefix[j]=rightPrefix[j+1]*nums[j+1]
        res=[]
        for i in range(len(nums)):
            res.append(leftPrefix[i]*rightPrefix[i])
        return res