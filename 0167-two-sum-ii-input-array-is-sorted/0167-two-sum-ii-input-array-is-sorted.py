class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        left, right=numbers[0], numbers[-1]
        #shrink the window to get sum target
        while l<r:
            curSum=left+right
            if curSum==target:
                return [l+1,r+1]
            elif curSum>target:
                r-=1
                right=numbers[r]
            else:
                l+=1
                left=numbers[l]
        