class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map={}
        # for i,num in enumerate(nums):
        #     map[num]=i
        # for i,num in enumerate(nums):
        #     if target-num in map and map[target-num]!=i:
        #         return [i, map[target-num]]
    #status: correct:
    #analysis: Space O(n)
    #Time O(n)
    
    #improvement: idea from leetocde discussion solution (https://leetcode.com/problems/two-sum/discuss/2669414/Python-solution-oror-Easy-to-understand)
        
        # idea:two iterations of the elements are reduced to one, add elements after checking if target-num in map, then if not add to map. this avoid eg) 3 to 3 mapped case
        map={}
        for i,num in enumerate(nums):
            if target-num in map:return [i, map[target-num]]
            map[num] = i
        