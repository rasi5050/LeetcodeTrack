class Solution:
    def trap(self, height: List[int]) -> int:
        maxHToLeft=[]
        leftMax=0
        maxHToRight=[]
        rightMax=0
        for h in height:
            maxHToLeft.append(leftMax)
            leftMax=max(leftMax, h)
            
        for h in reversed(height):
            maxHToRight.append(rightMax)
            rightMax=max(rightMax, h)
        maxHToRight.reverse()
        res=0
        for i,h in enumerate(height):
            res+=max(min(maxHToLeft[i], maxHToRight[i])-h,0)
        return res
            