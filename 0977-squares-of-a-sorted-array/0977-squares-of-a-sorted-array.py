class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #intuition: utilizing spliting to -ve, +ve, then merge, then square
        #find pivot
        pivot=0
        for i in range(len(nums)):
            if abs(nums[i])==nums[i]:
                pivot=i
                break
        
        #split by pivot, a has -ve numbers, b has +ve numbers
        a,b=nums[:pivot], nums[pivot:]
        if nums[pivot]!=abs(nums[pivot]):a=b;b=[]      #if all numbers of -ve, dump b to a
        a.reverse()     #all are -ve, reverse and square would make in non decreasing order
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
        