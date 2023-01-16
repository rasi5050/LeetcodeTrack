class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left,right=0,len(nums)-1     
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
    #status: correct
    #Analysis: Time O(log n); binary search, Space O(1)
    #ref: 1/15/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day82/82C3Ai3QuestionsFromMostFrequentListOf0/10Day2/5+Blind75WeekOne0/14q,2q/dayDay2/7-,1.binarySearchTimed25Mins-x1pomo(18:30-19:00),2.implement-x1pomo(19:00-19:30),3.floodFillTimed25Mins-x1pomo(19:30-20:00),4.implement-x1pomo(20:00-20:30)=x4pomo(18:30-20:30)
