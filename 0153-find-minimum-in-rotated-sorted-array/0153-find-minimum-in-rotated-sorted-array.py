class Solution:
    def findMin(self, nums: List[int]) -> int:
        #intuition: do modified binary search to find pivot
        
        #skipping binary search if already sorted
        if nums[0]<nums[-1]:
            return nums[0]
        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[right] < nums[mid]:
                left=mid+1
            else:
                right=mid-1
                
                
        #status: correct
        #ref:11/4/2022P2:rack1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day32/32:do,1.findMinInRotatedSortedArrayTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00),3.medianOfTwoSortedArrayTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.matrixTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.absorber-x1pomo(11:00-11:30)=x10pomo(6:30-11:30)
        
        #assumptions made in thinking process: 
        #1.O(logn)==>thought:binarySearch(not a strong reason per se, but has higher probablity)
        #2.addOn:deductedFromFailedTestCase: elif nums[mid-1] > nums[mid]:
                # return nums[mid]