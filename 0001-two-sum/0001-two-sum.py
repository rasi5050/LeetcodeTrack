class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """workingCode
        # map={}
        # for i,num in enumerate(nums):
        #     map[num]=i
        # for i,num in enumerate(nums):
        #     if target-num in map and map[target-num]!=i:
        #         return [i, map[target-num]]
        """
    #status: correct:
    #analysis: Space O(n)
    #Time O(n)
    
    #improvement: idea from leetocde discussion solution (https://leetcode.com/problems/two-sum/discuss/2669414/Python-solution-oror-Easy-to-understand)
        
        # idea:two iterations of the elements are reduced to one, add elements after checking if target-num in map, then if not add to map. this avoid eg) 3 to 3 mapped case
        map={}
        for i,num in enumerate(nums):
            if target-num in map:return [i, map[target-num]]
            map[num] = i
        
        #status: success
        #analysis: space O(n)
        #Time O(n)
        #ref: 11/17/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day40/40:(P1:doPaypalLeetcodeQuestion1/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.twoSumTimed25Mins-x1pomo(5:30-6:00),2.longestSubstringWithoutRepeatingCharactersTimed25Mins-x1pomo(6:00-6:30),3.implement-x2pomo(6:30-7:30),4.medianOfTwoSortedArraysTimed25Mins-x1pomo(7:30-8:00),5.implement-x2pomo(8:00-9:00),6.zigzagConversionTimed25Mins-x1pomo(9:00-9:30),7.implement-x2pomo(9:30-10:30)=x10pomo(5:30-10:30)
