class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,val in enumerate(nums):
            required=target-val
            if required in map:
                return [i,map[required]]
            map[val]=i
        