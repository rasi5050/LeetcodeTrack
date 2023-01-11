class Solution:
    def trap(self, height: List[int]) -> int:
        leftHeights = [0]*len(height)
        rightHeights = [0]*len(height)
        
        for i in range(1,len(height)):
            leftHeights[i] = max(height[i-1], leftHeights[i-1])
        
        for j in range(len(height)-2, -1, -1):
            rightHeights[j] = max(height[j+1], rightHeights[j+1])
        
        rain=0
        for r in range(len(height)):    
            if (val:=min(leftHeights[r], rightHeights[r])-height[r])>0: rain+=val
        return rain
                