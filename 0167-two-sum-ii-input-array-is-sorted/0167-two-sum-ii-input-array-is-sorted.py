class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        left, right=numbers[0], numbers[-1]
        #shrink the window to get sum target
        while l<r:
            curSum=left+right
            if curSum==target:
                return [l+1,r+1]
            elif curSum>target:
                r-=1
                right=numbers[r]
            else:
                l+=1
                left=numbers[l]
        #Status: correct
        #Analysis: Time O(n), Space O(1)
        #ref: 1/26/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day93/94Blind29/75,2q/dayDay12/12;1.P1:doOA:1.robotRoomCleaner-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.numberOfGoodLeafNodesPairsTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.3SumTimed25Mins-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.binaryTreeLevelOrderTraversalTimed25Mins-x1pomo(9:00-9:30),8.cloneGraph-x1pomo(9:30-10:00),9.Evaluate Reverse Polish NotationTimed25Mins-x1pomo(10:00-10:30),10.implement-x1pomo(10:30-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
