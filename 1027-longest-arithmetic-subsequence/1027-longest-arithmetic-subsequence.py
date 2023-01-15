class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        map={}
        for i in range(len(nums)):
            flag=True
            for j in range(i+1, len(nums)):
                diff=nums[j]-nums[i]
                map[j, diff]=map.get((i,diff),1)+1
        return max(map.values())
                