class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #valid triangle is a+b>c for all sides, sum of two sides should be strictly greater than third side for any combination of a, b, c
        """
        #brute force O(n^3)
        maxPeri=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    a,b,c=nums[i], nums[j], nums[k]
                    if a+b>c and b+c>a and c+a>b:
                        maxPeri=max(maxPeri, a+b+c)
        return maxPeri
        """
                        
        #idea:sort(idea from leetcode solution)
                
        nums.sort()
        for i in range(len(nums)-1-2,-1,-1):
            a,b,c=nums[i], nums[i+1], nums[i+2]
            if a+b>c:
                return a+b+c
        return 0
    
        # encore: why does this work:
        #consider sorted array:
        """
        [1,2,2,3,5]         then a+b=5 and c=5; ==> a+b!>c
             a b c 
        why does there cant be a combination of [c,3,5] because it is guranteed that initial a+b had the highest sum of 2+3, that was not enough to match the c value, hence any value less than 2 can have only value less than 2+3, that will not be not enough to match c value.
        hence the the last a, b, c was the only possible combination, simillarly for b value also.
        so the next possible value of c should be 3, for which a,b,c=2,2,3 satisfies traingle inequality
        """
        
    
        #status: correct (idea from leetcode solution)
        #Analysis: Time O(n), Space O(1)
        #ref: 1/14/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day81/82C3Ai3QuestionsFromMostFrequentListOf10Day1/5+Blind75WeekOne14q,2q/dayDay1/7-,0.void-x4pomo(5:30-7:30),1.3.JP Morgan Chase & Co. – NAMR SEP - Campus Hiring - 2023 Batch:lastDateUnknown:assumingLastDate1/15/2023;doOn1/14/2023-x2pomo(6:30-7:30),2.addQuestionsToDrive-x1pomo(7:30-8:00),3.searchInRotatedSortedArrayTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.largestPerimeterTriangleTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(7:30-11:30)delayed;1.searchInRotatedSortedArrayTimed25Mins-x1pomo(10:30-11:00),2.implement-x1pomo(11:00-11:30)

        