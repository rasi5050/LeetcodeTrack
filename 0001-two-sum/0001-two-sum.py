class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,num in enumerate(nums):
            map[num]=i
        for i,num in enumerate(nums):
            if target-num in map and map[target-num]!=i:
                return [i, map[target-num]]