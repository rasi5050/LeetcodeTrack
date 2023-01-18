class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        freq=0
        lastVisited=nums[0]
        for n in nums:
            if n==lastVisited:
                freq+=1
                if freq>len(nums)//2:
                    return n
            else:
                lastVisited=n
                freq=1