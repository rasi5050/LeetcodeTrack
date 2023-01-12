from collections import Counter
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter, prefSum, count = Counter({0:1}), 0, 0
        for num in nums:
            prefSum+=num
            count+=counter[prefSum-goal]
            counter[prefSum]+=1
        return count
   
        