class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #no for each target apply 2Sum 2 solution
        
        nums.sort()
        def twoSum2(index, target):
            l,r=index+1,len(nums)-1
            while l<r:
                threeSum=target+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([nums[index], nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                
            
        res=[]
        for i,val in enumerate(nums):
            index=i
            target=val
            if i>0 and val==nums[i-1]:
                continue
            twoSum2(index, target)
        return res
        
        