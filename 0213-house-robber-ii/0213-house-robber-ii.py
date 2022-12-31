class Solution:
    def rob(self, nums: List[int]) -> int:
       
        if len(nums)==1: return nums[0]
        house1=house2=0
        for moneyFromCurHouse in nums:
            temp=max(moneyFromCurHouse + house1, house2)
            house1=house2
            house2=temp
        houseR2=houseR1=0
        for moneyFromCurHouse in reversed(nums):    #... n R2 R1
            temp=max(moneyFromCurHouse + houseR1, houseR2)
            houseR1=houseR2
            houseR2=temp
        
        return max(house1, houseR1)