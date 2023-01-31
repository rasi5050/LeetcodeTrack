class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: return 0 if nums[0]==target else -1
        #find pivot
        pivot=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                pivot=i+1
                break
        
        def binarySearch(l,r):
            while l<=r:
                # counter-=1
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        # print(0, pivot-1, pivot, len(nums)-1)
        b1=binarySearch(0,pivot-1)
        b2=binarySearch(pivot, len(nums)-1)
        # print(b)
        if b1!=None: return b1
        if b2!=None: return b2
        return -1
                    
                