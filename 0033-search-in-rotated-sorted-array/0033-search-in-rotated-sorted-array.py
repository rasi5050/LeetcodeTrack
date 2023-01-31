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
                    
        #status: correct
        #Analysis: Time O(log n), Space O(1)
        #ref: 1/31/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day98/98Blind39/75;doLeetcodeBlind75-3q/day-9/45Q:completeOn2/15/2023-Day4/15:1.numberOfIslandsTimed25Mins-x1pomo(6:00-6:30),2.rottingOrangesTimed25Mins-x1pomo(6:30-7:00),3.searchInARotatedSortedArrayTimed25Mins-x1pomo(7:00-7:30),4.combinationSumTimed25Min-x1pomo(7:30-8:00),5.implement-x1pomo(8:00-8:30),6.couresWork:DAA:flippedClassroom:P1:DAA:fliipedClassroom:watchReccurenceRelation(https://drive.google.com/drive/u/1/folders/0AJMcog-ghtHLUk9PVA)-x4pomo(8:30-10:30),7.absorber-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
