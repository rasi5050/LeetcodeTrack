class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #intuition: find pivot, apply binary search on left side and right side of pivot separately
        
        #steps:
        #identify pivot
        #1.for i in range(len(nums)-1):
        #2.if nums[i]>nums[i+1]: pivot=i+1;break
        #3.appy merge sort on left and right
        #4.return index, else return -1
        
        if len(nums)==1 and nums[0]==target:
            return 0
        
        pivot=len(nums)-1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                pivot=i+1
                break
        #merge sort
        left=0
        right=pivot-1
        if nums[left]<=target<=nums[right]:
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        else:
            left=pivot
            right=len(nums)-1
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                elif target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return -1