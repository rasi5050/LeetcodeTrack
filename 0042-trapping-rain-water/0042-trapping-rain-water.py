class Solution:
    def trap(self, height: List[int]) -> int:
#         maxHToLeft=[]
#         leftMax=0
#         maxHToRight=[]
#         rightMax=0
#         for h in height:
#             maxHToLeft.append(leftMax)
#             leftMax=max(leftMax, h)
            
#         for h in reversed(height):
#             maxHToRight.append(rightMax)
#             rightMax=max(rightMax, h)
#         maxHToRight.reverse()
#         res=0
#         for i,h in enumerate(height):
#             res+=max(min(maxHToLeft[i], maxHToRight[i])-h,0)
#         return res
    
        #idea2: two pointers, trapping is limited by the lowest height, then increment that side pointer.
        l,r=0,len(height)-1
        leftMax,rightMax=height[l], height[r]
        res=0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax, height[r])
                res+=rightMax-height[r]
        return res