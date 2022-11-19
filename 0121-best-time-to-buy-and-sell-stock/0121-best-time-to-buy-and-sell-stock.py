class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #intuition: maintain cur min, max table
        
        leftMin=[]
        curMin=prices[0]
        for price in prices:
            curMin=min(price, curMin)
            leftMin.append(curMin)
        
        rightMax=[]
        curMax=prices[-1]
        for price in reversed(prices):
            curMax=max(price, curMax)
            rightMax.append(curMax)
        rightMax.reverse()
        maxProfit=0
        for i,j in zip(rightMax, leftMin):
            maxProfit=max(maxProfit, i-j)
        return maxProfit
            
         
    
