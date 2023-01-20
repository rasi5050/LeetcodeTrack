class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #insert interval and merge
        if not intervals: return [newInterval]
        inserted=False
        for i in range(len(intervals)):
            if newInterval[0]<=intervals[i][0]:
                intervals.insert(i, newInterval)
                inserted=True
                break
        if not inserted: intervals.append(newInterval)
        def checkOverlap(a,b):
            return b[0]<=a[1] and b[1]>=a[0] or a[1]>=b[0] and a[0]<=b[1]

        def mergeOverlap(a,b):
            return [min(a[0],b[0]),max(a[1],b[1])]
        
        res=[intervals[0]]
        for inter in intervals[1:]:
            a,b=res[-1], inter
            if checkOverlap(a, b):
                res[-1]=mergeOverlap(a,b)
            else:
                res.append(inter)
        return res
    
    #status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/20/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day87/88C3Ai3QuestionsFromMostFrequentListOf10/10Day6/5+Blind20/75,2q/dayDay6/7; 1.Count Vowels PermutationTimed25Mins-x1pomo(6:00-6:30),2.reachingPointsTimed25Mins-x1pomo(6:30-7:00),3.longestArithmeticSequenceTimed25Mins-x1pomo(7:00-7:30),3.diameterOfABinaryTreeTimed25Mins-x1pomo(7:30-8:00),4.implement-x1pomo(8:00-8:30),5.middleOfLinkedListTimed25Mins-x1pomo(8:30-9:00),6.maximumDepthOfBinaryTreeTimed25Mins-x1pomo(9:00-9:30),7.containsDuplicateTimed25Mins-x1pomo(9:30-10:00),8.maximumSubarrayTimed25Mins-x1pom(10:00-10:30),9.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)  
