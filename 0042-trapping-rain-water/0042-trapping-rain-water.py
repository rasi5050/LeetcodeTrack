class Solution:
    def trap(self, height: List[int]) -> int:
        #capture current's max left height
        
        leftMax=[0]*len(height)
        rightMax=[0]*len(height)
        rain=0
        for i in range(1, len(height)):
            leftMax[i]=max(leftMax[i-1],height[i-1])
        
        for j in range(len(height)-1-1, -1, -1):
            rightMax[j]=max(rightMax[j+1],height[j+1])
        
        for l,r,h in zip(leftMax, rightMax, height):
            rain+=min(l,r)-h if (min(l,r)-h)>0 else 0
        return rain 