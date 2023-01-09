class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp={}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dp[(j, nums[j]-nums[i])] = dp.get((i,nums[j]-nums[i]), 1) + 1
        return max(dp.values())
                
    #status: correct; didnot understand; idea from leetcode discussions solutions (https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274611/JavaC%2B%2BPython-DP)
    #Analysis: Time O(n^2), Space O(n^2)
    #ref:1/9/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day76/76-,1.countVowelsPermutationsTimed25Mins-x1pomo(18:00-18:30),2.implement-x2pomo(18:30-19:30),3.absorber-x1pomo(19:30-20:00)=x4pomo(18:00-20:00)early(12:30-14:30)              
