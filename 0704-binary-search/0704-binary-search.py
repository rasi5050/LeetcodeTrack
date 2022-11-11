class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #intuition: do binary search O(nlogn)
        #steps:
        #0.while right<=left:
        #1.left=0, right=len(nums)-1
        #2.mid=(left+right)//2
        #3.if nums[mid]==target: return
        #4.elif target<nums[mid]: right=mid-1
        #5.elif taget>nums[mid]: left=mid+1
        #6.return -1
        
        #implement
        
        left=0
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
    
    #status: correct, clocked 10mins in first attempt using google timer
    #ref:11/1/2022P2:rack1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day29/30:do,1.sudokuSolverLogic+implement-x2pomo(7:30-8:30),2.study:sortingAndSearching-x2pomo(8:30-9:30),3.binarySearchLogic-x1pomo(9:30-10:00)=x5pomo(7:30-10:00)

            