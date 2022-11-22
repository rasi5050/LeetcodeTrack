class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #find pivot
        pivot=0
        for i in range(len(nums)):
            if abs(nums[i])==nums[i]:
                pivot=i
                break
        
        #split by pivot
        a,b=nums[:pivot], nums[pivot:]
        if nums[pivot]!=abs(nums[pivot]):a=b;b=[]
        a.reverse()
        
        print(a,b)
        # if abs(b[0])!=b[0]: b.reverse()
            
        a=[i*(-1) for i in a]
        
        #merge + square O(n)
        res=[]
        i=j=0
        while i<len(a) and j<len(b):
            if a[i]<=b[j]:
                res.append(a[i]**2)
                i+=1
            else:
                res.append(b[j]**2)
                j+=1
        while i<len(a):
            res.append(a[i]**2)
            i+=1
        while j<len(b):
            res.append(b[j]**2)
            j+=1
        return res
        