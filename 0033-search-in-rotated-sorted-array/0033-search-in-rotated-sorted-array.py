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
        if inLeft or inLeft==0: return inLeft    #included the zero index case here
        if inRight or inRight==0: return inRight    #included the zero index case here
        return -1
                
        #status: correct
        #Analysis: Time O(n + nlogn + nlogn)=O(n Logn), Space O(1)
        #ref: 1/14/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day81/82C3Ai3QuestionsFromMostFrequentListOf10Day1/5+Blind75WeekOne14q,2q/dayDay1/7-,0.void-x4pomo(5:30-7:30),1.3.JP Morgan Chase & Co. – NAMR SEP - Campus Hiring - 2023 Batch:lastDateUnknown:assumingLastDate1/15/2023;doOn1/14/2023-x2pomo(6:30-7:30),2.addQuestionsToDrive-x1pomo(7:30-8:00),3.searchInRotatedSortedArrayTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.largestPerimeterTriangleTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(7:30-11:30)delayed;1.searchInRotatedSortedArrayTimed25Mins-x1pomo(10:30-11:00),2.implement-x1pomo(11:00-11:30)

        
        