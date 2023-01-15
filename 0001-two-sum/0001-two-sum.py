class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,val in enumerate(nums):
            required=target-val
            if required in map:
                return [i,map[required]]
            map[val]=i
        #status: correct
        #Analysis: Time O(n), Space O(n)
        #ref: 1/15/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day82/82C3Ai3QuestionsFromMostFrequentListOf0/10Day2/5+Blind75WeekOne0/14q,2q/dayDay2/7-,1.bestTimeToBuyAndSellStocksTimed25Mins-x1pomo(12:30-13:00),2.implement-x1pomo(13:00-13:30),3.validPalindromeTimed25Mins-x1pomo(13:30-14:00),4.implement-x1pomo(14:00-14:30),5.invertBinaryTimed25Mins-x1pomo(14:30-15:00),6.implement-x1pomo(15:00-15:30),7.validAnagramTimed25Mins-x1pomo(15:30-16:00),8.implement-x1pomo(16:00-16:30),9.absorber-x1pomo(16:30-17:00)=x9pomo(12:30-17:00)delayed;5.longestArithmeticSubsequenceTimed25Mins-x1pomo(13:00-13:30),Blind753q/Day,7.2SumTimed25Mins-x1pomo(13:30-14:00),8.validParenthesesTImed25Mins-x1pomo(14:00-14:30),9.mergeTwoSortedListsTimed25Mins-x1pomo(14:30-15:00)

        