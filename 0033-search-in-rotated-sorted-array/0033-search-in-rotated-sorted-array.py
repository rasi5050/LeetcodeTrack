class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot and do binary search on left and right segments
        pivot=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                pivot=i+1
                
        def binarySearch(left, right):
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
        inLeft=binarySearch(0, pivot-1)
        inRight=binarySearch(pivot, len(nums)-1)
        if inLeft or inLeft==0: return inLeft
        if inRight or inRight==0: return inRight
        return -1
                
        