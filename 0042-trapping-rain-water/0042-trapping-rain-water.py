class Solution:
    def trap(self, height: List[int]) -> int:
        #intuition: table for current state (help from neetcode youtube solution: https://www.youtube.com/watch?v=ZI2z5pq0TqA)
        
        maxLeft=[]
        curLeft=0
        for h in height:
            maxLeft.append(curLeft)
            curLeft=h if h>curLeft else curLeft
        maxRight=[]
        curRight=0    
        for h in reversed(height):
            maxRight.append(curRight)
            curRight=h if h>curRight else curRight
        maxRight.reverse()
        rain=0
        for i,h in enumerate(height):
            rain+=max(min(maxLeft[i],maxRight[i])-h,0)
        return rain
        
        
        